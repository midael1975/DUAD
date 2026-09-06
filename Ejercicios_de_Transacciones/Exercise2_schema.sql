DO $$
DECLARE
    -- Input data for the transaction (you can change these values)
    v_user_id      INT := 1;

    -- We simulate a "cart" with temporary table or array.
    -- Here we'll use a temporary table for clarity.
BEGIN
    ----------------------------------------------------------------
    -- 1) Prepare sample data for the purchase (only for the exercise)
    ----------------------------------------------------------------
    -- Create a temporary table to hold the products to buy
    CREATE TEMP TABLE temp_cart (
        product_id INT,
        quantity   INT
    ) ON COMMIT DROP;

    -- Insert some example items (change IDs to match your data)
    INSERT INTO temp_cart(product_id, quantity) VALUES
        (1, 2),   -- product 1, quantity 2
        (2, 1);   -- product 2, quantity 1

    ----------------------------------------------------------------
    -- 2) Start explicit transaction
    ----------------------------------------------------------------
    BEGIN
        -- Check that user exists
        IF NOT EXISTS (SELECT 1 FROM users WHERE id = v_user_id) THEN
            RAISE EXCEPTION 'User % does not exist', v_user_id;
        END IF;

        ----------------------------------------------------------------
        -- 3) Validate stock for each product in the cart
        ----------------------------------------------------------------
        PERFORM 1
        FROM temp_cart c
        JOIN products p ON p.id = c.product_id
        WHERE p.stock < c.quantity;

        IF FOUND THEN
            RAISE EXCEPTION 'Not enough stock for one or more products';
        END IF;

        ----------------------------------------------------------------
        -- 4) Calculate total and insert bill
        ----------------------------------------------------------------
        -- Compute total from cart and product prices
        -- We use a SELECT to sum line totals
        DECLARE
            v_total NUMERIC(10,2);
            v_bill_id INT;
        BEGIN
            SELECT SUM(c.quantity * p.price)
            INTO v_total
            FROM temp_cart c
            JOIN products p ON p.id = c.product_id;

            IF v_total IS NULL THEN
                RAISE EXCEPTION 'Cart is empty';
            END IF;

            -- Insert bill header
            INSERT INTO bills(user_id, total, status)
            VALUES (v_user_id, v_total, 'Created')
            RETURNING id INTO v_bill_id;

            ----------------------------------------------------------------
            -- 5) Insert bill items and reduce stock
            ----------------------------------------------------------------
            INSERT INTO bill_items(bill_id, product_id, quantity, unit_price, line_total)
            SELECT
                v_bill_id,
                c.product_id,
                c.quantity,
                p.price,
                c.quantity * p.price
            FROM temp_cart c
            JOIN products p ON p.id = c.product_id;

            -- Reduce stock
            UPDATE products p
            SET stock = p.stock - c.quantity
            FROM temp_cart c
            WHERE p.id = c.product_id;

            RAISE NOTICE 'Purchase completed. Bill id: %, total: %', v_bill_id, v_total;
        END;
    EXCEPTION
        WHEN OTHERS THEN
            -- If anything fails, rollback the transaction
            RAISE NOTICE 'Error in purchase transaction: %', SQLERRM;
            ROLLBACK;
            RETURN;
    END;

    -- If we reach here, transaction was successful
    COMMIT;
END;
$$ LANGUAGE plpgsql;

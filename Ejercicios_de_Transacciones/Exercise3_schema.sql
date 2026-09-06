DO $$
DECLARE
    v_bill_id INT := 1;  -- bill to be returned (change as needed)
BEGIN
    ----------------------------------------------------------------
    -- 1) Start transaction
    ----------------------------------------------------------------
    BEGIN
        -- Check that bill exists
        IF NOT EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id) THEN
            RAISE EXCEPTION 'Bill % does not exist', v_bill_id;
        END IF;

        -- Optional: check if already returned
        IF EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id AND status = 'Returned') THEN
            RAISE EXCEPTION 'Bill % is already returned', v_bill_id;
        END IF;

        ----------------------------------------------------------------
        -- 2) Increase stock for each product in the bill
        ----------------------------------------------------------------
        -- We use bill_items to know what was bought
        UPDATE products p
        SET stock = p.stock + bi.quantity
        FROM bill_items bi
        WHERE bi.bill_id = v_bill_id
          AND bi.product_id = p.id;

        ----------------------------------------------------------------
        -- 3) Mark bill as returned
        ----------------------------------------------------------------
        UPDATE bills
        SET status = 'Returned'
        WHERE id = v_bill_id;

        RAISE NOTICE 'Bill % has been returned and stock updated', v_bill_id;
    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE 'Error in return transaction: %', SQLERRM;
            ROLLBACK;
            RETURN;
    END;

    COMMIT;
END;
$$ LANGUAGE plpgsql;



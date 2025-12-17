products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_category = {}
for product in products:
    category = product["category"]
    price = product["price"]
    total_category[category] = total_category.get(category, 0) + price

print(total_category)

#from collections import defaultdict

#total_category = defaultdict(int) # Use int, which defaults to 0
#for product in products:
    #category = product["category"]
    #price = product["price"]
    #total_category[category] += price

#print(dict(total_category)) # Convert back to a regular dict for printing

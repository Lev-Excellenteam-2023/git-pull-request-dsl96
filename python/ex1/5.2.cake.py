def get_recipe_price(*, d_products , optional = None , **d_amount):
    if not optional :
        optional = []

    sum = 0
    for name,cost in d_products.items():

       if name in optional:
           continue

       if name not in d_amount:
           print(f"ERROR {name} in products but not in amount")
           continue

       sum = sum + cost * d_amount[name]

    return sum/100




c = get_recipe_price(d_products={'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
print(c)
product={"milk":25,
         "biscuit":20,
         "mixture":50}
product_name=input("Enter your product name : ")
if product_name.lower() in product:
    print("price : ",product[product_name.lower()])
else:
    print("product not found...")


# Output :

# Enter your product name : milk
# price :  25

# Enter your product name : Milk
# price :  25

# Enter your product name : Bun
# product not found...

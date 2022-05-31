foodList=["chicken fry","beef fry","porotta","biriyani","idli"]
print("3rd item is :",foodList[2])
foodList.append("fish curry")
print("after added item:",foodList)
foodList.insert(3,"tacos")
print("updated food list:",foodList)


# output
# 3rd item is : porotta
# after added item: ['chicken fry', 'beef fry', 'porotta', 'biriyani', 'idli', 'fish curry']
# updated food list: ['chicken fry', 'beef fry', 'porotta', 'tacos', 'biriyani', 'idli', 'fish curry']
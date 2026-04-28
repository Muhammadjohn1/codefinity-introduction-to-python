vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)
if "carrorts" in vegetables:
    print("Carrorts are already in the list.")
elif "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")
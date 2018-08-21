
lucky_numbers = [4,8,15,16,23,42]
vegetables = ["Brocolli","Spinach","Cabbage","Asparagus"]

vegetables.append("Creed")  # using the append function to add an additional item to the end of a list
vegetables.insert(1, "Brussels")  # using the insert function to add an additional item to a specific index of a list

print(vegetables.count("Brussels"))  # count number of times an items appears in the list
vegetables.sort()  # sort list in ascending order
print(vegetables)
print(vegetables.index("Spinach"))
vegetables.remove("Asparagus")  # remove an item from a list
print(vegetables)
vegetables.pop()  # remove the last item at the end of the list
print(vegetables)

vegetables.clear()  # clear an entire list
print(vegetables)  # list is now empty
vegetables.insert(1,"Legumes")  # using the insert function to add an additional item to a specific index of a list
print(vegetables)  # print list

vegetables.extend(lucky_numbers)  # using the extend function to add two lists together
print(vegetables)
lucky_numbers.reverse()  # using reverse to reverse the order of list items
print(lucky_numbers)

vegetables.reverse()  # using reverse to reverse the order of list items
print(vegetables)

veggies2 = vegetables.copy()  # using the copy function to copy list of friends
print(veggies2)  # print new copy of list of friends

new_numbers = lucky_numbers.copy()  # using the copy function to copy list of friends
print(new_numbers)  # print new copy of list of friends

new_numbers.append(100)  # adding a new number to your numbers list
print(new_numbers)  # print new copy of list of friends



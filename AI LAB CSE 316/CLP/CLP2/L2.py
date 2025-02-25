
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = []

for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)
print("Common Elements:", common_elements)
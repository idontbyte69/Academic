
numbers = [5, 3, 8, 3, 2, 8, 1, 5]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

for i in range(len(unique_numbers)):
    for j in range(i + 1, len(unique_numbers)):
        if unique_numbers[i] > unique_numbers[j]:
            unique_numbers[i], unique_numbers[j] = unique_numbers[j], unique_numbers[i]
            
print("Sorted Unique List:", unique_numbers)

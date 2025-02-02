numbers = input("Enter numbers: ").split()
numbers = [int(n) for n in numbers]

if len(numbers) < 2: 
    print("Give more then 2 numbers.")
else:
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    secondHighest = None
    
    for i in range(len(numbers)-2,-1,-1):
        if numbers[i] != numbers[-1]:
            secondHighest = numbers[i]
            break
    if secondHighest is None:
        print("All are same")
    else:
        print("Second highest number:", secondHighest)
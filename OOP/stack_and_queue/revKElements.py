def revKElements(input_numbs, k):
    numbs = []
    final_numbs = []
    for i in range(k):
        numbs.append(input_numbs[0])
        input_numbs.pop(0)
        
    for i in range(k):
        input_numbs.insert(0, numbs[0])
        numbs.pop(0)
    return input_numbs

input_values = input("Enter the numbers: ")
input_values = input_values.split(',')
numbers = []

for numb in input_values:
    numbers.append(int(numb))

k = int(input("Enter the k: "))
print(revKElements(numbers, k))
def strrev(input_string):
    letters = []
    reversed_letters = []
    for i in input_string:
        letters.append(i)
        
    for j in range(len(letters)):
        reversed_letters.append(letters[-1])
        letters.pop()

    result = ""
    for ch in reversed_letters:
        result = result + ch
    
    return result

my_string = input("Enter the string to be reversed: ")
result = strrev(my_string)
print("Reversed String:", result)
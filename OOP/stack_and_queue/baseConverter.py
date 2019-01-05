def baseConverter(decNum, base):
    numb = 1
    power = 0
    stack = []
    vals = []
    multiplier = 1
    final_ans = 0

    while(numb <= decNum):
        numb = base**power
        stack.append(numb)
        power+=1

    numb = decNum
    while(stack[-1] > numb):
        stack.pop()

    for i in range(len(stack)):
        if stack[-1] <= numb:
            takeout = int(numb/stack[-1])
            vals.insert(0, takeout)
            numb-=(takeout*stack[-1])
            stack.pop()
        else:
            stack.pop()
            vals.insert(0, 0)



    for i in range(len(vals)):
        final_ans+=vals[i]*multiplier
        multiplier*=10

    return final_ans

dec_numb = int(input("Enter the decimal number: "))
base = int(input("Enter the base: "))

print(baseConverter(dec_numb, base))
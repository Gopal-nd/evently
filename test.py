def space(num):
    digits=[]
    while num>0:
        dig = num%10
        digits.append(dig)
        num//=10
    digits.reverse()
    for i in digits:
        print(i," ")
num = int(input("enter the number"))
space(num)

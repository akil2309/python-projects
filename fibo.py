terms = int(input("how many terms?"))
n1 = 0
n2 = 1
count =0
if terms <= 0:
    print("enter the positive number")
elif terms == 1:
    print("fibonacci series upto ", terms)
    print(n1)
else:
    print("fibonacci series: ")
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

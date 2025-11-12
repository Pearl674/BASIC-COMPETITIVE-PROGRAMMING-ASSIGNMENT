N=int(input("Enter how many numbers: "))
A=list(map(int, input("Enter numbers: ").split()))
total = 0
for x in A:
    total = total + x
print(total)

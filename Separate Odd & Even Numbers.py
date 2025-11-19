A=[1, 2, 3, 4, 5]
odd=""
even=""
for x in A:
    if x%2!=0:
        odd += str(x) + " "
    else:
        even += str(x) + " "
print(odd.strip())
print(even.strip())




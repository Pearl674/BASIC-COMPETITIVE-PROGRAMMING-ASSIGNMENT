t=int(input())
for i in range(t):
    s=input()
    print(1 if s == s[::-1] else 0)

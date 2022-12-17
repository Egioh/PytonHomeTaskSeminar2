n=int(input("n="))
div=0
for i in range(n,1,-1):
    if n%i==0:
        div=i
print(div)
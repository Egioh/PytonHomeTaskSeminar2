from random import randint
n=int(input("n="))
avers =0
revers =0
nikle=[randint(0,1) for i in range (n)]
for i in range (n):
   if (nikle[i]==0):
    avers+=1
   else:
    revers+=1
   print(nikle[i])
if avers<revers:
    print(avers)
else:
    print(revers)

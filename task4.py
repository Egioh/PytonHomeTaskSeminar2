pupils = [165, 163, 162, 162, 160, 160, 157, 157, 155, 154]
petya =162
place =0
for i in range (len(pupils)):
    if pupils[i]<petya:
        place = i+1
        break
print(place)

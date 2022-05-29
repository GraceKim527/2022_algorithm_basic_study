n = int(input())
count = 0

list_alight = list(map(int, input().split()))
list_blight =[]

for _ in range(n):
    list_blight.append(0)

for i,a in enumerate(list_alight):
    if (list_alight[i] != list_blight[i]) and (n-i>=3):
        list_blight[i] = not list_blight[i] 
        list_blight[i+1] = not list_blight[i+1] 
        list_blight[i+2] = not list_blight[i+2]
        count += 1
    elif (list_alight[i] != list_blight[i]) and (n-i==2):
        list_blight[i] = not list_blight[i] 
        list_blight[i+1] = not list_blight[i+1] 
        count += 1
    elif (list_alight[i] != list_blight[i]) and (n-i==1):
        list_blight[i] = not list_blight[i] 
        count += 1

print(count)




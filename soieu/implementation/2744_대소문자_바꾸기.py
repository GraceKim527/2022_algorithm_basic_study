n = input()
result =''

for i in n:
    if i.isupper() == True:
        result = result + i.lower()
        
    else:
        result = result + i.upper()
print(result)
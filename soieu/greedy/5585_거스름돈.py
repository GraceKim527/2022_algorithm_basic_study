result = 0
# 거스름돈 화폐 종류
MONEY_TYPE = [500, 100, 50, 10, 5, 1]

# 내야할 금액
price = int(input())

# 받아야할 금액
remain = 1000 - price

for money in MONEY_TYPE:
    result += remain // money
    remain = remain % money
    
print(result)
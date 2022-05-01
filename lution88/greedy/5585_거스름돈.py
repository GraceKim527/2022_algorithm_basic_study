# 잔돈 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
# 거스름돈 개수 가장 적게 주기.
# PR test


def change_coin():
    change = 1000 - int(input())
    cnt = 0
    coin_list = [500, 100, 50, 10, 5, 1]
    for coin in coin_list:
        cnt += (change // coin)
        change = change % coin
    return cnt


print(change_coin())

# change = 1000 - int(input())
# cnt = 0

# coin_list = [500, 100, 50, 10, 5, 1]
# for coin in coin_list:
# 	cnt += (change // coin)
# 	change = change % coin

# print(cnt)

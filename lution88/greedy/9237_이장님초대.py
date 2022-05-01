# 나무 심는 데 1일
# 나무가 다 자라고 나서 이장 초대 1일
# PR TEST


def grow_days():
    num_tree = int(input())
    g_days = list(map(int, input().split()))
    g_days.sort(reverse=True)

    for i in range(num_tree):
        g_days[i] = g_days[i] + (i + 1)
    return max(g_days) + 1


print(grow_days())
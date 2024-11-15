# [1,2,5,10,20,50] = 48[20,20,5,2,1]
# [1,2,5,10,20,50,100,200,500] = 67[50,10,5,2]


# greedy
# [1,5,2,10,20,50]
# def Greedy(coins, amount):
#     coins.sort(reverse=True)
#     count = 0
#     array = []

#     for i in coins:
#         count = count + amount // i
#         if amount // i > 0:
#             que = amount // i
#             for j in range(que):
#                 array.append(i)
#         amount = amount % i
#         if amount == 0:
#             break
#     if amount == 0:
#         print("Number of coins required :", count)
#         print("coins :", array)
#     else:
#         print("this amount can not be maked")


# Greedy([1, 3, 4], 6)
# minimum = 2(6)


# 47 =[10,10,10,10,5,2]


# Dynamic programing
def dynamic(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in coins:
            if i - j >= 0:  # or i >= j
                dp[i] = min(dp[i], dp[i - j] + 1)
    if dp[amount] != amount + 1:
        print("minimum coins required :", dp[amount])
        print(dp)
    else:
        print("can not make this amount")


dynamic([1, 3, 4], 6)
# dynamic = time consuming but correct
# array = [6] * 5
# print(array)

# backtracking

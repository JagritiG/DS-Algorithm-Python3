# Buy and sell stocks


# Method-1: using brute force
# Time complexity: O(n^2)
# Space complexity: O(1)
# def buy_sell_stock(arr):
#     max_profit = 0
#     for i in range(len(arr) - 1):
#         for j in range(i+1, len(arr)):
#             if arr[j] - arr[i] > max_profit:
#                 max_profit = arr[j] - arr[i]
#
#     return max_profit


# Method-2:
# Time complexity: O(n)
# Space complexity: O(1)
def buy_sell_stock(arr):
    max_profit = 0.0
    min_price = arr[0]

    for price in arr:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


if __name__ == "__main__":

    stock_price = [410, 420, 415, 395, 390, 410, 400, 405, 425]
    print(buy_sell_stock(stock_price))


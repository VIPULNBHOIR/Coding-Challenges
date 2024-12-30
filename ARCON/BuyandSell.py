def BestStock(stocks: list[int])-> int:
    profit = 0
    min_stock = stocks[0]

    for curr in range(1, len(stocks)):
        profit = max(profit, stocks[curr] - min_stock )

        min_stock = min(min_stock, stocks[curr])

    return profit

print(BestStock([1,4,8,9,2,5]))

print(BestStock([9,8,6,5,5,4,3,2,1]))

print(BestStock([2,5,8,9,8,2,12,1,15]))
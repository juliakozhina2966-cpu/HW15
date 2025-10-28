from Task1 import rod_cutting

prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

cuts, profit = rod_cutting(prices, n)
print("Recommended cuts:", cuts)
print("Maximum profit:", profit)

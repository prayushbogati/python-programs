def sum(*nums):
    """sums the given numbers"""
    total = 0
    for num in nums:
        total += num
    return total

try:
    x = sum(1, 2, 4, "hi")
    print(x)
except:
    print("Error!")
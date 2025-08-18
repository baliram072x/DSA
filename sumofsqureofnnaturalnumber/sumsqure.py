# def sum_of_squares(n):
#     if n == 0:
#         return 0
#     return n * n + sum_of_squares(n - 1)

# n = int(input("Enter a number: "))
# print("Sum of squares of first", n, "natural numbers is:", sum_of_squares(n))


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    # using formula
    result = (n * (n + 1) * (2 * n + 1)) // 6
    
    print("Sum of squares of first", n, "natural numbers is:", result)

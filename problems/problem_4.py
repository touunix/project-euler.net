"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


class Problem4:
    @staticmethod
    def get_largest_palindrome_product() -> None:
        max_palindrome: int = 0
        for number_1 in range(999, 99, -1):  # loop through all products of two 3-digit numbers
            for number_2 in range(number_1, 99, -1):  # only loop downwards to avoid duplicate products
                product: int = number_1 * number_2
                if str(product) == str(product)[::-1] and product > max_palindrome:
                    max_palindrome: int = product
        print(max_palindrome)


if __name__ == "__main__":
    app: Problem4 = Problem4()
    app.get_largest_palindrome_product()

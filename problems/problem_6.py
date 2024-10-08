"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


class Problem6:
    @staticmethod
    def sum_square_difference() -> None:
        n: int = 100
        sum_of_the_squares: int = sum(i ** 2 for i in range(1, n + 1))
        square_of_the_sum: int = sum(range(1, n + 1)) ** 2
        difference: int = square_of_the_sum - sum_of_the_squares
        print(difference)


if __name__ == "__main__":
    app: Problem6 = Problem6()
    app.sum_square_difference()

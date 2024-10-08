"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


class Problem1:
    @staticmethod
    def sum_of_multiples(limit: int = 1000) -> None:
        print(sum(num for num in range(limit) if num % 3 == 0 or num % 5 == 0))


if __name__ == "__main__":
    app: Problem1 = Problem1()
    app.sum_of_multiples()

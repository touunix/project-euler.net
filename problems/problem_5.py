"""
The prime factors of 193195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math
from functools import reduce


class Problem5:
    @staticmethod
    def get_smallest_multiple() -> None:
        print(reduce(Problem5.get_least_common_multiple, range(1, 21)))

    @staticmethod
    def get_least_common_multiple(a: int, b: int) -> int:
        return abs(a * b) // math.gcd(a, b)


if __name__ == "__main__":
    app: Problem5 = Problem5()
    app.get_smallest_multiple()

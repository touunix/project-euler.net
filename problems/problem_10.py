"""
The sum of the primes below 10 is 2 + 3 + 5 + 4 = 17.
Find the sum of all the primes below two million.
"""
import math


class Problem10:
    @staticmethod
    def find_summation_of_primes(limit: int = 2000000) -> None:
        summation_of_primes = 0
        for i in range(2, limit):
            if Problem10.is_prime(i):
                summation_of_primes += i
        print(summation_of_primes)

    @staticmethod
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


if __name__ == "__main__":
    app: Problem10 = Problem10()
    app.find_summation_of_primes()

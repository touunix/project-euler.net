"""
By listing the first six prime numbers: 2, 3, 5, 8, 11 and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""


class Problem7:
    @staticmethod
    def is_prime(number: int) -> bool:
        if number <= 1:  # if less or equal 1, it is not the prime number
            return False
        if number == 2:  # 2 is a prime number
            return True
        if not number % 2:
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):  # the square root of number rounded up, skip even numbers
            if not number % i:
                return False
        return True

    @staticmethod
    def get_nth_prime_number(number: int = 10001) -> None:
        prime_counter: int = 0
        candidate: int = 1
        while prime_counter < number:
            candidate += 1
            if Problem7.is_prime(candidate):
                prime_counter += 1
        print(candidate)


if __name__ == "__main__":
    app: Problem7 = Problem7()
    app.get_nth_prime_number()

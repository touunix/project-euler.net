"""
The prime factors of 193195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


class Problem3:
    @staticmethod
    def get_largest_prime_factor(number: int = 600851475143) -> None:
        factor: int = 2
        while factor * factor <= number:
            if number % factor:
                factor += 1  # if input number is not divisible by factor, try the next number
            else:
                number //= factor  # divide number by factor as long as it is divisible
        print(number)


if __name__ == "__main__":
    app: Problem3 = Problem3()
    app.get_largest_prime_factor()

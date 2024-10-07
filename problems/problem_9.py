"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


class Problem9:
    @staticmethod
    def find_special_pythagorean_triplet() -> None:
        for a in range(1, 1000):
            for b in range(a + 1, 1000 - a):
                c: int = 1000 - b - a
                if a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


if __name__ == "__main__":
    app: Problem9 = Problem9()
    app.find_special_pythagorean_triplet()

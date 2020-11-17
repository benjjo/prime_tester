import math


class PrimeNumberTest:
    """
    To test n for primality, divide by all of the primes less than the square root of n.
    some big ones:
    100003679       Total time: 0.8540897369384766
                    Total time: 12.958332300186157 Traditional method
    1000004249      Total time: 6.87762188911438
                    Total time: 141.87551712989807 Traditional method
    10000004873     Total time: 62.29244923591614
    100000004953    Total time: 218.40894222259521
    1000000005721   Total time: 1866.14448595047
    """

    def big_number_test(self, n):
        """
        Tests n for primality using prime_test, against a list of numbers provided by prime_filter. Returns True if
        n is prime, otherwise False.
        :param n:
        :return boolean:
        """
        prime_list = self.prime_filter(n)
        isPrime = True if n % 2 and prime_list else False
        while isPrime and prime_list:
            if not (n % prime_list.pop()):
                isPrime = False
        return isPrime

    def prime_filter(self, n):
        """
        Returns a list of prime numbers from 3 to the square root of n using prime_test.
        T(n) = 1 + 1 + (sqrt(n/2) * 1)
        O(sqrt(n/2))
        :param n:
        :return list:
        """
        maximum = int(math.sqrt(n))
        prime_list = []
        for i in range(3, maximum, 2):
            if self.prime_test(i):
                prime_list.append(i)
        return prime_list

    def prime_test(self, n):
        """
        Loops through the integer range of 3 to n in steps of 2 (odd numbers) and checks for a modulus of 0.
        If no 0 is found
        T(n) = 1 + 1 + ((n * 1) / 2) = T(2+n)
        O(n/2)
        :param n:
        :return boolean:
        """
        isPrime = True if n % 2 else False
        count = 3
        while isPrime and count < n:
            if not (n % count):
                isPrime = False
            count += 2
        return isPrime

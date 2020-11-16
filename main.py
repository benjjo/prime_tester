import math
import time


class prime_number_test():
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

        """
        prime_list = self.prime_filter(n)
        isPrime = True if n % 2 and prime_list else False
        while isPrime and prime_list:
            if not (n % prime_list.pop()):
                isPrime = False
        return isPrime

    def prime_filter(self, n):
        """
        T(n) = 1 + 1 + (sqrt(n) * 1)
        O?
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
        T(n) = 1 + 1 + (n * 1) = T(2+n)
        O(n)
        :param n:
        :return:
        """
        isPrime = True if n % 2 else False
        count = 3
        while isPrime and count < n:
            if not (n % count):
                isPrime = False
            count += 2
        return isPrime
"""
def main():
    pnt = prime_number_test()
    pnt.big_number_test(9)


if __name__ == '__main__':
    main()
"""
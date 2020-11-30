from main import *
import time

pnt = PrimeNumberTest()

failed = 0
ran = 0

def test(name, actual, expected):
    """Report if test passed or failed."""
    global ran, failed
    if actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1


# print("Testing a wee number using prime_test (traditional loop method).")
# test("Testing 19 for prime. Expect True.", pnt.prime_test(19), True)

# start = time.time()
# print("\nTesting a bigger number using prime_test (traditional loop method).")
# test("Testing 100003679 for prime. Expect True.", pnt.prime_test(100003679), True)
# duration = time.time() - start
# print("Total time: %10.2f" % duration)

# print("\nTesting a wee number using big_number_compact_test (Square root method).")
# test("Testing 19 for prime. Expect True.", pnt.big_number_compact_test(19), True)

start = time.time()
print("\nTesting a bigger number using big_number_new_test. (1000000016531)")
test("Testing for prime. Expect True.", pnt.prime_quick_test(1000000016531), True)
duration = time.time() - start
print("Total time: %10.5f" % duration)

file = open("primeNumbers.txt", "a")
start = time.time()
for i in range(1000000016531, 1000000026531, 2):
    if pnt.prime_quick_test(i):
        file.write(str(i) + "\n")
        print("Prime: " + str(i))
file.close()
print("Total time: %10.2f" % duration)

# start = time.time()
# print("\nTesting a bigger number using big_number_compact_test. (1000004249)")
# test("Testing for prime. Expect True.", pnt.big_number_compact_test(1000004249), True)
# duration = time.time() - start
# print("Total time: %10.2f" % duration)
#
# start = time.time()
# print("\nTesting an even bigger number using big_number_test. (1000004249)")
# test("Testing for prime. Expect True.", pnt.big_number_test(1000004249), True)
# duration = time.time() - start
# print("Total time: %10.2f" % duration)

# start = time.time()
# print("Testing an even bigger number using big_number_test. (Square root method)")
# test("Testing 1000000005719 for prime. Expect False.", pnt.big_number_test(1000000005719), False)
# duration = time.time() - start
# print("Total time: %10.2f" % duration)

print('================================================')
print('All tests run:', ran - failed, 'OK,', failed, 'FAILED')
print('================================================')

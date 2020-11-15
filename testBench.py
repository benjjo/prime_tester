from main import *

pnt = prime_number_test()

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


print("Testing big number method.")
test("Testing 19 for prime. Expect True.", pnt.big_number_test(19), True)

start = time.time()
print("Testing big number method.")
test("Testing 100003679 for prime. Expect True.", pnt.big_number_test(100003679), True)
duration = time.time() - start
print("Total time: %10.5f" % duration)

print('================================================')
print()
print('All tests run:', ran - failed, 'OK,', failed, 'FAILED')
print('================================================')

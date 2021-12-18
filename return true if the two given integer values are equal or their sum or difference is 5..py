

#Write a Python program which will return true if the two given integer values are equal or their sum or difference is 5.

def test_numbers(x,y):

    if x == y or (x-y) == 5 or (x+y) == 5:

        return True

    else:

        return False

print(test_numbers(7, 2))
print(test_numbers(3, 2))
print(test_numbers(2, 2))
print(test_numbers(7, 3))
print(test_numbers(27, 53))
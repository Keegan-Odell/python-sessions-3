# Your task is to make a function that can take any non-negative integer
# as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 21445 Output: 54421
# Input: 145263 Output: 654321
# Input: 1254859723 Output: 9875543221
def descending_order(num):
    num_as_list = list(map(int, str(num)))
    num_ordered_list = []
    higher_num = 0
    while len(num_as_list) != 0:
        for i in num_as_list:
            test_num = i

            if higher_num < test_num:
                higher_num = test_num
        num_ordered_list.append(higher_num)
        num_as_list.remove(higher_num)
        higher_num = 0
    return int(''.join(map(str, num_ordered_list)))


# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    numbers_list = [int(num) for num in numbers.split()]
    return str(max(numbers_list)) + ' ' + str(min(numbers_list))


# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count





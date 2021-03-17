def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) + 1):
        if (list_of_nums{[i-1] == list_of_nums[i] + 1} and
            list_of_nums[i-2] == list_of_nums[i] + 2):
            return True
        elif list_of_nums[i+1] != list_of_nums[i] - 1:
            i -= 1
        else:
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print("Answer1: ", answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print("Answer2: ", answer2) # should print True

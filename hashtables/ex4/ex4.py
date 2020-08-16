def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    positive_nums = {}

    for num in a:
        if num >= 0:
            if num not in positive_nums:
                positive_nums[num] = None

    for num in a:
        if num < 0:
            neg_to_pos = (num * (-1))
            if neg_to_pos in positive_nums:
                if neg_to_pos not in result:
                    result.append(neg_to_pos)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

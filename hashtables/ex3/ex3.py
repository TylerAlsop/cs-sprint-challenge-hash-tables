def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    numbers_from_arrays = {}

    for array in arrays:
        for number in array:
            if number not in numbers_from_arrays:
                numbers_from_arrays[number] = None
            else:
                if number not in result:
                    result.append(number)
    print(result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

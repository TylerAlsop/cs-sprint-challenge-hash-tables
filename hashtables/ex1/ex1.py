def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # U. 
        # We are given: 
            # A list with each itme in the list being the weight of an item.
            # A length which is the length of the list.
            # A weight limit.
        # We need to see if the weight of any two items combined is equal to the weight limit.
        # If none do then we return NONE
        # If two items do exist then we return a tuple containing the indices of each item from the list.
            # The index of item with the higher weight should be in the zero-th place in the tuple and the lighter one in the first index of the tuple.

    # P.
        # Create a hash table to store data.
    weight_and_indices = {}        

        # Use a for loop to loop over the "weights" list.
    for weight in weights:
        # Create Varialbes for the indicies
        index_num = weights[weight]
        weight_and_indices.key = weight
        weight_and_indices.value = index_num
            # For each item in the list we want to save the weight to the hash table as the key and the index number of that weight as the value.
        # Loop over the hash table to see if any of two keys add up to the weight limit.
            # If that doesn't exist return NONE
            # Else return the values of the two keys.
        # Find the higher number and save it to the zeroth index in a tuple and the other number in the first index of the tuple.
        # Return the tuple.

    print(weight_and_indices)

    return weight_and_indices


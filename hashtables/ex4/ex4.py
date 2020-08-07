def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for i in a:
        if i not in cache:
            cache[i] = i
    
    for x in cache:
        if x < 0 and abs(cache[x]) in cache:
            result.append(abs(cache[x]))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

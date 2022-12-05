def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayTwo.sort()
    smallest_diff = abs(arrayOne[0] - arrayTwo[0])
    smallest_set = [arrayOne[0], arrayTwo[0]]
    for x in arrayOne:
        i = 0
        current_diff = abs(x - arrayTwo[i])
        previous_diff = current_diff
        while current_diff <= previous_diff:
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                smallest_set = [x, arrayTwo[i]]
            if i < len(arrayTwo)-1:
                previous_diff = current_diff
                i += 1
                current_diff = abs(x - arrayTwo[i])
            else:
                break
    return smallest_set

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        x = array[i]
        for j in range(i+1, len(array)-1):
            y = array[j]
            for k in range(j+1, len(array)):
                z = array[k]
                if x + y + z == targetSum:
                    triplets.append([x, y, z])
    return triplets

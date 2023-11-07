def edit_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    dp = [[0 for x in range(len_str1+1)] for y in range(len_str2+1)]

    for i in range(len_str2+1):
        for j in range(len_str1+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insertion
                                 dp[i-1][j],        # Deletion
                                 dp[i-1][j-1])      # Replacement

    return dp


def print_operations(dp, str1, str2):
    i = len(str2)
    j = len(str1)
    operations = []

    while i > 0 and j > 0:
        if str2[i-1] == str1[j-1]:
            i, j = i-1, j-1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            operations.append('Replace {} with {}'.format(str1[j-1], str2[i-1]))
            i, j = i-1, j-1
        elif dp[i][j] == dp[i][j-1] + 1:
            operations.append('Insert {}'.format(str2[i-1]))
            j = j-1
        elif dp[i][j] == dp[i-1][j] + 1:
            operations.append('Delete {}'.format(str1[j-1]))
            i = i-1

    while j > 0:
        operations.append('Delete {}'.format(str1[j-1]))
        j = j-1
    while i > 0:
        operations.append('Insert {}'.format(str2[i-1]))
        i = i-1

    return operations[::-1]

# Example usage:
str1 = 
str2 = 
dp_matrix = edit_distance(str1, str2)
operations = print_operations(dp_matrix, str1, str2)

print('Edit Distance Matrix:')
for row in dp_matrix:
    print(row)
print('\nTransformations:')
for operation in operations:
    print(operation)

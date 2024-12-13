def nums_sums(*args):
    # Sum negative and positive numbers
    negative_sum = sum(n for n in args if n < 0)
    positive_sum = sum(n for n in args if n > 0)
    return negative_sum, positive_sum


# Get the input and convert it into a list of integers
nums = list(map(int, input().split()))  # Convert map object to list

# Unpack the sums into neg_nums and pos_nums
neg_nums, pos_nums = nums_sums(*nums)

# Print the results
print(neg_nums)
print(pos_nums)

# Compare the absolute value of negative sum with positive sum
if abs(neg_nums) > pos_nums:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negative")

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(nums):
    return nums[-1]
nums_sorted = sorted(nums, key=last_char, reverse=True)
print(nums_sorted)

##########LAMBDA   ##############


nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
yo = lambda nums: nums[-1]
nums_sorted_lambda = sorted(nums, key=yo , reverse=True)


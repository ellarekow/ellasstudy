phrase = input("What would you like to calculate: ").strip()

nums = phrase.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
nums = [float(i) for i in nums]

ops = []
for item in phrase:
    if not item.isdigit():
        ops.append(item)

while len(nums) > 1 and len(ops) > 0:
    if ops.__contains__('*') or ops.__contains__('/'):
        for i in ops:
            if i == '*' or i == '/':
                loc = ops.index(i)
                break
        if ops[loc] == '*':
            ans = nums[loc] * nums[loc+1]
            del nums[loc]
            nums[loc] = ans
            del ops[loc]
        else:
            ans = nums[loc] / nums[loc + 1]
            del nums[loc]
            nums[loc] = ans
            del ops[loc]
    else:
        if ops[0] == '+':
            ans = nums[0] + nums[1]
            del nums[0]
            nums[0] = ans
            del ops[0]
        else:
            ans = nums[0] - nums[1]
            del nums[0]
            nums[0] = ans
            del ops[0]

print('= ' + str(nums[0]))


nums = [3,3,4,2]
target = 6

def check():

    for j in range(len(nums)):
        for i in range(j,len(nums)):
            if nums[j]+nums[i] == target and j != i:
                print(f'{nums[j]}[{j}] + {nums[j]}[{i}] = {target}') 

def check2():

    for j in range(len(nums)):
        for i in range(j,len(nums)):
            if nums[i] == target - nums[j] and j != i:
                print(f'{nums[j]}[{j}] + {nums[j]}[{i}] = {target}') 

check2()
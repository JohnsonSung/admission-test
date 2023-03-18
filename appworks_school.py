
# Question 1:
# You are required to complete the following two functions.
# 1. find_max: find the max value of an array of numbers.

def find_max(numbers):
    max_num = 0
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num        



# 2. find_position: find the first position of the target number inside an array of numbers. The position
# should be counted starting from 0, if you can't find the target, please return -1.

def find_position(numbers, target):
    position = -1
    for number in numbers:
        if target in numbers:
            position+=1
            if number == target:
                break
        else:
            position=-1    
            
    return position
        
# Question 2:
# 1. count: return an object which shows the count of each character.

def count(input):
    counts = {}
    for char in input:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# 2. group_by_key: return an object which shows the summed up value of each key.

def group_by_key(input):
    result = {}
    for i in input:
        key = i['key']
        value = i['value']
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]



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

def count(input1):
    counts = {}
    for char in input1:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

# 2. group_by_key: return an object which shows the summed up value of each key.

def group_by_key(input2):
    result = {}
    for i in input2:
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

# Question 3:

# 1. What is Git and why is it used?

# 1-1: 什麼是Git?: 
# Ans: Git是一種分散式的版本控制系統
# 1-2: 為什麼用Git?:
# Ans: 因為Git是免費跟開源的,而且commit的速度快而且檔案又小,每次commit的時候都會留下紀錄,方便去查看版本間的差異性,在離線時也可以在local端操作,如果多人協作一個專案時,
# 也可以各自開Branch,等到開發完成後,在merge到master裡面


# 2. What is the difference between List, Dictionary, Tuple and Set in Python?
# Ans: List是用[]呈現,而且列表裡面的資料是可以被變動或取代的,列表內的資料則是用序列取得,例如 list[0],list[1],list[2]...
#      Tuple是用()呈現,也是列表,但是裡面的資料卻不可被變動,然後取得資料也是以序列取得,例如 tuple[0],tuple[1],tuple[2]...
#      Dictionary則是以{}來呈現,如果是已字典的方式使用,則必須要有key與value搭配使用,裡面的資料是可以被更動或刪除,但必須以key當代表,處理新增,刪除,或變動資料,例如dict[key],dict[key1]...
#      Set()集合最後會是以{}呈現,但他不需要key搭配value,而且他的內容元素必須是不重複的,例如set1 = set('banana'), set1印出來會是: {'a', 'b', 'n'},重複的元素會被過濾且結果是沒有順序的

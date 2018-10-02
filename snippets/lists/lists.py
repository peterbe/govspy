# initialize list
numbers = [0] * 5
# change one of them
numbers[2] = 100
some_numbers = numbers[1:3]
print(some_numbers)  # [0, 100]
# length of it
print(len(numbers))  # 5

# initialize another
scores = []
scores.append(1.1)
scores[0] = 2.2
print(scores)  # [2.2]

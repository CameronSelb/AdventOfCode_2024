left, right = [], []
distance = 0
total_count = 0

with open('Day_1/puzzle_input.txt', 'r') as input:
    for line in input:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    if left[i] > right[i]:
        distance += left[i] - right[i]
    else:
        distance += right[i] - left[i] 

print(f"Total Distance: {distance}")

for num in left:
    total_count += num * right.count(num)

print(f"Similarity Score: {total_count}")
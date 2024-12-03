#Part 1

file = open("input.txt", "r")
numbers = file.read()
file.close()

lines = numbers.split("\n")

list1 = []
list2 = []

for line in lines:
    temp = line.split("   ")
    list1.append(temp[0])
    list2.append(temp[1])

list1 = sorted(list1)
list2 = sorted(list2)

total = 0

for i in range(len(list1)):
    total += abs(int(list1[i])-int(list2[i]))

print(total)

#PART 2

total = 0

for num in list1:
    if num in list2:
        count = 1
        i = list2.index(num) + 1
        while list2[i] == num:
            count += 1
            i += 1
        total += (int(num) * count)

print(total)

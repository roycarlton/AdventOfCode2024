import re

file = open("input.txt", "r")
data = file.read()
file.close()

matches = re.findall("mul\(\d{1,3},\d{1,3}\)", data)

total = 0

for match in matches:
    nums = match[4:][:-1].split(",")
    total += (int(nums[0]) * int(nums[1]))

print(total)
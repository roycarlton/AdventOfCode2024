def is_safe(report):
    diff = report[1] - report[0]
    if abs(diff) > 3 or abs(diff) < 1:
        return False
    if diff > 0:
        ascending = True
    else:
        ascending = False

    for i in range(2, len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        if (diff > 0) != ascending:
            return False
        
    return True



file = open("input.txt", "r")
data = file.read()
file.close()

total_safe = 0

for report in data.split("\n"):
    formatted_report = []
    for level in report.split(" "):
        formatted_report.append(int(level))
    
    if is_safe(formatted_report):
        total_safe += 1

print(total_safe)

#PART 2
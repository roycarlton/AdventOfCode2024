def apply_dampener(report):
    for i in range(len(report)):
        temp_report = report[:]
        temp_report.pop(i)
        if is_safe(temp_report, False):
            return True
    return False

def is_safe(report, dampener):
    diff = report[1] - report[0]
    if abs(diff) > 3 or abs(diff) < 1:
        if dampener:
            return apply_dampener(report)
        else:
            return False
    if diff > 0:
        prev_ascending = True
    else:
        prev_ascending = False

    for i in range(2, len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) > 3 or abs(diff) < 1:
            if dampener:
                return apply_dampener(report)
            else:
                return False
        if (diff > 0) != prev_ascending:
            if dampener:
                return apply_dampener(report)
            else:
                return False
        prev_ascending = (diff > 0)
        
    return True



file = open("input.txt", "r")
data = file.read()
file.close()

total_safe = 0

for report in data.split("\n"):
    formatted_report = []
    for level in report.split(" "):
        formatted_report.append(int(level))
    
    if is_safe(formatted_report, False):
        total_safe += 1

print(total_safe)

#PART 2

total_safe = 0

for report in data.split("\n"):
    formatted_report = []
    for level in report.split(" "):
        formatted_report.append(int(level))
    
    if is_safe(formatted_report, True):
        total_safe += 1

print(total_safe)
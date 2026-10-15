
def classify(value):
    if value < 148:
        return "Below range"
    elif value <= 152:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result


count = int(input("Enter the number of soap bars: "))

total = 0
below_count = 0
in_count = 0
above_count = 0

for i in range(count):
    weight = int(input("Enter the soap bar weight: "))

    classification = classify(weight)
    print(classification)

    total += weight

    if classification == "Below range":
        below_count += 1
    elif classification == "In range":
        in_count += 1
    else:
        above_count += 1

average = calculate_average(total, count)

print(f"Total weight: {total} g")
print(f"Average weight: {average} g")
print(f"Below range: {below_count}")
print(f"In range: {in_count}")
print(f"Above range: {above_count}")

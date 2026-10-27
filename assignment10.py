def replace_value(values,index,new_value):
    values[index] =  new_value
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1    
def summarize(values):
    return (min(values), max(values), sum(values)) 
days_count = int(input("Enter number of days: "))  
original = [] 
for _ in range(days_count):
    time_value = int(input("Enter cooking time in minutes: "))
    original.append(time_value) 
updated = original[:] 
index_to_correct = int(input("Enter the index to correct: "))
new_time = int(input("Enter the new cooking time: "))
replace_value(updated, index_to_correct, new_time)  
target = int(input("Enter the cooking time to search for: ")) 
first_index = find_first(updated, target)
match_count = updated.count(target)
minimum,maximum,total = summarize(updated) 
sorted_list = sorted(updated) 
print()
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum cooking time: {minimum} minutes")
print(f"Maximum cooking time: {maximum} minutes")
print(f"Total cooking time: {total} minutes") 
if first_index != -1: 
    print(f"First matching index: {first_index}")  
else:
    print("Target not found")  


print(f"Matching values: {match_count}") 

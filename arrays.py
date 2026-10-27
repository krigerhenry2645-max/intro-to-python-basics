# ===== 1. LISTS / ARRAYS - store many items =====
ages = [21, 72, 43, 76, 23, 78, 88, 90, 15]  # list
names = ["Zack", "Jane", "Jack", "Moha", "Rick", "Jack"]

# list functions
ages.append(31)
# ages.clear()
# ages.sort()
# ages.reverse()
print(f"ages: {ages}")
print(f"names: {names}")

jack_count = names.count("Jack")
print(f"Jack appears: {jack_count} times")
print(f"Total names: {len(names)}")

# ===== 2. MORE LIST OPERATIONS =====
numbers = [10, 20, 30, 40, 50]

print(f"First: {numbers[0]}, Last: {numbers[-1]}")

numbers.append(60)
numbers.insert(1, 15)
print(f"After add: {numbers}")

numbers.remove(15)
numbers.pop()
print(f"After remove: {numbers}")

# Looping (most important)
for num in numbers:
    print(num)

total = sum(numbers)
print(f"Total sum = {total}, Max = {max(numbers)}, Min = {min(numbers)}")

# ===== 3. SET - no duplicates =====
scores = {90, 85, 90, 78, 85}
print(f"Set scores (duplicates removed): {scores}")

# ===== 4. TUPLE - immutable (cannot change) =====
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(f"Tuple first day: {weekdays[0]}")
print(f"All weekdays: {weekdays}")

# ===== 5. DICTIONARY - key: value =====
person = {"name": "Jason", "age": 22, "weight": 54, "height": 1.88}
print(person["name"])
print(person["age"])
print(person["weight"])
print(f"Full person: {person}")


#
people = [
    {"name":"Jason","age":22},
{"name":"Mike ","age":26},
{"name":"Bon","age":24},
]

print(people[0]["age"])


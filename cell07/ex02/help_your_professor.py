def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "j": 1,
    "e": 5,
    "n": 8,
    "n": 9,
    "i": 2,
    "e": 3
}

class_C = {
    "b": 20,
    "o": 15,
    "a": 10,
    "t": 12
}

print(f"Average for class B: {average(class_B)}.")
print(f"Average for class C: {average(class_C)}.")
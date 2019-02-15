# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []

# for n in humans:
#     if n.name.startswith("D"):
#         a.append(n.name)

a = [h.name for h in humans if h.name.startswith("D")]

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []

for n in humans:
    if n.name.endswith("e"):
        b.append(n.name)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

for n in humans:
    if n.name.startswith(("C", "D", "E", "F", "G")):
        c.append(n.name)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []

for n in humans:
    older = Human(n.name, n.age)
    older.age = n.age + 10
    d.append(older.age)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []

for n in humans:
    nameAge = f"{n.name}-{n.age}"
    e.append(nameAge)

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for n in humans:

    if 26 < n.age < 33:
        nameAge = (n.name, n.age)
        f.append(nameAge)


print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
g = []

for n in humans:
    cap = Human(n.name, n.age)
    cap.age = n.age + 5
    cap.name = n.name.upper()
    g.append(cap)

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = []

import math

for n in humans:
    sqrroot = Human(n.name, n.age)
    sqrroot.age = math.sqrt(n.age)
    h.append(sqrroot.age)

print(h)

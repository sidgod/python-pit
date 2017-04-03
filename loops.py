number = 1

while number <= 10:
    print(number)
    number += 1

print("=" * 80)

for number in range(1, 11):
    print(number)

print("=" * 80)

for letter in "sidgod":
    print(letter)

string = "sidgod"

vowels = 0
consonanats = 0

for letter in string:
    if letter in "aeiou":
        vowels += 1
    else:
        consonanats += 1

print("String {} has {} vowels and {} consonants".format(string, vowels, consonanats))

event_numbers = [x for x in range(1, 100) if x % 2 == 0]

print(event_numbers)
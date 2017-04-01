# Health Potion Game
import random
import math

health = 50

difficulty = 1

potion_health = int(random.randint(25, 50) / difficulty)

health += potion_health

print(health)

# Other basic math stuff
print(round(2.1))
print(round(1.5))
print(round(1.51, 1))
print(round(1.55, 1))

print(math.floor(3.9))
print(math.ceil(2.1))
print(math.pi)
print(math.e)

# resultant vectors
print(math.hypot(3, 4))

print(math.pow(2, 3))
print(2 ** 3)

print(math.exp(1))

print(math.log(math.e))

print(math.log10(1000))

print(math.log2(8))
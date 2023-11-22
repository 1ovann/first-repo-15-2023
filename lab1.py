music = "Skryabin"

print(f"My favourite music band - {music}.")

#
#
#
#

score = "87"
positive_score = "60"

if score >= positive_score:
    result = "positive, keep going this way!"
else:
    result = "negative, work more!"

print(f"Your score {score} is {result}")

#
#
#
#

is_even = True
is_odd = False

a = is_even and is_odd
print(f"AND - {a}")
b = is_even or is_odd
print(f"OR - {b}")
c = not is_even
print(f"NOT EVEN - {c}")
d = not is_odd
print(f"NOT ODD - {d}")

#
#
#
#

import math

x = 1.155
y = 3.981

result = math.log(x**2+4*x*y+y**2) - 12*math.cos(x*y**4) + 13*x**6

print(f"Result is {result}")


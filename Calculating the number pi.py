# Question interview about calculating the number pi

import random

def calculate_pi(n):
  points_circle = 0

  for i in range (1,n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x**2 + y**2
    if distance <= 1:
      points_circle += 1
  return (4*points_circle/n)

print("The number pi is: ", calculate_pi(100000))
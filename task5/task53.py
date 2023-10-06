import csv
import random

random_numbers = [random.randint(0, 100) for _ in range(1000)]

with open("random_numbers.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Index", "Value"])
    for index, value in enumerate(random_numbers):
        writer.writerow([index, value]) 
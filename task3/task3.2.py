import math
def g(m2, r):
    G = 6.67430 * math.pow(10,-11) 
    return (G * (5.97237 * math.pow(10,24) * m2)) / r**2

masses = { "Меркурий": 3.3011 * math.pow(10,23), "Венера": 4.8675 * math.pow(10,24), "Марс": 6.4171 * math.pow(10,23), "Юпитер": 1.8982 * math.pow(10,27), "Сатурн": 5.6834 * math.pow(10,26), "Уран": 8.6810 * math.pow(10,25), "Нептун": 1.02413 * math.pow(10,26)}
distances = {"Меркурий": 9.3 * math.pow(10,7),  "Венера": 4.1 * math.pow(10,7),  "Марс": 7.7 * math.pow(10,7),  "Юпитер": 6.14 * math.pow(10,8),  "Сатурн": 1.2 * math.pow(10,9),  "Уран": 2.8 * math.pow(10,9),  "Нептун": 4.3 * math.pow(10,9)}

for planet in masses:
    force = g(masses[planet], distances[planet])
    print(f"Притяжение планеты {planet}: {force} Н")

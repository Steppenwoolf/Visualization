import pygal
from Dice.die import Die

# Создание 2x кубик
die_a = 6
die_b = 6
times = 100000
die1 = Die(die_a)
die2 = Die(die_b)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(times):
    result = die1.roll() + die2.roll()
    results.append(result)
# Анализ результатов
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
hist = pygal.Bar()
hist.title = "Results of rolling two " + str(die_a) + ' & ' + str(die_b) + ' dices ' + str(times) + "times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add(str(die_a) + ' & ' + str(die_b), frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)


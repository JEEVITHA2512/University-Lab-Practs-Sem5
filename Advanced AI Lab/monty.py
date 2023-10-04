import random
import matplotlib.pyplot as plt

def switch_doors_experiment():
    correct_door = random.choice([1, 2, 3])
    door = random.choice([1, 2, 3])
    doors = [1, 2, 3]

    try:
        doors.remove(door)
        doors.remove(correct_door)
    except:
        pass

    random_incorrect_door = random.choice(doors)
    doors = [1, 2, 3]
    doors.remove(random_incorrect_door)
    doors.remove(door)
    final_choice = doors[0]

    if final_choice == correct_door:
        return 1
    else:
        return 0

def probability_of_success_on_switch_door(precision):
    switch_door = 0
    for i in range(precision):
        switch_door += switch_doors_experiment()
    return switch_door / precision

runs = 100
total = 0
x = []
y = []
precision = 100000

for i in range(runs):
    total += probability_of_success_on_switch_door(precision)
    x.append(i + 1)
    y.append(total / (i + 1))

plt.plot(x, y)

plt.xlabel('Runs')
plt.ylabel('Probability of success while switching')
plt.title('Monty Hall problem')
plt.ylim(0, 1)
plt.xlim(1, runs)
plt.show()

print("Probability of success on switching door for {} precision and {} runs is {}".format(precision, runs, total / runs))

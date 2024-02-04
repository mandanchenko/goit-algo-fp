import random
from collections import defaultdict

import matplotlib.pyplot as plt

nums = 1_000_000

counts = defaultdict(int)

for _ in range(nums):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dices = dice1 + dice2
    counts[dices] += 1

probabilities = {key: count / nums for key, count in counts.items()}
print(probabilities)

# відсортовуємо словник з вірогідностями за ключем для виведення впорядкованої таблиці
sorted_probabilities = dict(sorted(probabilities.items()))

print("Dice | Probability")
print("-----|------------")
for dice, prob in sorted_probabilities.items():
    print(f"{dice: <4} | {prob:.2%}")


plt.bar(probabilities.keys(), probabilities.values())  # noqa
plt.show()

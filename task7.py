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
# відсортувати за значенням ключа
sorted_counts = dict(sorted(probabilities.items()))

print(sorted_counts)
print(probabilities)
print("Dice | Probability")
print("-----|------------")
for dice, prob in probabilities.items():
    print(f"{dice: <4} | {prob:.2%}")


plt.bar(probabilities.keys(), probabilities.values())  # noqa
plt.show()
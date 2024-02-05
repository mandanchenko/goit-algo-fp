def greedy_algorithm(items, budget):
    # Створюємо список страв, які будемо обирати
    selected_items = []

    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    # Обираємо страви жадібно
    total_cost = 0
    total_calories = 0
    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    # Повертаємо результат
    result = {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

    return result


def dynamic_programming(items, budget):
    # Ініціалізуємо матрицю для зберігання результатів
    dp_matrix = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    # Заповнюємо матрицю
    for i in range(1, len(items) + 1):
        for w in range(budget + 1):
            cost = items[list(items.keys())[i - 1]]["cost"]
            calories = items[list(items.keys())[i - 1]]["calories"]

            # Обчислюємо максимальну калорійність для даного бюджету
            if cost <= w:
                dp_matrix[i][w] = max(dp_matrix[i - 1][w], dp_matrix[i - 1][w - cost] + calories)
            else:
                dp_matrix[i][w] = dp_matrix[i - 1][w]

    # Відновлюємо оптимальний набір страв
    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp_matrix[i][j] != dp_matrix[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    # Повертаємо результат
    result = {
        "selected_items": selected_items,
        "total_cost": sum(items[item]["cost"] for item in selected_items),
        "total_calories": dp_matrix[len(items)][budget]
    }

    return result

if __name__ == "__main__":
    # Наявні страви
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    # Заданий бюджет
    budget = 100

    # Викликаємо функцію жадібного алгоритму з заданими даними
    result = greedy_algorithm(items, budget)

    # Виводимо результат
    print("Результати жадібного алгоритму:")
    print("Обрані страви:", result["selected_items"])
    print("Загальна ватрість:", result["total_cost"])
    print("Загальні калорії:", result["total_calories"])

    # Викликаємо функцію алгоритму динамічного програмування з тими самими даними
    result_dp = dynamic_programming(items, budget)

    # Виводимо результат
    print("Результати алгоритму динамічного програмування:")
    print("Обрані страви:", result_dp["selected_items"])
    print("Загальна ватрість:", result_dp["total_cost"])
    print("Загальні калорії:", result_dp["total_calories"])


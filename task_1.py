import heapq

def min_connection_cost(cables):
    # Якщо кабель один або немає кабелів, витрати 0
    if len(cables) <= 1:
        return 0
    
    # Створюємо мінімальну купу з довжин кабелів
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(heap) > 1:
        # Беремо два найкоротші кабелі
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        
        # Рахуємо вартість їх з'єднання
        connection_cost = cable1 + cable2
        
        # Додаємо вартість до загальної суми
        total_cost += connection_cost
        
        # Додаємо об'єднаний кабель назад до купи
        heapq.heappush(heap, connection_cost)
    
    return total_cost

def print_connection_steps(cables):
    if len(cables) <= 1:
        print("Немає необхідності в з'єднанні")
        return
    
    heap = cables.copy()
    heapq.heapify(heap)
    
    step = 1
    total_cost = 0
    
    while len(heap) > 1:
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        connection_cost = cable1 + cable2
        total_cost += connection_cost
        
        print(f"Крок {step}: З'єднуємо кабелі довжиною {cable1} та {cable2}")
        print(f"Вартість з'єднання: {connection_cost}")
        print(f"Поточна загальна вартість: {total_cost}")
        print()
        
        heapq.heappush(heap, connection_cost)
        step += 1
    
    print(f"Фінальна вартість: {total_cost}")

# Тестуємо рішення
def test_cable_connection():
    test_cases = [
        ([4, 3, 2, 6], 29),  # Базовий випадок
        ([1], 0),            # Один кабель
        ([1, 2], 3),         # Два кабелі
        ([5, 5, 5, 5], 40),  # Однакові довжини
        ([], 0)              # Порожній список
    ]
    
    for i, (cables, expected) in enumerate(test_cases, 1):
        result = min_connection_cost(cables)
        print(f"\nТест {i}:")
        print(f"Кабелі: {cables}")
        print(f"Очікувана вартість: {expected}")
        print(f"Отримана вартість: {result}")
        print(f"Тест {'пройдено' if result == expected else 'не пройдено'}")
        
        if cables:
            print("\nПокроковий процес з'єднання:")
            print_connection_steps(cables)

if __name__ == "__main__":
    test_cable_connection()
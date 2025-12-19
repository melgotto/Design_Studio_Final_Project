import time
import requests
import statistics

BASE_URL = "http://127.0.0.1:8000"
ITERATIONS = 10


def measure_request_time(endpoint, method='GET', data=None):
    """
    Вимірює час виконання одного запиту.
    Повертає час у мілісекундах (мс).
    """
    url = f"{BASE_URL}{endpoint}"
    start_time = time.time()

    try:
        if method == 'GET':
            headers = {'User-Agent': 'PerformanceTest/1.0'}
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, data=data)

        # Примусово зчитуємо контент, щоб врахувати час завантаження тіла відповіді
        _ = response.content

        # Перевірка на помилки
        if response.status_code != 200:
            print(f"\n[Увага] Отримано статус {response.status_code} для {url}")

    except requests.exceptions.RequestException as e:
        print(f"\nПомилка з'єднання з {url}: {e}")
        return None

    end_time = time.time()
    return (end_time - start_time) * 1000  # Переводимо в мс


def run_performance_test():
    print(f"--- Запуск тестування продуктивності ({ITERATIONS} ітерацій) ---\n")
    print(f"Цільовий сервер: {BASE_URL}\n")

    scenarios = [
        # 1. Головна сторінка
        {"name": "Головна сторінка", "endpoint": "/dashboard/", "method": "GET"},

        # 2. Сторінка входу
        {"name": "Сторінка входу", "endpoint": "/accounts/login/", "method": "GET"},

        # 3. Пошук референсів
        {"name": "Пошук референсів", "endpoint": "/references/?query=nature&color=any&orientation=any",
         "method": "GET"},

        # 4. Генерація ідей
        {"name": "Генерація ідей", "endpoint": "/ideas/generate/", "method": "GET"},

        # 5. Сторінка тестів
        {"name": "Список тестів", "endpoint": "/tests/", "method": "GET"},

        # 6. Спільнота
        {"name": "Спільнота", "endpoint": "/community/", "method": "GET"},
    ]

    results_table = []

    for scenario in scenarios:
        print(f"Тестування сценарію: {scenario['name']}...", end="", flush=True)
        times = []

        for _ in range(ITERATIONS):
            t = measure_request_time(scenario['endpoint'], scenario['method'])
            if t is not None:
                times.append(t)
            # Невелика пауза між запитами
            time.sleep(0.1)

        if times:
            avg_time = statistics.mean(times)
            min_time = min(times)
            max_time = max(times)
            results_table.append((scenario['name'], avg_time, min_time, max_time))
            print(f" Готово. Середній: {avg_time:.2f} мс")
        else:
            print(" Помилка (всі запити провалилися).")

    # Вивід підсумкової таблиці
    print("\n" + "=" * 80)
    print(f"{'Сценарій':<35} | {'Середній (мс)':<15} | {'Мін.':<10} | {'Макс.':<10}")
    print("-" * 80)
    for row in results_table:
        print(f"{row[0]:<35} | {row[1]:<15.2f} | {row[2]:<10.2f} | {row[3]:<10.2f}")
    print("=" * 80)


if __name__ == "__main__":
    run_performance_test()
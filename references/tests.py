import time
import requests


def test_unsplash_speed():
    start_time = time.time()

    # Емуляція запиту до вашої функції пошуку або прямий запит до API
    response = requests.get("https://api.unsplash.com/search/photos?query=office&client_id=GeMMwNa2pVJU8FW6JEZBty9po9TBiiFq52B8ymgvgsA")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Час відповіді Unsplash API: {duration:.4f} секунд")


test_unsplash_speed()
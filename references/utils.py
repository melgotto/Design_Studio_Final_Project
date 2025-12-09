import requests
from django.conf import settings


def search_unsplash_images(query, color=None, orientation=None, page=1):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {settings.UNSPLASH_ACCESS_KEY}"
    }
    params = {
        "query": query,
        "page": page,
        "per_page": 12,  # Кількість фото на сторінку
    }

    # Додаємо фільтри, якщо вони обрані
    if color and color != 'any':
        params['color'] = color
    if orientation and orientation != 'any':
        params['orientation'] = orientation

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error connecting to Unsplash: {e}")
        return None
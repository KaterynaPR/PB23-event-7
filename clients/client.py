import requests

BASE_URL = 'http://127.0.0.1:5000'

# Search for books by author or title
def search_books(author=None, title=None):
    params = {}
    if author:
        params['author'] = author
    if title:
        params['title'] = title

    response = requests.get(f'{BASE_URL}/books', params=params)
    if response.status_code == 200:
        print("Books found:", response.json())
    else:
        print("Error:", response.json())

# rent books ID
def rent_book(book_id):
    data = {"id": book_id}
    response = requests.post(f'{BASE_URL}/rent', json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response.json())

if __name__ == '__main__':
    search_books(author="Jack London")
    rent_book(1)
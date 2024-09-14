from flask import Flask, request, jsonify
app = Flask(__name__)
books = [
    {"id": 1, "author": "Jack London", "title": "The Call of the Wild", "available": True},
    {"id": 2, "author": "Jack London", "title": "White Fang", "available": True},
    {"id": 3, "author": "Jack London", "title": "The Sea-Wolf", "available": False}  # takeing
]

@app.route('/books', methods=['GET'])
def get_books():
    author = request.args.get('author')
    title = request.args.get('title')
    result = [book for book in books if (author and book['author'] == author) or (title and book['title'] == title)]
    
    if not result:
        return jsonify({"message": "No books found"}), 404
    
    return jsonify(result), 200
@app.route('/rent', methods=['POST'])
def rent_book():
    data = request.get_json()
    book_id = data.get('id')
    
    for book in books:
        if book['id'] == book_id:
            if book['available']:
                book['available'] = False
                return jsonify({"message": "Book rented successfully"}), 200
            else:
                return jsonify({"message": "The book is already rented"}), 400

    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for books and members
books =  [
    {'id': 1, 'title': '1984', 'author': 'George Orwell', 'published': '1949-06-08'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'published': '1960-07-11'}
]
members = [
    {'id': 1, 'Dob': '1984', 'author': 'Munshi Prem Chandra', 'published': '1949-06-08'},
    {'id': 2, 'Dob': '1965', 'author': 'Rajkumar', 'published': '1960-07-11'}
]

# Book CRUD operations
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books}), 200 

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify({'message': 'Book added successfully', 'book': new_book}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book.update(request.json)
            return jsonify({'message': 'Book updated successfully', 'book': book}), 200
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully'}), 200

# Member CRUD operations
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify({'members': members}), 200

@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.json
    members.append(new_member)
    return jsonify({'message': 'Member added successfully', 'member': new_member}), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    for member in members:
        if member['id'] == member_id:
            return jsonify(member), 200
    return jsonify({'message': 'Member not found'}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    for member in members:
        if member['id'] == member_id:
            member.update(request.json)
            return jsonify({'message': 'Member updated successfully', 'member': member}), 200
    return jsonify({'message': 'Member not found'}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [member for member in members if member['id'] != member_id]
    return jsonify({'message': 'Member deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

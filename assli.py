from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# قاعدة بيانات مبدئية
books = []

# إضافة كتاب
@app.route('/books', methods=['POST'])
def add_book():
    """
    Add a new book
    ---
    parameters:
      - name: book
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Book Title"
            author:
              type: string
              example: "Author Name"
            published_year:
              type: integer
              example: 2022
            isbn:
              type: string
              example: "123456789"
    responses:
      201:
        description: Book added successfully
      400:
        description: Validation error
    """
    try:
        # الحصول على البيانات من الطلب
        book = request.json

        # التحقق من وجود الحقول المطلوبة
        required_fields = ('title', 'author', 'published_year', 'isbn')
        if not all(key in book for key in required_fields):
            return jsonify({"error": "Missing required fields: title, author, published_year, isbn"}), 400

        # التحقق من أن ISBN فريد
        if any(b['isbn'] == book['isbn'] for b in books):
            return jsonify({"error": "A book with this ISBN already exists"}), 400

        # إضافة الكتاب إلى قاعدة البيانات
        books.append(book)
        return jsonify({"message": "Book added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# عرض كل الكتب
@app.route('/books', methods=['GET'])
def list_books():
    """
    List all books
    ---
    responses:
      200:
        description: A list of all books
    """
    return jsonify(books), 200

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)

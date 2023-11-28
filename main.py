from flask import Flask, jsonify, request
import json

app = Flask(__name__)
f = open('books.json')
data = json.load(f)
data = data['books']
f.close()


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


# Zadanie 0.3
@app.route("/titles")
def titles_all():
    titles_tab = [book['title'] for book in data]
    return json.dumps(titles_tab)


# Zadanie 0.4
@app.route('/titles/<isbn>', methods=['GET'])
def titles_isbn(isbn):
    for book in data:
        if isbn == book['isbn']:
            return book
    resp = jsonify({'status': 404, 'message': f'Not Found {isbn}'})
    resp.status_code = 404
    return resp


# Zadanie 0.5
@app.route('/descriptions/<expression>', methods=['GET'])
def descriptions(expression):
    des = []
    for book in data:
        if expression in book['description']:
            des.append(book['description'])
    return des


# Zadanie 0.6
@app.route('/titles/<isbn>', methods=['PUT'])
def titles_author(isbn):
    book_id = None
    for i in range(0, len(data)):
        if isbn == data[i]['isbn']:
            book_id = i
    resp = jsonify({'status': 404, 'message': 'Procedure has failed.'})
    resp.status_code = 404
    if book_id is not None:
        if 'author' in request.args:
            data[book_id]['author'] = request.args['author']
            resp = jsonify({'status': 200, 'message': 'Procedure has been successful.'})
            resp.status_code = 200
    return resp

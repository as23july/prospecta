from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = {
    "category1": [
        {"title": "Title 1", "description": "Description 1"},
        {"title": "Title 2", "description": "Description 2"}
    ],
    "category2": [
        {"title": "Title 3", "description": "Description 3"},
        {"title": "Title 4", "description": "Description 4"}
    ]
}

@app.route('/items', methods=['GET'])
def get_items():
    category = request.args.get('category')
    items = data.get(category, [])
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import ollama


app = Flask(__name__)

# Sample data
'''
items = [
    {"id": 1, "name": "Item 1", "price": 50},
    {"id": 2, "name": "Item 2", "price": 100},
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = items[-1]['id'] + 1 if items else 1
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    item.update(data)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return '', 204
'''
MODEL_NAME = "llama3"


@app.route('/ask-edbot', methods=['POST'])
def generate():
    data = request.json
    web_prompt = data.get('prompt', '')

    try:
        ai_response = ollama.generate(model=MODEL_NAME, prompt=web_prompt)
        return jsonify(ai_response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

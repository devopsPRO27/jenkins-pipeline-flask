from flask import Flask
from flask import request

app = Flask('zhai app')

foods = [{"id": 1, "name": "shawarma", "score": 6},
         {"id": 2, "name": "tofu", "score": 8},
         {"id": 3, "name": "araaees", "score": 10}]


@app.route('/foods', methods=['GET', 'DELETE'])
def get_foods():
    if request.method == 'DELETE':
        foods.clear()
    return foods


@app.route('/foods/<int:id>', methods=['GET', 'POST'])
def get_id(id):
    if request.method == 'GET':
        for food in foods:
            if food.get('id') == id:
                return food
    if request.method == 'POST':
        foods.append(request.get_json())
        return {"status": 'success'}
    return {}


app.run(host="0.0.0.0", port="5000")
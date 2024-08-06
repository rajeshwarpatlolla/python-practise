from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def test():
    return 'Flask API running..'


@app.route('/list', methods=['GET', 'POST', 'PUT', 'DELETE'])
def lists():
    # request.args.get('id')
    # To get the query parameter value from '/list?id=12'
    print(request, request.args.get('id'))
    if request.method == 'GET':
        return 'This is GET method of list'
    elif request.method == 'POST':
        return 'This is POST method of list'
    elif request.method == 'PUT':
        return 'This is PUT method of list'
    elif request.method == 'DELETE':
        return 'This is DELETE method of list'
    else:
        return 'No matching method found'


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def users(user_id):
    if request.method == 'GET':
        return 'This is GET method of users/<user_id>'
    elif request.method == 'PUT':
        return 'This is PUT method of users/<user_id>'
    elif request.method == 'DELETE':
        return 'This is DELETE method of users/<user_id>'
    else:
        return 'No matching method found'


if __name__ == '__main__':
    app.run(debug=True)

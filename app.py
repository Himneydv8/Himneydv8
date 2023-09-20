from flask import Flask, jsonify

app = Flask(__name__)

data = [
	{}
]

@app.route('/api/items', methods=['GET'])
def get_items():
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/youtube-seo-optimize', methods=['POST'])
def seo_optimize():
	data = json.loads(request.data)
	print(data)
	if data["url"]:
		return jsonify({"Message": "Welcome", "METHOD": "POST"})
	else:
		return jsonify({"ERROR": "Some Error"})

if __name__=="__main__":
	app.run(threaded=True, port=5000)

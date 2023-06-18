from flask import Blueprint, jsonify, request

# define the blueprint
youtube_api = Blueprint(name="youtube_api", import_name=__name__)


@youtube_api.route('', methods=['POST'])
def plus_x():
    data = request.get_json()
    output = {"msg": f"Your URL is: '{data['url']}'"}
    return jsonify(output)

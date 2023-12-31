"""Flask Application"""

# load libaries
from flask import Flask, jsonify
import sys

# load modules
from src.routes.youtube import youtube_api
from src.routes.swagger import swagger_ui_blueprint, SWAGGER_URL

# init Flask app
app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(youtube_api, url_prefix="/api/v1/youtube-seo-optimize")

from src.api_spec import spec

# register all swagger documented functions here

with app.test_request_context():
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)


@app.route("/api/swagger.json")
def create_swagger_spec():
    """
    Swagger API definition.
    """
    return jsonify(spec.to_dict())


app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

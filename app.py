from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from view import blueprint as stats

app = Flask(__name__)

app.config['API_TITLE'] = ''
app.config['API_VERSION'] = ''
app.config['OPENAPI_VERSION'] = '3.1.0'

api = Api(app)
api.register_blueprint(stats)

cors = CORS(app, resources={r'*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(debug=True)
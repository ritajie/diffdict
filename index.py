import json

from flask import Flask, render_template, request

from services import deal_dict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/diffdict', methods=['POST'])
def diffdict():
    ans = {
        "code": 200,
        "message": None,
        "data": {}
    }
    first_dict = request.json.get("first_json")
    second_dict = request.json.get("second_json")
    
    processed_first_dict, processed_second_dict = deal_dict.deal_dict(first_dict, second_dict)

    ans['data']['first_json'] = processed_first_dict
    ans['data']['second_json'] = processed_second_dict

    return json.dumps(ans)


if __name__ == "__main__":
    app.run(debug=True)

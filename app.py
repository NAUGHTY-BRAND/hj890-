from flask import Flask, request, jsonify
from meta_ai_api import MetaAI
app = Flask(__name__)

ai = MetaAI()

@app.route('/metaAi', methods=['GET'])
def meta_ai():
    prompt = request.args.get('prompt', '')

    if prompt:

        response = ai.prompt("hi there")
        return jsonify(response=response)
    else:
        return jsonify(error="No prompt provided"), 400

if __name__ == '__main__':
    app.run(host='localhost', port=3000)

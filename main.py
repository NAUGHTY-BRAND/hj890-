from flask import Flask, request, jsonify
from meta_ai_api import MetaAI

app = Flask(__name__)

# Initialize MetaAI
ai = MetaAI()

@app.route('/metaAi', methods=['GET'])
def meta_ai():
    # Get the prompt from the URL query parameter
    prompt = request.args.get('prompt', '')
    
    if prompt:
        # Get the response from MetaAI for the prompt
        response = ai.prompt(message=prompt)
        
        # Debug print to inspect the response
        print(response)
        
        # Check if the response is a list and handle it
        if isinstance(response, list):
            response = {"response": response}  # Example modification for list response
        
        return jsonify(response=response)
    else:
        return jsonify(error="No prompt provided"), 400

if __name__ == '__main__':
    app.run(host='localhost', port=3000)

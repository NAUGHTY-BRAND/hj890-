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
        
        # Debug print to inspect the response type and content
        print("Response from MetaAI:", response)
        
        # Check if response contains 'message' indicating login/authentication issue
        if isinstance(response, dict) and 'message' in response:
            if 'Please log in to generate images' in response['message']:
                return jsonify(error="Authentication required. Please log in to generate images.")
        
        # Check if response is a list or a dictionary and handle accordingly
        if isinstance(response, list):
            # If it's a list, return it directly as a list under a key
            return jsonify(response={"data": response})
        elif isinstance(response, dict):
            # If it's a dictionary, return it as is
            return jsonify(response=response)
        else:
            # If it's neither a list nor a dictionary, return as a generic response
            return jsonify(response={"message": str(response)})
    else:
        return jsonify(error="No prompt provided"), 400

if __name__ == '__main__':
    app.run(host='localhost', port=3000)

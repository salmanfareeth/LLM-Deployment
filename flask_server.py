import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS for all domains
CORS(app)

# Route to trigger the Ollama model command
@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']
    
    # Construct the command to run Ollama locally
    command = f'echo "{input_text}" | ollama run deepseek-r1'
    
    try:
        # Run the command in the background using subprocess.Popen
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # Check if the command was successful and return the output
        if process.returncode == 0:
            model_output = stdout.strip()  # Get the output from the command
            return jsonify({'result': model_output})
        else:
            return jsonify({'result': f'Error: {stderr.strip()}'})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'})

# Optional route if you want to serve a page at the root URL (can be removed)
@app.route('/')
def index():
    return 'Flask Server is running!'

# Start the Flask server in a separate thread
def run_flask():
        app.run(debug=True, host="0.0.0.0", port=8000, use_reloader=False)

# Start Flask in a background thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

from flask import Flask, render_template, request, jsonify
from threading import Thread
import FyersWebSocket as Fskt
import os 
app = Flask(__name__)

# This will keep track of whether the WebSocket should be running.
websocket_running = False

def start_websocket():
    global websocket_running
    websocket_running = True
    Fskt.main()

@app.route('/')
def index():
    os.environ.get('access_token')
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    if not websocket_running:
        thread = Thread(target=start_websocket)
        thread.start()
    return jsonify({'message': 'WebSocket started'})

@app.route('/stop', methods=['POST'])
def stop():

    Fskt.stop_websocket() # Example, adjust according to your implementation
 

@app.route('/get-messages', methods=['GET'])
def get_messages():
    # Implement logic to fetch and return messages stored by FyersWebSocket.py
    return jsonify({'messages': Fskt.get_messages()})  # Example, adjust accordingly

if __name__ == '__main__':
    app.run(debug=True)

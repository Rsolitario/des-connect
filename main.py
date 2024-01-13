from flask import Flask, render_template, request

import formateador as FD

app = Flask(__name__, static_folder='static')

@app.route('/')
def chat():
    return render_template('chat-modelo.html')

@app.route("/send_message", methods=['POST'])
def send_message():
    message = request.form['message']
    print(message)
    response = FD.respuesta(message)
    print(response)
    return response

if '__main__' == __name__:
    app.run(debug=True)
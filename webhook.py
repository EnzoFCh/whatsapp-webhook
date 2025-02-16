import os
from flask import Flask, request

app = Flask(name)

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == "miwebhook123":
        return challenge
    return "Error de verificación", 403

@app.route('/', methods=['GET'])
def home():
    return "El servidor está funcionando correctamente."

if name == 'main':
    port = int(os.environ.get("PORT", 10000))  # Render usa puertos dinámicos
    app.run(host="0.0.0.0", port=port)

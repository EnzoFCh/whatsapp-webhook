from flask import Flask, request

app = Flask(name)

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == "miwebhook123":  # Debe coincidir con lo que pongas en Meta
        return challenge
    return "Error de verificación", 403

if name == 'main':
    app.run(port=5000)

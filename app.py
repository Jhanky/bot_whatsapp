from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Obtener el cuerpo del mensaje
    incoming_msg = request.values.get('Body', '')

    # Crear una respuesta
    resp = MessagingResponse()
    msg = resp.message()

    # Procesar el mensaje recibido
    if incoming_msg.lower() == 'hola':
        msg.body("¡Hola! ¿En qué puedo ayudarte?")
    else:
        msg.body("Hola, soy un bot y solo respondo a 'hola'. ¡Intenta decirme 'hola'!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

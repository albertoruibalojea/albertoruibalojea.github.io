from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Configurar la clave API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No se envió un mensaje válido."}), 400

        # Llamada a OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente especializado en enfermedades inflamatorias intestinales (EIIs). Proporciona información precisa y basada en evidencia médica."},
                {"role": "user", "content": user_message},
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        # Manejar cualquier error genérico
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

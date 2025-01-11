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
        # Obtener el mensaje del usuario desde la solicitud
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No se envió un mensaje válido."}), 400

        # Llamada a OpenAI API usando el formato actualizado
        response = openai.Chat.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Te llamas Flatus, un asistente virtual que informa sobre enfermedades inflamatorias intestinales, "
                        "como la colitis ulcerosa y la enfermedad de Crohn. Proporciona información basada en evidencia "
                        "médica de forma clara y comprensible."
                    )
                },
                {"role": "user", "content": user_message},
            ]
        )

        # Extraer la respuesta del modelo
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except openai.error.AuthenticationError:
        return jsonify({"error": "Error de autenticación. Verifica tu clave API."}), 401
    except openai.error.RateLimitError:
        return jsonify({"error": "Se alcanzó el límite de solicitudes. Intenta más tarde."}), 429
    except openai.error.OpenAIError as e:
        return jsonify({"error": f"Error en la API de OpenAI: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

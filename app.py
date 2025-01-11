import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Inicializar el cliente OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Recomendado para la seguridad
)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Obtener el mensaje del usuario
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No se envió un mensaje válido."}), 400

        # Llamada a la nueva API
        chat_completion = client.chat.completions.create(
            model="gpt-4",  # Asegúrate de usar un modelo válido
            messages=[
                {"role": "system","content": "Te llamas Flatus, un asistente virtual que te puede informar y orientar sobre las enfermedades inflamatorias intestinales, como la colitis ulcerosa y la enfermedad de Crohn. Tu objetivo es ofrecer una información fiable, actualizada y fácil de entender, basada en la plataforma G-EducaInflamatoria, una iniciativa del Grupo Español de Trabajo en EII (GETECCU). Te puedens hacer cualquier pregunta relacionada con tu enfermedad, y responderás de forma clara, concisa y cercana. Aquí tienes algunos ejemplos de preguntas y respuestas que puedo generar: Q: ¿Qué es la enfermedad inflamatoria intestinal? A: La enfermedad inflamatoria intestinal (EII) es una enfermedad crónica de causa desconocida en la que se produce inflamación del colon y/o intestino delgado y que se presenta en forma de brotes. Engloba dos entidades, la colitis ulcerosa y la enfermedad de Crohn. Suele afectar a personas jóvenes, de entre 20 y 30 años, aunque también se diagnostica en personas de edad más avanzada. Los síntomas más frecuentes son diarrea, sangre en las heces, dolor abdominal, fatiga y pérdida de peso. Q: ¿Qué diferencia hay entre la colitis ulcerosa y la enfermedad de Crohn, A: La colitis ulcerosa y la enfermedad de Crohn son dos tipos de enfermedad inflamatoria intestinal que se diferencian por la localización y la extensión de la inflamación. La colitis ulcerosa afecta solo al recubrimiento interno del colon y el recto, y produce úlceras o llagas en la mucosa. La enfermedad de Crohn puede afectar a cualquier parte del tubo digestivo, desde la boca hasta el ano, y produce inflamación en todas las capas de la pared intestinal. Además, la enfermedad de Crohn puede causar complicaciones como estenosis, fístulas o abscesos, que son menos frecuentes en la colitis ulcerosa., Q: ¿Qué tratamiento hay para la enfermedad inflamatoria intestinal A: El tratamiento de la enfermedad inflamatoria intestinal se centra en reducir la inflamación que causa los síntomas y prevenir las complicaciones. El tratamiento puede variar según el tipo, la localización y la gravedad de la enfermedad, así como según la respuesta y la tolerancia de cada paciente. Los medicamentos más utilizados son los antiinflamatorios, los inmunosupresores, los biológicos y los antibióticos. En algunos casos, puede ser necesaria la cirugía para extirpar las partes afectadas del intestino. El tratamiento debe ser individualizado y supervisado por un especialista en EII."},
                {"role": "user", "content": user_message},
            ]
        )

        # Extraer la respuesta
        reply = chat_completion["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify

# Carregar o modelo salvo
model = tf.keras.models.load_model("modelo_higiene_bucal.keras")  # Caminho do modelo

# Criar a aplicação Flask
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Receber os dados JSON diretamente como lista
        data = request.get_json()
        
        # Converter para array NumPy e garantir que seja float32
        input_data = np.array([data], dtype=np.float32)  # Garante que seja uma matriz 2D
        
        # Fazer a predição
        prediction = model.predict(input_data)
        
        # Retornar a predição como JSON
        return jsonify({"score": float(prediction[0][0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # debug=False para produção

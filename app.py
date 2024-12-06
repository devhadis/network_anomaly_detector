from flask import Flask, render_template, request
from utils.preprocess import preprocess_data
from utils.detect import detect_anomaly
import joblib

# Configuração do Flask
app = Flask(__name__)

# Carregar modelo de machine learning
MODEL_PATH = 'model/isolation_forest.pkl'
model = joblib.load(MODEL_PATH)

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para resultados
@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        # Coletar dados do formulário
        data = {
            'src_ip': request.form['src_ip'],
            'dst_ip': request.form['dst_ip'],
            'protocol': int(request.form['protocol']),
            'packet_length': int(request.form['packet_length']),
        }

        # Pré-processar dados
        features = preprocess_data(data)

        # Detectar anomalia
        result, details = detect_anomaly(model, features)

        return render_template('results.html', result=result, details=details)

if __name__ == '__main__':
    app.run(debug=True)

from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib

# Dados simulados
data = pd.DataFrame({
    'protocol': [1, 2, 1, 3, 1],
    'packet_length': [400, 500, 100, 600, 200]
})

# Treinar o modelo
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

# Salvar o modelo no caminho correto
joblib.dump(model, 'model/isolation_forest.pkl')
print("Modelo salvo em: model/isolation_forest.pkl")

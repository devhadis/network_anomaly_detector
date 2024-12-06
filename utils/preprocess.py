import pandas as pd

def preprocess_data(data):
    # Convertendo os dados em DataFrame
    df = pd.DataFrame([data])
    # Normalização
    df['packet_length'] = df['packet_length'] / 1500  # Normalizar o tamanho do pacote
    return df[['protocol', 'packet_length']].values

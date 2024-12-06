def detect_anomaly(model, features):
    prediction = model.predict(features)
    is_anomaly = prediction[0] == -1
    details = 'Desvio significativo detectado.' if is_anomaly else 'Tráfego normal.'
    return is_anomaly, details

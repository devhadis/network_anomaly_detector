# **Documentação do Projeto: Detector de Anomalias de Rede**

Este projeto é uma aplicação web construída com Flask que utiliza aprendizado de máquina para detectar anomalias no tráfego de rede, como possíveis ataques ou comportamentos suspeitos. A aplicação permite que o usuário insira informações sobre pacotes de rede e retorna se há uma anomalia baseada em um modelo treinado de machine learning.

---

## **Estrutura do Projeto**

```
network_anomaly_detector/
├── app.py                   # Aplicação principal Flask
├── train_model.py           # Script para treinar e salvar o modelo
├── requirements.txt         # Dependências do projeto
├── static/                  # Arquivos estáticos (CSS)
│   └── style.css
├── templates/               # Templates HTML
│   ├── base.html            # Layout base
│   ├── index.html           # Página inicial com formulário
│   └── results.html         # Página de resultados
├── utils/                   # Funções auxiliares
│   ├── preprocess.py        # Pré-processamento de dados
│   └── detect.py            # Detecção de anomalias
└── model/                   # Diretório do modelo treinado
    └── isolation_forest.pkl # Modelo treinado
```

---

## **Pré-requisitos**

Antes de começar, certifique-se de ter os seguintes itens instalados no seu sistema:

- **Python 3.7 ou superior**
- **Pip** (gerenciador de pacotes do Python)
- Um navegador web (para acessar a aplicação)

---

## **Configuração do Ambiente**

### **1. Clone o Repositório**
Baixe o projeto em seu sistema:
```bash
git clone https://github.com/seu-repositorio/network-anomaly-detector.git
cd network-anomaly-detector
```

### **2. Crie e Ative um Ambiente Virtual**
Configure um ambiente virtual para isolar as dependências do projeto:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### **3. Instale as Dependências**
Use o arquivo `requirements.txt` para instalar todas as dependências necessárias:
```bash
pip install -r requirements.txt
```

---

## **Como Usar**

### **1. Treinar o Modelo de Machine Learning**
Antes de rodar a aplicação, treine e salve o modelo:
```bash
python3 train_model.py
```
O modelo será salvo no diretório `model/` como `isolation_forest.pkl`.

---

### **2. Executar a Aplicação Flask**
Inicie o servidor Flask com o seguinte comando:
```bash
python3 app.py
```
Após iniciar, o servidor estará disponível no endereço:
```
http://127.0.0.1:5000/
```

---

### **3. Interagir com a Aplicação**

1. **Acesse a página inicial** no navegador:  
   ```
   http://127.0.0.1:5000/
   ```

2. **Preencha os campos do formulário**:
   - **IP de Origem**: Exemplo: `192.168.1.1`
   - **IP de Destino**: Exemplo: `192.168.1.100`
   - **Protocolo**: Número inteiro representando o protocolo (exemplo: `1` para ICMP, `6` para TCP, `17` para UDP).
   - **Tamanho do Pacote**: Exemplo: `500`.

3. **Clique em "Enviar"** para submeter os dados.

4. **Veja o Resultado**: A aplicação exibirá se o tráfego é normal ou anômalo.

---

## **Exemplo de Uso**

### **Exemplo 1: Tráfego Normal**
- **Entrada do Usuário**:
  - IP de Origem: `192.168.1.1`
  - IP de Destino: `192.168.1.2`
  - Protocolo: `6`
  - Tamanho do Pacote: `200`
  
- **Saída**:
  ```
  Status: Tráfego Normal
  Detalhes: O tráfego segue padrões esperados.
  ```

### **Exemplo 2: Tráfego Anômalo**
- **Entrada do Usuário**:
  - IP de Origem: `10.0.0.1`
  - IP de Destino: `10.0.0.255`
  - Protocolo: `17`
  - Tamanho do Pacote: `1500`
  
- **Saída**:
  ```
  Status: Anomalia Detectada
  Detalhes: Desvio significativo detectado.
  ```

---

## **Detalhes Técnicos**

### **1. Modelo de Machine Learning**
- **Algoritmo**: Isolation Forest
- **Bibliotecas**: `scikit-learn`, `joblib`
- **Treinamento**:
  - Baseado em dados simulados de tráfego de rede.
  - Detecta desvios no padrão de tráfego normal.

### **2. Estrutura do Flask**
- **Rota `/`**:
  - Página inicial com formulário para entrada de dados.
- **Rota `/results`**:
  - Processa os dados enviados e retorna o resultado da detecção.

---

## **Personalização**

1. **Treinamento com Dados Reais**:
   - Substitua os dados simulados no `train_model.py` pelos seus próprios dados de tráfego de rede.
   - Re-treine o modelo para melhorar a precisão.

2. **Estilo da Interface**:
   - Edite o arquivo `static/style.css` para personalizar a aparência da aplicação.

3. **Log de Resultados**:
   - Adicione lógica para salvar os resultados em um banco de dados, como SQLite ou PostgreSQL.

---

## **Dicas para Produção**

1. **Servidor de Produção**:
   - Use um gerenciador como **Gunicorn** para rodar o Flask:
     ```bash
     pip install gunicorn
     gunicorn app:app
     ```

2. **Proxy Reverso**:
   - Configure um proxy reverso com **Nginx** ou **Apache** para gerenciar o tráfego e habilitar HTTPS.

3. **Segurança**:
   - Valide as entradas do usuário para evitar ataques (ex.: injeção de código malicioso).

---

## **Solução de Problemas**

### **Erro: `ModuleNotFoundError: No module named 'flask'`**
Certifique-se de que o ambiente virtual está ativado e instale as dependências:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### **Erro: `KeyError: 102` ao carregar o modelo**
Recrie o modelo com o script `train_model.py` no mesmo ambiente onde será usado:
```bash
python3 train_model.py
```

---


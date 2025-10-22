# Intent Classifier
Um classificador de intenções treinável com diferentes conjuntos de dados e configurações.
## Instalação
```bash
conda create -n intent-clf python=3.11
conda activate intent-clf
pip install -r requirements.txt
```
## Treinamento
### Treinar modelo Confusion
```bash
python intent_classifier.py train \
    --examples_file="data/confusion_intents.yml" \
    --config="models/confusion-v1_config.yml" \
    --save_model="models/confusion-v1.keras"
```
### Treinar modelo Clair
```bash
python intent_classifier.py train \
    --examples_file="data/clair_intents.yml" \
    --config="models/clair-v1_config.yml" \
    --save_model="models/clair-v1.keras"
```
## Em `models/`:
    * Novo arquivo `.yml` para o dataset Clair
    * Ajuste de hiperparâmetros
    * * Regularizações `L1` e `L2`
    * * `validation_split`
## Em `app.py`:
    * Variável global `MODELOS`
    * Endpoints adicionados:
    * * `/predict` que prediz usando todos os modelos
    * * `/confusion` que prediz usando somente o modelo Confusion
    * * `/clair` que prediz usando somente o modelo Clair

## Testando as rotas
Após treinar os modelos, execute dentro da pasta `intent-classifier`:
```bash
    python app.py
```
Em seguida acesse no navegador: http://localhost:8000/docs

No Swagger UI:
1. Selecione um dos 3 endpoints POST disponíveis.

2. Clique em “Try it out”.

3. Altere a string dentro do corpo da requisição.

4. Clique em “Execute”.

5. Observe os resultados no corpo da resposta.
* * A intenção predita pode variar dependendo do modelo utilizado.
# intent-classifier

Como instalar:
```
conda create -n intent-clf python=3.11
conda activate intent-clf
pip install -r requirements.txt
```

Como treinar:
```
python intent_classifier.py train \
    --examples_file="data/confusion_intents.yml" \
    --config="models/confusion-v1_config.yml" \
    --save_model="models/confusion-v1.keras"

python intent_classifier.py train \
    --examples_file="data/clair_intents.yml" \
    --config="models/clair-v1_config.yml" \
    --save_model="models/clair-v1.keras"
```


O que tem de novo:
    ===========================================================================================
    Em models:
        novo .yml em models para o dataset clair
        os hiperparâmetros que mudei foram as regularizações l1 e l2 e o validation_split

    Em app.py:
        variável global MODELOS
        endpoint para predizer com todos os modelos
        endpoint para predizer somente com confusion
        endpoint para predizer somente com clair
    ===========================================================================================
    Para testar as rotas, após treinar os modelos, dentro da pasta intent-classifier, rode o comando no terminal:
    ```
        python app.py
    ```
    Após isso acesse no navegador: http://localhost:8000/docs

    Em seguida, clique em um dos 3 endpoints POSTs.
    Clique em "Try it out".
    Mude a String dentro do corpo da requisição.
    E finalmente, execute e analise os resultados no corpo da resposta.

    Dependendo do modelo, a intenção predita vai variar.
    ===========================================================================================
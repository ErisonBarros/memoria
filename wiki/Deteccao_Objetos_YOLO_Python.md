---
title: Detecção de Objetos Usando YOLO e Python
date: 2026-05-17
tags: [yolo, python, roboflow, colab, mAP]
sources: [raw/Detecção de Objetos Usando YOLO e Python.md]
---

# Detecção de Objetos Usando YOLO e Python

**Fonte:** [Leonardo Frugal - Oficina Python (YouTube)](https://www.youtube.com/watch?v=xQa6-a-HuvQ)

Este documento sumariza a criação e o treinamento de um modelo YOLO focado em detectar roupas e equipamentos de segurança em canteiros de obras.

## Conceitos Chaves do YOLO
- **Passada Única**: Usa camadas convolucionais para extrair características da imagem em uma única leitura.
- **Localização e Classificação**: O modelo prevê a localização (caixa delimitadora) e a classe do objeto.
- **Métricas de Precisão**:
  - **Matriz de Confusão**: Avalia Verdadeiros Positivos, Falsos Positivos, Falsos Negativos e Verdadeiros Negativos.
  - **Precisão**: Positivos reais em relação ao total de previsões positivas.
  - **Recall**: Positivos reais em relação a todos os positivos verdadeiros.
  - **mAP (mean Average Precision)**: A média de todas as previsões.

## Workflow de Treinamento
1. **Aquisição de Dados**: Utiliza-se o **Roboflow** para obter datasets prontos (ex: `construction site Safety` com 10 classes de objetos como capacetes, máscaras, etc.).
2. **Ambiente de Treinamento**: Executado no **Google Colab** utilizando aceleradores T4 GPU.
3. **Setup**:
   - Conectar o Google Drive ao Colab para facilitar o acesso aos dados.
   - Instalar a biblioteca `ultralytics`.
   - Modificar o arquivo `.yaml` de configuração de dados apontando o caminho do dataset.
4. **Treinamento**: Executa-se o treinamento (ex: 50 épocas, resolução 640px). O resultado é salvo em um arquivo de pesos, geralmente `best.pt`.
5. **Inferência (Detecção)**: Usa-se o modelo gerado, carregado no Python (via VS Code, por exemplo) para rodar o reconhecimento em vídeos ou imagens, filtrando os resultados baseados no nível de confiança.

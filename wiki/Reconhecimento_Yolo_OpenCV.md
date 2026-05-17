---
title: Reconhecimento de objetos com YOLO e OpenCV
date: 2026-05-17
tags: [yolo, opencv, python, ultralytics, deteccao]
sources: [raw/Reconhecimento de objectos com Yolo e OpenCV - AranaCorp.md]
---

# Reconhecimento de objetos com YOLO e OpenCV

**Fonte:** AranaCorp

Guia prático para a detecção de objetos em Python utilizando OpenCV, `imutils` e a biblioteca `ultralytics` (com foco nos modelos pré-treinados YOLOv8 ou YOLOv5).

## Dependências
- `python3 -m pip install imutils opencv-python ultralytics`

## Componentes Chaves da Aplicação

1. **Captura de Vídeo/Imagem**: 
   - Utilização do `imutils.video.VideoStream` para webcams nativas ou câmeras Raspberry Pi.
   - Utilização do `cv2.VideoCapture` para acessar arquivos MP4 ou streams RTSP de câmeras IP.

2. **Carregamento do Modelo**:
   - `model = YOLO("yolov8n.pt")` carrega o modelo YOLOv8 versão *nano* (rápido e leve). A arquitetura é capaz de baixar automaticamente os pesos caso não existam localmente.

3. **Loop de Processamento Contínuo**:
   - A imagem (frame) é passada para o modelo: `detections = model(frame)[0]`.
   - O objeto de detecção retorna propriedades como as coordenadas da caixa (`box.data`), a classe inferida (`box.cls.item()`) e a pontuação de confiança.

4. **Filtragem e Renderização (OpenCV)**:
   - Utiliza-se um threshold condicional (`CONFIDENCE_THRESHOLD = 0.8`) para descartar falsos positivos.
   - O OpenCV (`cv2.rectangle` e `cv2.putText`) é empregado para desenhar o retângulo sobre a detecção, incluindo uma *label* de texto contendo o nome da classe e a porcentagem de probabilidade.

5. **Exibição e Controle de Desempenho**:
   - O tempo gasto na inferência é medido (subtraindo o timestamp de final do inicial) para calcular e exibir os Quadros Por Segundo (FPS).
   - `cv2.imshow` exibe o resultado para o usuário.

O tutorial conclui demonstrando a flexibilidade do script, podendo ser trocada facilmente a fonte da imagem para analisar desde fotografias estáticas a monitoramentos de câmeras de segurança ao vivo.

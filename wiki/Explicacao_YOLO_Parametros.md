---
title: Explicação dos Parâmetros do YOLO
date: 2026-05-17
tags: [yolo, parametros, nms, iou, conf_threshold]
sources: [raw/Explicação.md]
---

# Explicação dos Parâmetros do YOLO

Este documento resume a função de execução de detecção do YOLO e seus parâmetros fundamentais.

## Função Base
A operação principal de detecção foca em identificar elementos em uma imagem usando uma Rede Neural Convolucional (CNN) de passada única (You Only Look Once). A função hipotética `run_yolo_on_tile` recebe uma imagem e parâmetros de configuração.

## Parâmetros Principais
- **`model`**: O modelo de Inteligência Artificial YOLO carregado e pronto para inferência.
- **`image`**: A imagem de entrada ou recorte ("azulejo") onde a busca será feita.
- **`conf_threshold`** (Limiar de Confiança): Define a certeza mínima para aceitar uma *bounding box*. Por exemplo, `0.30` ignora detecções com menos de 30% de confiança.
- **`imgsz`**: O tamanho da grade para o qual a imagem será redimensionada antes do processamento (ex: 736 pixels).
- **`iou_threshold`** (Intersection over Union): O limite de sobreposição entre duas caixas. É usado pela **Non-Maximum Suppression (NMS)** para remover caixas redundantes sobre o mesmo objeto. Se a sobreposição for maior que o limite (ex: 0.45), a caixa com menor confiança é descartada.

## Retorno
A inferência devolve uma lista de detecções, cada uma contendo:
- **Coordenadas espaciais** (da caixa delimitadora).
- **Classe identificada** (o tipo de objeto).
- **Pontuação de confiança**.

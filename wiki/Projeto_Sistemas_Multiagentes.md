---
title: Projeto de Sistemas Multiagentes
date: 2026-05-17
tags: [sistemas-multiagentes, crewai, gemini, ultralytics, rastreamento]
sources: [raw/Projeto de Sistemas Multiagentes _ Geração de relatório a partir de Dados de rastreamento..md]
---

# Projeto de Sistemas Multiagentes e Relatórios de Rastreamento

**Fonte:** [Matheus Carne (YouTube)](https://www.youtube.com/watch?v=hsH1c8j9AWQ)

Este projeto integra rastreamento visual usando YOLO e geração de relatórios utilizando Sistemas Multiagentes (via CrewAI) e Modelos de Linguagem Grande (Gemini).

## Visão Geral do Sistema
O objetivo inicial era construir uma arquitetura com múltiplos agentes autônomos:
1. **Agente de Rastreamento**: Responsável por utilizar o YOLO (Ultralytics) como uma ferramenta para extrair dados (velocidade, pose, entrada/saída de pessoas em zonas de interesse).
2. **Agente de Análise**: Para interpretar os dados visuais profundos.
3. **Agente de Relatório**: Para gerar resumos e insights em linguagem natural com base na análise.

## Desafios e Pivôs
- Houve dificuldade técnica em permitir que os agentes chamassem diretamente o modelo de visão computacional como uma "ferramenta".
- O modelo de rastreamento original (focado em dados complexos, como poses e velocidades) apresentou problemas de estabilidade e foi trocado por uma versão mais simples que apenas faz contagem básica de fluxo de pessoas.
- O resultado prático limitou-se ao **Agente de Relatório** recebendo um `txt` pré-processado com os dados de entrada/saída de pessoas da zona delimitada.

## Tecnologias Usadas
- **Visão Computacional**: `ultralytics` para aplicar a detecção e delimitar áreas de interesse em vídeos.
- **LLM e Orquestração**: A API do **Google Gemini** para a inteligência generativa e o **CrewAI** para orquestrar os agentes.

## Considerações Finais do Autor
O autor ressalta que se o sistema utilizasse modelos de visão mais densos (como o YOLO-Pose), o relatório gerado pela IA seria substancialmente mais rico, incluindo análises preditivas, pico de movimentações diárias, comportamento anômalo e até gráficos detalhados.

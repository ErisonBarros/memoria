---
sourceFile: "Explicação"
exportedBy: "Kortex"
exportDate: "2026-05-17T22:54:33.772Z"
---

# Explicação

ebfda6c1-6776-48ed-b7e5-476636dbd001

f9b15e1a-b4e5-4394-b1db-e40a6ccfdbdc

run\_yolo\_on\_tile

executa um modelo de detecção de objetos YOLO (

You Only Look Once

) para identificar elementos numa imagem. Embora os tipos de dados específicos

façam parte do seu código externo (estas estruturas exatas não são detalhadas nas fontes fornecidas, sendo uma tipagem do Python), os parâmetros da função baseiam-se em conceitos fundamentais do funcionamento do YOLO.

#### Abaixo está a explicação detalhada de cada argumento e o seu papel no modelo:

model: YOLO

: É o modelo de Inteligência Artificial carregado e pronto para realizar as inferências. O YOLO utiliza uma rede neural convolucional de passada única para detecção rápida e precisa.

: Representa a imagem de entrada (ou um "azulejo"/recorte específico da imagem maior) na qual o modelo vai procurar os objetos.

conf\_threshold: float = 0.30

limiar de confiança

. Este parâmetro define a confiança mínima para aceitar uma

bounding box

(caixa delimitadora). Em cada detecção, o YOLO calcula uma probabilidade (entre 0 e 1) que reflete a sua certeza sobre a presença e a classificação do objeto. O valor

significa que qualquer detecção em que o modelo tenha menos de 30% de certeza será descartada.

imgsz: int = 736

tamanho da imagem de entrada

. Antes de passar pela rede neural, a imagem (

) é redimensionada ou processada para uma grade correspondente a este tamanho de 736 pixels.

iou\_threshold: float = 0.45

: Representa o limite da métrica

Intersection over Union

(Interseção sobre União - IoU), que mede a área de sobreposição entre duas caixas. Este valor é utilizado num processo fundamental chamado

Non-Maximum Suppression (NMS)

. Como os modelos YOLO costumam prever múltiplas caixas delimitadoras redundantes ao redor do mesmo objeto, o algoritmo NMS compara as caixas; se duas caixas se sobrepõem numa proporção de 45% (

a caixa com a menor confiança é removida

, garantindo que sobra apenas a detecção mais precisa.

-&gt; List\[Detection\]

: O retorno da função. As inferências processadas por um modelo YOLO entregam tipicamente uma lista contendo as

coordenadas espaciais

da caixa delimitadora (ponto superior esquerdo e inferior direito, ou centro mais largura e altura), a

classe identificada

do objeto e a sua respectiva

pontuação de confiança

. Esses dados serão encapsulados na sua lista de instâncias


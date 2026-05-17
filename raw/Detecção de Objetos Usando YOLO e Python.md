---
sourceFile: "Detecção de Objetos Usando YOLO e Python"
exportedBy: "Kortex"
exportDate: "2026-05-17T22:54:33.771Z"
---

# Detecção de Objetos Usando YOLO e Python

055ca282-0c88-49be-ba43-d59902765ff0

Detecção de Objetos Usando YOLO e Python

c6428878-b762-4e00-9def-16de44afe9e8

https://www.youtube.com/watch?v=xQa6-a-HuvQ

xQa6-a-HuvQ

Leonardo Frugal - Oficina Python

que Inteligência Artificial foi o assunto de 2023 isso já tá todo mundo cansado de saber e que Python foi a grande responsável por quase todas as inteligências artificiais que existem isso também não é novidade nenhuma mas eu tô aqui para trazer um assunto que pouca gente sabe E que no Brasil tem pouquíssimas pessoas falando que é o yolo que é uma biblioteca do Python usada para Inteligência Artificial pra detecção de imagens e movimento essas coisas bom eu trouxe aqui ume

lista para falar sobre Iolo explicar tudo sobre io e até trazer código sobre então se você já gostou do assunto deixa aqui o seu comentário positivo indicando outros assuntos pra gente poder trazer e também já deixa aqui sua curtida que ajuda muito beleza bom sem mais delongas vamos pra tela F no vídeo de hoje eu vou est te Como criar o modelo de Inteligência Artificial que detecta objeto especificamente detecta roupas de segurança para isso a gente vai usar uma

ferramenta super poderosa do Python que é o yolo o yolo ele utiliza um método de detecção de passada única que usa ali de ras convolucionais para poder extrair as características da imagem é por isso que ele tem esse nome né yol É umaa para look on é diferente de outros modelos de de detecção de objetos que tem que passar várias vezes na mesma imagem para poder fazer a detecção Como que o yolo funciona o

tem duas partes localização e a classificação a localização é determinada é determinada pela Caixa delimitadora delimitadora Como que o yolo funciona o yolo tem duas partes a localização e a classificação a localização é determinada pela caixa delimitadora a caixa delimitadora é esses retângulos que ficam

volta do objeto então por exemplo o modelo ele vai prever aonde é o melhor lugar para pô essa esse retângulo e e a precisão varia de zero a um sendo zero que o modelo leou completamente onde é que tá o objeto e um que ele acertou completamente Onde tá o objeto para medir a precisão o Iolo precisa de três coisas a matriz de confusão a precisão e

a matriz de confusão é bem simples de entender Imagine que a gente tem um objeto no caso um carro a gente quer prever se ele é um carro a gente quer classificar se ele é um carro ou não é um carro então por exemplo no primeiro quadrado o objeto é um carro e o modelo classificou como o carro então é o verdadeiro positivo o segundo quadrado é uma casa Porém ele classificou com o cavo então é um falso positivo

no terceiro quadrado o objeto é o carro porém o modelo classificou como não é carro porém Então isso é um falso negativo no último quadrado é uma casa e o modelo classificou como não é carro não é um verdadeiro negativ a precisão são os positivos reais do total de previsões positivas e o Recall é os positivos reais de todas as previsões não só das positivas das negativas também

e isso é o map que é o mean Average Precision é a média de todas as previsões agora que você já entendeu o que que é o Iolo a gente vai partir agora pra Construção do nosso modelo só que paraa gente poder construir nosso modelo a gente precisa de imagens para poder fazer o treinamento dele o melhor site para poder faz para poder pegar esses bancos de dados usis é o roboflow nesse caso

a gente vai pegar um banco de dados que é o construction site Safety eu não vou precisar fazer o download Porque eu já tenho esse banco de dados instalado mas você vai ter que fazer o download com o zip e depois que você fazer o download você vai descompactar depois que você descompactar você vai fazer uma coisa super importante você vai colocar a pasta dele dentro do seu drive especificamente dentro da sua pasta me drive

por quê Porque a gente vai e usar o Google colab para poder fazer o treinamento do do nosso modelo e a única coisa que você vai precisar fazer é vir aqui no n data no editor de texto no Google e aqui você vai passar

O pef que é o caminho do de todas as passas né o diretório nesse caso você vai pôr aqui e dois pontos barra drive barra my drive e a pasta da onde tá o banco de dados no meu caso eu botei aqui nessa pasta yol Curse e botei aqui a a pasta do construction Safety e isso é importante porque é assim que o modelo vai conseguir pegar as imagens para poder fazer o treinamento e o teste

aqui esse NC é o número de classes ou seja são 10 classes e o nome dessas classes é o hard Hat ou seja o capacete a máscara o não capacete o não Máscara o não roupa de segurança ou pessoa o cone de segurança a roupa de segurança e etc depois que você fez o

o download do do banco de dados colocou ele dentro da do seu Google Drive você vai vir aqui no google colab para poder fazer o treinamento do nosso modelo mas antes um negócio muito importante que vocês TM que fazer é ver aqui em ambiente de execução alterar o tipo de ambiente de execução e colocar em T4 GPU por qu Porque que a gente quer rodar todo o treinamento na GPU do da máquina do Google colab

para poder agilizar o processo Porque ele demora muito vocês vão ver aqui são 50 épocas de Treinamento então por exemplo a gente pode rodar esse códigozinho aqui para poder ver como é que é a GPU né Eu já rodei mas vou rodar de novo Então nesse caso como vocês podem ver né E agora vocês podem fazer o download da do do

biblioteca ultralytics que é onde tá o Iolo então a gente pode só simplesmente rodar e antes de fazer o treinamento a gente vai vir aqui e vai montar o nosso drive que é para ele poder pegar Nossa pasta com os bancos de dados

da agora que o drive foi montado a gente pode mudar esse essa linha de código que é o que a gente tá pedindo para ele poder fazer o treinamento e no caso a tarefa é detecção a gente tá passando aqui né o banco de dados a nossa pasta e a gente tá passando aqui o o data pamel que é onde tá as configurações da

do nosso banco de dados a gente tá passando aqui também 50 épocas e a gente tá pré-definido as imagens como 640 na verdade eu não vou mudar o Essa é de código Porque eu já tenho o modelo treinado né mas eh vocês vão ter que fazer esse o treinamento né Então até para vocês darem uma olhada um processo que demora bastante então

vocês vão ter que ter bastante paciência Então são todos os parâmetros né que ele tá passando ele vai começar a fazer o treinamento como eu não preciso fazer o treinamento Porque eu já tenho modelo posso pausar isso aqui né mas depois que ele terminar o o treinamento ele vai criar uma pasta aqui chamada runs e nela vai ter uma pasta chamada pesos e lá vai est o arquivo chamado best.pt é o melor

melhor modelo que ele conseguiu treinar para poder fazer a detecção então agora aqui dentro do nosso V code a gente vai mudar o nosso modelo eu renomeio o nosso modelo como ppe PPT né E a gente vai passar para ele esse vídeo aqui para ele poder fazer a detecção das roupas de segurança né então A ideia é que ele crie né o as caixas delimitadoras e classifique

cada objeto então basicamente aqui a gente tá passando o vídeo a gente tá carregando o modelo colocando o nome das classes aqui a gente quer salvar o vídeo quando ele for depois que ele for processado então a gente colocou aqui como output vídeo em 20 frames para não demorar muito e aqui a tá passando o o vídeo Model

e e aqui a gente tá definindo a caixa da limitadora né aqui o c é o nível de confiança ou seja basicamente É como se você tivesse perguntando pro modelo de zero a um quanto que ele acha que T objeto é aquela coisa então por exemplo de zero a ponto que ele acha que aquele objeto é uma caixa é um

con de segurança e aqui nessa condição a gente tá definindo o que e confiança ou seja se quanto a a certeza do modelo de tal objeto ser aquela coisa for maior do que 0.5 a gente vai e criar a caixa limitadora para poder para poder aparecer na na tela né aqui no final a gente só tá salvando a

imagem e depois criando aqui um uma condição que clicando a tecla q a gente fecha o vi e agora né a gente pode só simplesmente rodar e como o minha a minha máquina não tem uma GPU o frame rate vai est bem baixo ou seja e ele vai est bem travado Mas como é por é C didático eu vou fazer o qu

e vou mostrar o vídeo já com o já processado com as detecções então agora né que o vídeo foi processado Então na verdade eu até parei um pouco antes porque tava demorando muito o arquivo output vídeo foi criado então a gente pode abrir o vs code ele não permite Então esse arquivo você abr nele né você des abrindo por fora O resultado é esse

o vídeo original Na verdade tem 8 segundos esse tem mais ou menos un seis que eu parei um pouco antes tava demorando muito então eu só encerrei ali o a execução Mas se você tiver uma máquina tiver uma placa de vídeo ele vai rodar muito mais liso né chando podendo chegar até 30 frames por segundo show de bola né bom esse conteúdo aqui foi bem pesado porque não tem quase ninguém no Brasil falando então se você gostou deixa aqui seu comentário positivo indica pra gente também

outros assuntos que você queira est vendo aqui no canal deixa aqui sua curtida e se você quiser aprender Python de verdade clica aqui no link da descrição que tem produtos para caramba para você aprender sobre Python Beleza tamo junto até a próxima


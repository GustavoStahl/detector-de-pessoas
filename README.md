# Sistema de segurança autônomo através de detecção de pessoas

## Funcionamento do projeto
![](funcionamento.gif)

## Funcionalidades do projeto
### Encontra e mostra pessoas
- Encontra pessoas na imagem e as mostra demarcadas por uma caixa em tempo real.

### Armazena pessoas encontradas de forma organizada e autônoma
- Salva em tempo real o conteúdo das caixas demarcadas em subpastas encontradas na pasta "YOLO". As imagens resultantes desse processo são nomeadas de acordo com o tempo do sistema operacional em que foram encontradas pelo programa. 
- As subpastas de "YOLO" serão nomeadas por intervalos de tempo de seis horas. Sendo assim, quatro pastas serão criadas: "0-6","6-12", "12-18", "18-24".
- Ao acessar a subpasta com nome relativo ao intervalo de tempo atual, pode-se observar a criação das imagens em tempo real.

### Realiza backup dos dados já armazenados de forma autônoma
- Em um determinado horário definido pelo usuário, uma nova pasta será criada dentro da pasta "Banco". Essa nova pasta terá como nome o dia atual e nela serão armazenadas as imagens salvas pelo programa no dia em questão de subpastas. Essas subpastas de "Banco" serão criadas com os mesmos nomes das subpastas de "YOLO", preservando o sistema de organização já explicado anteriormente em um dos tópicos acima. 

## Instruções para uso do projeto

### O que faz o arquivo [**seg.py**](https://github.com/GustavoStahl/detector-de-pessoas/blob/master/seg.py)?
- seg.py é um sistema de backup que cria uma pasta dentro da pasta "Banco" com o dia atual marcado no sistema e move todas as imagens salvas na pasta "YOLO" para essa pasta criada. Nesse processo, as imagens serão movidas para dentro de pastas demarcadas com horários, mantendo a organização proposta. Vale ressaltar que o uso desse sistema é recomendado, porém opcional.

### Os valores das variáveis globais HORA, MINUTO e SEGUNDO no arquivo seg.py
- HORA, MINUTO e SEGUNDO: hora, minuto e segundo desejados pelo usuário para armazenar na pasta "Banco" todas as imagens salvas no dia, semelhante a um backup.
- Embora seja possível alterar os horários mencionados, é recomendado que deixe nas configurações atuais. O intuíto do projeto é realizar diariamente um backup dos dados, criando uma pasta referente ao dia anterior. 

## Recomendações ao usuário para utilizar o repositório
- Utilize o conda para criar ambientes virtuais.
- Use cuda e cudnn para ter um melhor desempenho (verifique se a GPU é compatível).
- Recomenda-se Linux para realizar os procedimentos.

## Instalação
**Sugestão:** Use os seguintes trechos de código em ordem para instalar os requisitos. Necessário ter os pacotes git e wget.

### Python 
Recomenda-se versão 3.7

### Crie um ambiente virtual com o conda
`conda create -n <nome-do-ambiente> python=3.7`
`conda activate <nome-do-ambiente>` 

### Instale as dependecias necessarias
- ### Tensorflow (recomenda-se versões <= 1.15.2)
`pip install tensorflow==1.15.2` (CPU)<br/>
`pip install tensorflow-gpu==1.15.2` (GPU)

- ### Opencv
```pip install opencv-python```

- ### Tqdm
```pip install tqdm```

### Clone o repositório do projeto e salve-o no disco
```git clone https://github.com/GustavoStahl/detector-de-pessoas.git```

### Va para a pasta [**darknet_weights**](https://github.com/GustavoStahl/detector-de-pessoas/tree/master/data/darknet_weights) e baixe o arquivo de pesos da rede
```cd detector-de-pessoas/data/darknet_weights && wget https://pjreddie.com/media/files/yolov3.weights``` 
   
### Converta os pesos com o arquivo [**convert_weight.py**](https://github.com/GustavoStahl/detector-de-pessoas/blob/master/convert_weight.py) na pasta base do projeto
```cd .. && cd .. && python convert_weight.py```

### Caso queira utilizar o [**seg.py**](https://github.com/GustavoStahl/detector-de-pessoas/blob/master/seg.py), inicie-o no terminal:
```python seg.py```

### Inicie o sistema com uma câmera reconhecida no computador
`python camera_test.py --camera X`<br/>
Substitua X pelo número de reconhecimento da camera pelo sistema. Exemplo: `--camera 0` para webcam
	
## Informações
Este projeto é parte dos projetos da RAS Unesp Bauru. Para mais informações a respeito desse e outros projetos, acesse: https://sites.google.com/unesp.br/rasunespbauru/home

## Autores

- [**Fabricio Amoroso**](https://github.com/lefabricion)
- [**Gustavo Stahl**](https://github.com/GustavoStahl)
- [**Vinicius Pilan**](https://github.com/ViniPilan)
- [**Vitor Vecina**](https://github.com/vitorvecina)

## Licença

Este projeto é gratuito e sem fins lucrativos. Sua venda é proibida.

## Créditos

Baseado no projeto: [**YOLOv3_TensorFlow**](https://github.com/wizyoung/YOLOv3_TensorFlow)

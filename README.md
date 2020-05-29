# Sistema de segurança autônomo através de detecção de pessoas

## Funcionamento do projeto
![](funcionamento.gif)

## Funcionalidades do projeto
### Encontra e mostra pessoas
- Encontra pessoas na imagem e as mostra demarcadas por uma caixa em tempo real.

### Armazena pessoas encontradas de forma organizada e autônoma
- Salva em tempo real o conteúdo das caixas demarcadas em subpastas encontradas na pasta "YOLO". As imagens resultantes desse processo são nomeadas de acordo com o tempo do sistema operacional em que a pessoa foi encontrada pelo programa. 
- As subpastas de "YOLO" são nomeadas por intervalos de tempo de seis horas. Sendo assim, existem quatro pastas: "0-6","6-12", "12-18", "18-24".
- Ao acessar a subpasta com nome relativo ao intervalo de tempo atual, pode-se observar a criação das imagens em tempo real.

### Organiza os dados já armazenados de forma autônoma
- Para acionar esse recurso, é necessário que o arquivo seg.py tenha uma execução constante. Para isso, basta executá-lo em um novo terminal. O sistema de backup foi desenvolvido para a plataforma Linux e, por isso, pode necessitar de adaptações para outras plataformas.
- Mais informações sobre seg.py estão localizadas no próximo tópico. 


## Instruções para uso do projeto

### O que faz o arquivo [**seg.py**](https://github.com/GustavoStahl/detector-de-pessoas/blob/master/seg.py) e como deve ser utilizado?

- seg.py é um sistema de organização que cria uma pasta dentro da pasta "Banco" com o nome referente ao dia anterior marcado no sistema e move todas as imagens salvas nas subpastas de "YOLO" para subpastas da nova pasta criada. Todo esse processo ocorre as 00:00 am do sistema em que o programa seg.py está sendo executado. Vale ressaltar que o uso desse sistema é recomendado, porém opcional.
- As subpastas de "Banco" serão criadas com os mesmos nomes das subpastas de "YOLO", preservando o sistema de organização já explicado anteriormente em um dos tópicos acima. 
- seg.py deve estar em constante execução no sistema para que a autonomia do sistema esteja de acordo com a ideia proposta no projeto. Portanto, recomenda-se que ele seja executado em um terminal separado e que não seja interrompido em nenhum momento.

### Os valores das variáveis globais HORA, MINUTO e SEGUNDO no arquivo seg.py
- HORA, MINUTO e SEGUNDO: hora, minuto e segundo em que serão armazenadas, na pasta "Banco", todas as imagens salvas durante o dia anterior.
- Embora seja possível alterar os horários mencionados, é recomendado que deixe nas configurações padrões (00:00:01 - hora:minuto:segundo). O intuíto do projeto é realizar diariamente a organização dos dados, criando uma pasta referente ao dia anterior. 

## Recomendações ao usuário para utilizar o repositório
- Utilize o conda para criar ambientes virtuais.
- Use cuda e cudnn para ter um melhor desempenho (verifique se a GPU é compatível).
- Recomenda-se Linux para realizar os procedimentos.

## Instalação
**Sugestão:** Use os seguintes trechos de código em ordem para instalar os requisitos. Necessário ter os pacotes git e wget.

### Python 
Recomenda-se versão 3.7

### Crie um ambiente virtual com o conda
`conda create -n <nome-do-ambiente> python=3.7`<br/>
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
- [**Vinícius Pilan**](https://github.com/ViniPilan)
- [**Vitor Vecina**](https://github.com/vitorvecina)

## Licença

Este projeto é gratuito e sem fins lucrativos. Sua venda é proibida.

## Créditos

Baseado no projeto: [**YOLOv3_TensorFlow**](https://github.com/wizyoung/YOLOv3_TensorFlow)

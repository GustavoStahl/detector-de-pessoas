# Sistema de segurança autônomo através de detecção de pessoas

## Funcionalidades do projeto:
### Encontra e mostra pessoas
- Encontra pessoas na imagem e as mostra demarcadas por uma caixa em tempo real

### Armazena pessoas encontradas de forma organizada e autônoma
- Salva em tempo real o conteúdo das caixas demarcadas em subpastas encontradas na pasta "YOLO". As imagens resultantes desse processo são nomeadas de acordo com o tempo do sistema operacional em que foram encontradas pelo programa. 
- As subpastas de "YOLO" serão nomeadas por intervalos de tempo de seis horas. Sendo assim, quatro pastas serão criadas: "0-6","6-12", "12-18", "18-24"
- Ao acessar a subpasta com nome relativo ao intervalo de tempo atual, pode-se observar a criação das imagens em tempo real

### Realiza backup dos dados já armazenados de forma autônoma
- Em um determinado horário definido pelo usuário, uma nova pasta será criada dentro da pasta "Banco". Essa nova pasta terá como nome o dia atual e nela serão armazenadas as imagens salvas pelo programa no dia em questão de subpastas. Essas subpastas de "Banco" serão criadas com os mesmos nomes das subpastas de "YOLO", preservando o sistema de organização já explicado anteriormente em um dos tópicos acima. 



## Recomendações ao usuário para utilizar o repositório:
- Use o Conda para criar ambientes virtuais<br/>
- Use cuda e cudnn para ter um melhor desempenho (verifique se a GPU é compatível)


## Instalação e recomendações:
### Python (recomenda-se versão 3.7):
- ```conda create -n <nome-do-ambiente> python=3.7``` (exemplo de instalação do python através da criação de um ambiente virtual utilizando o anaconda)

### Tensorflow (recomenda-se versão <= 1.15):
- ```pip install tensorflow==1.15```

### Opencv:
- ```pip install opencv-python```

### Tqdm:
- ```pip install tqdm```

### Baixe o repositório do projeto e salve-o no disco
- ```git clone https://github.com/GustavoStahl/detector-de-pessoas.git```

### Baixe o arquivo dos pesos da rede
- ```https://pjreddie.com/media/files/yolov3.weights``` 
   
### Salve o arquivo baixado em: "./data/darknet_weights/", dentro do repositório do projeto
   
### Execute o comando abaixo no terminal
- ```python convert_weight.py```


## Instruções para uso do projeto

### O que faz o arquivo seg.py?
- seg.py é um sistema de backup que cria uma pasta dentro da pasta "Banco" com o dia atual marcado no sistema e move todas as imagens salvas na pasta "YOLO" para essa pasta criada. Nesse processo, as imagens serão movidas para dentro de pastas demarcadas com horários, mantendo a organização proposta. Vale ressaltar que o uso desse sistema é recomendado, porém opcional.

### Os valores das variáveis globais HORA, MINUTO e SEGUNDO no arquivo seg.py:
- HORA, MINUTO e SEGUNDO: hora, minuto e segundo desejados pelo usuário para armazenar na pasta "Banco" todas as imagens salvas no dia, semelhante a um backup.
- Embora seja possível alterar os horários mencionados, é recomendado que deixe nas configurações atuais. O intuíto do projeto é realizar diariamente um backup dos dados, criando uma pasta referente ao dia anterior. 

### Caso queira utilizar o seg.py, inicie no terminal o arquivo:
- ```python seg.py```

### Inicie o sistema com uma câmera reconhecida no computador:
- ```python camera_test.py --camera X``` (substitua X pelo número de reconhecimento da camera pelo sistema, exemplo: X=0 para webcam))
	
## Informações
Este projeto é parte dos projetos da RAS Unesp Bauru. Para mais informações a respeito desse e outros projetos, acesse: https://sites.google.com/unesp.br/rasunespbauru/home

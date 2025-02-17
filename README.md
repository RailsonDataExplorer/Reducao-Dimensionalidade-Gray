# 🖼️ Conversão de Imagem - Tons de Cinza e Binarização 🎨

Este projeto tem como objetivo aplicar técnicas simples de processamento de imagens, como conversão para tons de cinza e binarização. Ele ajuda na **redução de dimensionalidade** das imagens, tornando-as mais fáceis de manipular e permitindo operações de pré-processamento, como detecção de bordas, segmentação e compressão.

### 📋 Índice
- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Resultados Esperados](#-resultados-esperados)
- [Contribuições](#-contribuições)
- [Licença](#-licença)
- [Reconhecimentos](#-reconhecimentos)
- [Links Úteis](#-links-úteis)

## 🌟 Visão Geral
O objetivo deste projeto é demonstrar como aplicar técnicas simples de processamento de imagens para transformar uma imagem colorida em representações mais simples, como tons de cinza e binária (preto e branco). Essas técnicas são úteis para:

- **Redução de Dimensionalidade**: Simplifica os dados ao eliminar nuances de cor, deixando a imagem mais fácil de processar.
- **Pré-processamento**: Facilita operações como detecção de bordas e segmentação, frequentemente usadas em visão computacional.
- **Compressão**: Reduz o tamanho das imagens, o que é útil para economizar espaço e facilitar o armazenamento.

Além disso, o projeto organiza as imagens em pastas separadas para um melhor gerenciamento e organização dos arquivos.

## 🔧 Funcionalidades
- **Conversão para Tons de Cinza**: Transforma uma imagem colorida em uma versão em escala de cinza, eliminando as cores.
- **Binarização**: Converte a imagem em tons de cinza em uma imagem binária (preto e branco), com base em um limiar configurável.
- **Redução de Tamanho**: Reduz o tamanho da imagem original em 50% para facilitar a visualização e análise.
- **Organização de Arquivos**: Salva as imagens originais e processadas em pastas separadas para melhor organização.
- **Visualização**: Exibe as imagens processadas usando a biblioteca `matplotlib`.

## 💻 Requisitos
Para executar este projeto, você precisará de:

- **Python 3.7+**
- **Pillow**: Biblioteca para manipulação de imagens.
- **NumPy**: Biblioteca para operações matemáticas e manipulação de arrays.
- **Requests**: Biblioteca para baixar imagens da web.
- **Matplotlib**: Biblioteca para exibição das imagens.

Instale as dependências com o seguinte comando:

`
pip install pillow numpy requests matplotlib
## 🔧 Instalação
1. Clone o Repositório
Clone este repositório para o seu ambiente local com o comando:

`git clone https://github.com/seu-usuario/conversao-imagem.git`
`cd conversao-imagem`
2. Instale as Dependências
Dentro do diretório do projeto, instale as dependências usando o pip:

`pip install -r requirements.txt`
## 🚀 Uso
Após configurar o ambiente e as dependências, você pode executar o script principal para processar uma imagem. Basta rodar o seguinte comando:

`python main.py`
Após a execução, as imagens processadas serão salvas nas seguintes pastas:

Imagem Original: input_images/imagem_original.jpg
Imagens Processadas:
output_images/imagem_cinza.jpg (Imagem convertida para tons de cinza)
output_images/imagem_binarizada.jpg (Imagem binarizada)
output_images/imagem_reduzida.jpg (Imagem original reduzida para 50%)
Você também verá as imagens exibidas em janelas interativas usando o matplotlib.

📂 Estrutura do Projeto
Aqui está a estrutura de diretórios e arquivos do projeto:

```conversao-imagem/
├── main.py                     # Código principal que executa o processamento da imagem
├── input_images/               # Pasta para armazenar imagens baixadas da URL
│   └── imagem_original.jpg     # Imagem original baixada
├── output_images/              # Pasta para armazenar imagens processadas
│   ├── imagem_cinza.jpg        # Imagem convertida para tons de cinza
│   ├── imagem_binarizada.jpg   # Imagem binarizada
│   └── imagem_reduzida.jpg     # Imagem original reduzida em 50%
├── requirements.txt            # Lista de dependências
└── README.md                   # Este arquivo
```
## 📈 Resultados Esperados
Após o processamento, você obterá as seguintes imagens:

Imagem em Tons de Cinza: A versão simplificada da imagem original, convertida para escala de cinza.
Imagem Binarizada: A imagem original convertida para preto e branco com base em um limiar (threshold).
Imagem Reduzida: A imagem original redimensionada para 50% do seu tamanho.
Exemplo de Visualização:


Nota: Substitua a URL da imagem no código pelo link desejado para testar com diferentes imagens.

## 🤝 Contribuições
Contribuições são bem-vindas! Para contribuir com o projeto, siga estas etapas:

Faça um fork deste repositório.
Crie uma branch para sua contribuição:

`git checkout -b feature/nova-funcionalidade`
Envie um pull request detalhando suas alterações.
## 📜 Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

## 🙏 Reconhecimentos
Pillow: Pela excelente biblioteca de manipulação de imagens.
NumPy: Pela eficiência em operações matriciais.
Matplotlib: Pela visualização de imagens.
Requests: Pela facilidade de download de arquivos via URL.
## 🌐 Links Úteis

- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/) - Documentação oficial do Pillow, biblioteca de manipulação de imagens em Python.
- [NumPy Documentation](https://numpy.org/doc/) - Documentação oficial do NumPy, biblioteca para operações matemáticas e manipulação de arrays.
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) - Documentação oficial do Matplotlib, biblioteca para visualização de gráficos e imagens.
- [Requests Documentation](https://docs.python-requests.org/en/master/) - Documentação oficial do Requests, biblioteca para realizar requisições HTTP em Python.

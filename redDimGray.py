from PIL import Image
import numpy as np
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Função para converter uma imagem colorida para tons de cinza
def convert_to_grayscale(image):
    # Converte a imagem para o modo 'L' (escala de cinza)
    grayscale_image = image.convert("L")
    return grayscale_image

# Função para binarizar uma imagem em tons de cinza
def binarize_image(grayscale_image, threshold=128):
    # Converte a imagem para um array numpy
    grayscale_array = np.array(grayscale_image)
    
    # Aplica o limiar para binarizar a imagem
    binary_array = np.where(grayscale_array > threshold, 255, 0)
    
    # Converte o array binarizado de volta para uma imagem
    binary_image = Image.fromarray(binary_array.astype(np.uint8))
    return binary_image

# URL da imagem
image_url = "https://th.bing.com/th/id/OIP.D5GcpD2Zv_1h5dBPnt8R_AHaE8?rs=1&pid=ImgDetMain"  # Substitua pela sua URL

# Baixar a imagem usando requests
response = requests.get(image_url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Abrir a imagem a partir dos dados recebidos
    color_image = Image.open(BytesIO(response.content))
    
    # Passo 1: Converter para tons de cinza
    grayscale_image = convert_to_grayscale(color_image)

    # Passo 2: Binarizar a imagem
    threshold_value = 128  # Limiar para binarização
    binary_image = binarize_image(grayscale_image, threshold=threshold_value)

    # Reduzir o tamanho da imagem original em 50%
    reduced_color_image = color_image.resize((color_image.width // 2, color_image.height // 2))

    # Salvar as imagens resultantes
    grayscale_image.save("imagem_cinza.jpg")
    binary_image.save("imagem_binarizada.jpg")
    reduced_color_image.save("imagem_reduzida.jpg")

    # Exibir as imagens usando matplotlib
    fig, axs = plt.subplots(1, 3, figsize=(16, 6))

    # Exibir a imagem original reduzida
    axs[0].imshow(reduced_color_image)
    axs[0].set_title("Imagem Original (Reduzida 50%)")
    axs[0].axis('off')  # Desliga os eixos

    # Exibir a imagem em tons de cinza
    axs[1].imshow(grayscale_image, cmap='gray')
    axs[1].set_title("Imagem em Tons de Cinza")
    axs[1].axis('off')  # Desliga os eixos

    # Exibir a imagem binarizada
    axs[2].imshow(binary_image, cmap='gray')
    axs[2].set_title("Imagem Binarizada")
    axs[2].axis('off')  # Desliga os eixos

    plt.show()

else:
    print("Erro ao baixar a imagem.")

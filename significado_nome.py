# Websacraping para pesquisar significado de nome próprio

# importação das bibliotecas necessárias (pode ser necessário instalar antes pelo pipinstall - procurar sintaxe de cada uma no google, se der erro na instalçao padrão)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import webbrowser

# entrada de dados
nome = input("Qual o seu nome? ")

# para rodar o navegador google chrome em segundo plano/invisível
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
navegador = webdriver.Chrome(options=chrome_options)

# abre site de pesquisa de nome e passa o nome de parametro
navegador.get("https://www.dicionariodenomesproprios.com.br/" + nome)

# captura o primeiro resultado com o comando .text
significado = navegador.find_element(By.XPATH, '//*[@id="significado"]/p[1]').text

# imprime resultado
print(significado)

# fechar navegador
navegador.close()
navegador.quit()

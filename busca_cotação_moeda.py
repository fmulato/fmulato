from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from datetime import datetime

def fechar():
    janela.destroy()

def pegar_cotacoes():
    navegador = webdriver.Chrome()

    navegador.get("https://br.investing.com/currencies/streaming-forex-rates-majors")
    navegador.minimize_window()
    x = navegador.find_element(By.XPATH, '//*[@id="pair_2103"]/td[3]').text
    y = navegador.find_element(By.XPATH, '//*[@id="pair_1"]/td[3]').text
    z = navegador.find_element(By.XPATH, '//*[@id="pair_2"]/td[3]').text

    #trocando virgula por ponto e convertendo em float

    x1 = float(x.replace(",", "."))
    y1 = float(y.replace(",", "."))
    z1 =float(z.replace(",", "."))
      
    cotacao_dolar = round(x1,4)
    cotacao_euro = round(x1*y1,4)
    cotacao_libra = round(x1*z1,4)
    data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Libra: {cotacao_libra}\n
    Atualizado em: {data_hora_atual}'''

    navegador.quit()

janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas em Reais (R$)")
texto.grid(column=0, row=0, padx=60, pady=60)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.place(x=140, y=100)

botao = Button(janela, text="Fechar", command=fechar)
botao.place(x=280, y=100)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

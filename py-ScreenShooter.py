import requests
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_opcoes = Options()
chrome_opcoes.add_argument("--headless")
chrome_opcoes.add_argument("--log-level=3")
chrome_opcoes.binary_location = "chrome-windows/chrome.exe"

chrome_navegador = webdriver.Chrome('chrome-windows/chrome-driver.exe', chrome_options=chrome_opcoes)
chrome_navegador.set_window_size(1920,1080)

total_alvos = sum(1 for linha in open("alvos.txt", "r"))
contador = 0


with open('alvos.txt', 'r') as f:
	for linha in f.read().splitlines():

		print(str(contador) + '/' + str(total_alvos))
		contador = contador + 1
		
		try:
			chrome_navegador.get('http://' + linha)
			linha = linha.replace('.', '-')
			chrome_navegador.save_screenshot(linha + '.png')
			
		except:
			print("[+]FALHA")

chrome_navegador.close()
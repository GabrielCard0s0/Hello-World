import time

def ola(texto, atraso=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
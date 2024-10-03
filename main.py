import saudacao, time

while True:
    saudacao.ola("\nDigite [hello] para prosseguir ou [quit] para sair.")
    frase = input('\n> ').lower()
    time.sleep(1)
    try:
        if frase == 'hello':
            saudacao.ola('Hello World!')
        elif frase == 'quit':
            saudacao.ola('Finalizando...')
            time.sleep(1)
            break
        else:
          saudacao.ola("Digite uma frase válida!")  
    except TypeError:
        saudacao.ola("Digite uma frase válida!")
from pacote.calculo import Calculo


# Função principal.
def jogar(pontos):
    # O usuario digita um valor inteiro que corresponde à dificuldade.
    dificuldade: int = int(input('escolha a dificuldade [1 - Fácil, 2 - Médio, 3 - Difícil, 4 - Muito difícil]: '))

    # Criação da variável 'calc' que será responsável por armazena os valores gerados, operações, tipo de operação e resultado.
    calc: Calculo = Calculo(dificuldade)

    print('Qual o resultado da seguinte operação: ')
    print(calc.mostra_operacao) # Printa uma operação matemática ex: 10 + 5 = ?

    resultado: int = int(input()) # O usuário digita o resultado da operação.

    # O método "checa_resultado" retorna True se o resultado do usuário for correto e False caso contrário.
    if calc.checa_resultado(resultado):
        pontos += 1
        print('Resposta Correta!')
    else:
        print('Resposta Errada!')    

    calc.mostra_resultado() # O resultado é exibido na tela.

    print(f'Você tem {pontos} ponto(s)')
    
    continuar: int = int(input('Deseja continuar [1 - sim, 0 - não]: ')) 

    if continuar:
        jogar(pontos) # Volta a função "jogar" recursivamente e com os pontos atualizados.
    else:
        print(f'Você terminou o jogo com {pontos} ponto(s)')
        print(f'Até a próxima!')
    


def main():
    # Pontos iniciais igual a zero.
    pontos: int = 0
    jogar(pontos)


if __name__ == '__main__':
    main()
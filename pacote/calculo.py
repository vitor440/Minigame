from random import randint

class Calculo:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade # Dificuldade(1 - Fácil, 2 - Médio, 3 - Dificil, 4 - Muito dificil)
        self.__valor1: int = self._gerar_valor()
        self.__valor2: int = self._gerar_valor()
        self.__operacao: int = randint(1, 3)
        self.__resultado: int = self._gerar_resultado()

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Soma'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicação'
        else:
            op = 'Operação Desconhecida'

        return f'Dificuldade: {self.dificuldade} \nValor1: {self.valor1} \nValor2: {self.valor2} \noperação: {op} \nResultado: {self.resultado}'


    def _gerar_valor(self: object) -> int:
        """ Função que gera números aleatórios com intervalos que dependem da dificuldade."""

        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    def _gerar_resultado(self: object) -> int:
        """ Função que retorna o resultado de uma operação com os valores 1 e 2 gerados.
            1 - '+' Soma
            2 - '-' Subtração
            3 - '*' Multiplicação
        """

        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def simbolo_operacao(self: object) -> str:
        """ Função que retorna qual deve ser a operação realizada dependendo do número aleatório gerado."""

        op: str = ''
        if self.operacao == 1:
            op = '+'
        elif self.operacao == 2:
            op = '-'
        elif self.operacao == 3:
            op = '*'
        
        return op


    @property
    def mostra_operacao(self: object) -> str:
        """ Retorna a operação gerada. Ex: return = 54 + 12 = ?"""
        return f'{self.valor1} {self.simbolo_operacao} {self.valor2} = ?'


    def checa_resultado(self: object, result: int) -> bool:
        """ Verifica se a resposta fornecida pelo usuário é correta ou incorreta."""

        flag: bool = False

        if self.resultado == result:
            flag = True

        return flag

    def mostra_resultado(self: object) -> None:
        """ Printa o resultado da operação: ex: 25."""
        print(f'{self.valor1} {self.simbolo_operacao} {self.valor2} = {self.resultado}')
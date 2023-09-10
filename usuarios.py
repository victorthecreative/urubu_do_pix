import random
import string
import sqlite3

from database import inserir_usuario, inserir_deposito

class Usuario:
    def __init__(self):
        self.nome = input('Bem-vindo ao Urubu do Pix! Para começar, nos diga o seu nome: ')
        self.chave_aleatoria = self.gerar_chave()
        inserir_usuario(self.nome, self.chave_aleatoria)

    def gerar_chave(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    def __str__(self):
        return f'{self.nome}. Sua chave é {self.chave_aleatoria}.'

class Deposito:
    def __init__(self, usuario):
        self.nome = usuario.nome
        self.user_id = usuario.chave_aleatoria
        self.valor_deposito = self.obter_valor_deposito()
        self.codigo_deposito = self.gerar_codigo_deposito()

    def obter_valor_deposito(self):
        while True:
            valor = input(f'{self.nome}, quanto gostaria de investir hoje? R$ ')
            try:
                valor = float(valor)
                if valor >= 200:
                    return valor
                else:
                    print("O valor mínimo para depósito é de R$ 200,00. Por favor, insira um valor maior.")
            except ValueError:
                print("Por favor, insira um valor válido.")

    def gerar_codigo_deposito(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    def __str__(self):
        return f'{self.nome}, o ID do seu depósito é {self.codigo_deposito}. Use-o para buscar informações sobre seu depósito.'

def main():
    usuario = Usuario()
    deposito = Deposito(usuario)
    print(deposito)

if __name__ == "__main__":
    main()

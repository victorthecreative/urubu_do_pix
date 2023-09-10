import sqlite3
from database import inserir_rendimento, buscar_depositos_por_chave

juros = 0.3333

class CalculoRendimento:
    def __init__(self, deposito):
        self.nome = deposito[1]
        self.user_id = deposito[2]
        self.valor_depositado = float(deposito[3])
        self.codigo_deposito = deposito[4]

    def calcular_rendimento(self):
        lista_rendimentos = []
        valor_atual = self.valor_depositado

        for dia in range(1, 31):
            rendimento_do_dia = valor_atual * juros
            valor_atual += rendimento_do_dia

            detalhes_dia = {
                "Dia": dia,
                "Nome": self.nome,
                "ID do Usuário": self.user_id,
                "ID da Transação": self.codigo_deposito,
                "Valor Depositado": self.valor_depositado,
                "Rendimento": round(rendimento_do_dia, 2)
            }

            inserir_rendimento(
                dia, self.nome, self.user_id, self.codigo_deposito, 
                self.valor_depositado, detalhes_dia["Rendimento"]
            )

            lista_rendimentos.append(detalhes_dia)

        return lista_rendimentos

def main_rendimento():
    user_id = input("Digite o ID do usuário: ")

    depositos = buscar_depositos_por_chave(user_id)

    if not depositos:
        print("Nenhum depósito encontrado para este usuário.")
        return

    print("Depósitos disponíveis:")
    for index, deposito in enumerate(depositos, 1):
        print(f"{index}. Código do Depósito: {deposito[4]}, Valor Depositado: R$ {deposito[3]}")

    escolha = int(input("Selecione o número do depósito para calcular o rendimento: "))

    if 1 <= escolha <= len(depositos):
        deposito_selecionado = depositos[escolha - 1]
        calc = CalculoRendimento(deposito_selecionado)
        lista_rendimentos = calc.calcular_rendimento()

        print("\nDetalhes do Rendimento:")
        for rendimento in lista_rendimentos:
            print(rendimento)
    else:
        print("Escolha inválida. Por favor, selecione um número de depósito válido.")

if __name__ == "__main__":
    main_rendimento()

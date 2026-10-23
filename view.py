from Model import BancoDados
from service import ContaService
from controller import ContaController


class BancoView:
    def __init__(self):
        self.db = BancoDados()
        self.service = ContaService(self.db)
        self.controller = ContaController(view=self, service=self.service)

    def obter_dados_cliente(self):
        print("\n--- ABERTURA DE CONTA ---")
        nome = input("Nome do titular: ").strip()
        cpf = input("CPF do titular: ").strip()
        while True:
            try:
                saldo = float(input("Saldo Inicial (R$): "))
                return nome, cpf, saldo
            except ValueError:
                print("Digite um valor numérico válido.")

    def pedir_numero_conta(self):
        return input("\nDigite o número da conta (ex: 001): ").strip()

    def pedir_valor_operacao(self, tipo_operacao):
        while True:
            try:
                return float(input(f"Digite o valor do {tipo_operacao} (R$): "))
            except ValueError:
                print("Digite um valor numérico válido.")

    def exibir_conta_criada(self, conta):
        print(f"\n🎉 Conta {conta.numero} criada! Titular: {conta.titular.nome} | Saldo: R$ {conta.saldo:.2f}")

    def exibir_mensagem(self, mensagem):
        print(f"\nℹ️  [Sistema]: {mensagem}")

    def exibir_lista_contas(self, contas):
        print(f"\n{'Nº':<5} | {'TITULAR':<20} | {'SALDO':<12}")
        print("-" * 42)
        for c in contas:
            print(f"{c.numero:<5} | {c.titular.nome:<20} | R$ {c.saldo:>9.2f}")

    def exibir_historico_tela(self, conta, historico):
        print("\n" + "=" * 45)
        print(f"{'HISTÓRICO / EXTRATO':^45}")
        print("=" * 45)
        print(f"Conta: {conta.numero} | Titular: {conta.titular.nome}")
        print(f"Saldo Atual: R$ {conta.saldo:.2f}")
        print("-" * 45)
        for evento in historico:
            print(f" • {evento}")
        print("=" * 45 + "\n")

    def executar_interface(self):
        while True:
            print("\n=== BANCO MULTICAMADAS ===")
            print("1. Cadastrar Nova Conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Ver Extrato e Histórico")
            print("5. Listar Todas as Contas")
            print("6. Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.controller.cadastrar_nova_conta()
            elif opcao == "2":
                self.controller.depositar()
            elif opcao == "3":
                self.controller.sacar()
            elif opcao == "4":
                self.controller.exibir_extrato_completo()
            elif opcao == "5":
                self.controller.listar_contas()
            elif opcao == "6":
                print("\nAté logo!")
                break
            else:
                print("\nOpção inválida!")


if __name__ == "__main__":
    app = BancoView()
    app.executar_interface()
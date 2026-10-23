# rabbits/views/rabbits.views.py
class BancoView:
    def __init__(self, controller):
        self.controller = controller

    def obter_dados_cliente(self):
        print("\n--- ABERTURA DE CONTA ---")
        nome = input("Nome do titular: ").strip()
        cpf = input("CPF do titular: ").strip()
        while True:
            try:
                saldo = float(input("Saldo Inicial (R$): "))
                return nome, cpf, saldo
            except ValueError:
                print("Digite um valor válido.")

    def pedir_numero_conta(self):
        return input("\nDigite o número da conta (ex: 001): ").strip()

    def pedir_valor_operacao(self, tipo):
        while True:
            try:
                return float(input(f"Valor do {tipo} (R$): "))
            except ValueError:
                print("Digite um valor válido.")

    def exibir_conta_criada(self, conta):
        print(f"\n🎉 Conta {conta.numero} criada com sucesso para {conta.titular.nome}!")

    def exibir_mensagem(self, msg):
        print(f"\nℹ️ [Sistema]: {msg}")

    def exibir_lista_contas(self, contas):
        print(f"\n{'Nº':<5} | {'TITULAR':<20} | {'SALDO':<12}")
        print("-" * 42)
        for c in contas:
            print(f"{c.numero:<5} | {c.titular.nome:<20} | R$ {c.saldo:>9.2f}")

    def exibir_historico_tela(self, conta, historico):
        print(f"\n=== HISTÓRICO CONTA {conta.numero} ===")
        for e in historico:
            print(f" • {e}")

    def executar_interface(self):
        while True:
            print("\n=== BANCO MULTICAMADAS (RABBITS) ===")
            print("1. Cadastrar Nova Conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Ver Extrato")
            print("5. Listar Todas as Contas")
            print("6. Sair")
            opcao = input("Opção: ").strip()
            if opcao == "1": self.controller.cadastrar_nova_conta()
            elif opcao == "2": self.controller.depositar()
            elif opcao == "3": self.controller.sacar()
            elif opcao == "4": self.controller.exibir_extrato_completo()
            elif opcao == "5": self.controller.listar_contas()
            elif opcao == "6": break

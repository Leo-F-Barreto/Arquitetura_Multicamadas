# rabbits/controllers/rabbits.controllers.py
class ContaController:
    def __init__(self, view, service):
        self.view = view
        self.service = service
        self._contador_contas = 1

    def cadastrar_nova_conta(self):
        nome, cpf, saldo_inicial = self.view.obter_dados_cliente()
        numero_conta = f"{self._contador_contas:03d}"
        try:
            nova_conta = self.service.criar_conta(numero_conta, nome, cpf, saldo_inicial)
            self._contador_contas += 1
            self.view.exibir_conta_criada(nova_conta)
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def depositar(self):
        numero = self.view.pedir_numero_conta()
        valor = self.view.pedir_valor_operacao("Depósito")
        try:
            conta = self.service.realizar_deposito(numero, valor)
            self.view.exibir_mensagem(f"Sucesso! Novo Saldo: R$ {conta.saldo:.2f}")
        except (ValueError, LookupError) as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def sacar(self):
        numero = self.view.pedir_numero_conta()
        valor = self.view.pedir_valor_operacao("Saque")
        try:
            conta = self.service.realizar_saque(numero, valor)
            self.view.exibir_mensagem(f"Sucesso! Novo Saldo: R$ {conta.saldo:.2f}")
        except (ValueError, LookupError) as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def exibir_extrato_completo(self):
        numero = self.view.pedir_numero_conta()
        try:
            historico = self.service.obter_historico(numero)
            contas = self.service.obter_todas_contas()
            conta = next(c for c in contas if c.numero == numero)
            self.view.exibir_historico_tela(conta, historico)
        except LookupError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def listar_contas(self):
        contas = self.service.obter_todas_contas()
        if not contas:
            self.view.exibir_mensagem("Nenhuma conta cadastrada.")
        else:
            self.view.exibir_lista_contas(contas)

from Model import Cliente, Conta, BancoDados


class ContaService:
    """Camada de Negócios para validar regras e proteger o estado do sistema."""

    def __init__(self, banco_dados: BancoDados):
        self.db = banco_dados

    def criar_conta(self, numero: str, nome: str, cpf: str, saldo_inicial: float) -> Conta:
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios para abrir uma conta.")
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")

        cliente = Cliente(nome, cpf)
        nova_conta = Conta(numero, cliente, saldo_inicial)
        self.db.salvar_conta(nova_conta)
        return nova_conta

    def realizar_deposito(self, numero_conta: str, valor: float) -> Conta:
        conta = self.db.buscar_conta_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada no sistema.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")

        conta.saldo += valor
        conta.historico.append(f"Depósito realizado: +R$ {valor:.2f}")
        return conta

    def realizar_saque(self, numero_conta: str, valor: float) -> Conta:
        conta = self.db.buscar_conta_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada no sistema.")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente para realizar a operação.")

        conta.saldo -= valor
        conta.historico.append(f"Saque realizado: -R$ {valor:.2f}")
        return conta

    def obter_historico(self, numero_conta: str) -> list:
        conta = self.db.buscar_conta_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada no sistema.")
        return conta.historico

    def obter_todas_contas(self) -> list:
        return self.db._contas
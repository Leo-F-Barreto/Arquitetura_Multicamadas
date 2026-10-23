# rabbits/services/rabbits.services.py
from rabbits.models.rabbits_models import Cliente, Conta

class ContaService:
    def __init__(self, banco_dados):
        self.db = banco_dados

    def criar_conta(self, numero: str, nome: str, cpf: str, saldo_inicial: float):
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        cliente = Cliente(nome, cpf)
        nova_conta = Conta(numero, cliente, saldo_inicial)
        self.db.salvar_conta(nova_conta)
        return nova_conta

    def realizar_deposito(self, numero_conta: str, valor: float):
        conta = self.db.buscar_conta_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada.")
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        conta.saldo += valor
        conta.historico.append(f"Depósito realizado: +R$ {valor:.2f}")
        return conta

    def realizar_saque(self, numero_conta: str, valor: float):
        conta = self.db.buscar_conta_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada.")
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente.")
        conta.saldo -= valor
        conta.historico.append(f"Saque realizado: -R$ {valor:.2f}")
        return conta

    def obter_historico(self, numero_conta: str):
        conta = self.db.buscar_conta_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada.")
        return conta.historico

    def obter_todas_contas(self):
        return self.db._contas

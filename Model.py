class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf


class Conta:
    def __init__(self, numero: str, cliente: Cliente, saldo_inicial: float = 0.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo_inicial
        # Propriedade de Histórico solicitada
        self.historico = [f"Abertura de conta com saldo de R$ {saldo_inicial:.2f}"]


class BancoDados:
    def __init__(self):
        self._contas = []

    def salvar_conta(self, conta: Conta):
        self._contas.append(conta)

    def buscar_conta_por_numero(self, numero: str) -> Conta | None:
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None
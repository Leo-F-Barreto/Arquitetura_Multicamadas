# rabbits/models/rabbits.models.py
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, numero: str, cliente: Cliente, saldo_inicial: float = 0.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo_inicial
        self.historico = [f"Abertura de conta com saldo de R$ {saldo_inicial:.2f}"]

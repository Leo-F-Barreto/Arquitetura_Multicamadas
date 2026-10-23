# db/db.py
class BancoDados:
    def __init__(self):
        self._contas = []

    def salvar_conta(self, conta):
        self._contas.append(conta)

    def buscar_conta_por_numero(self, numero: str):
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None

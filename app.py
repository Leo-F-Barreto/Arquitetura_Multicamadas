# app.py
from db.db import BancoDados
from rabbits.services.rabbits_services import ContaService
from rabbits.controllers.rabbits_controllers import ContaController
from rabbits.views.rabbits_views import BancoView

if __name__ == "__main__":
    banco_dados = BancoDados()
    servico = ContaService(banco_dados)
    
    # Criamos a view e injetamos o controller que por sua vez usa o service
    controller = ContaController(view=None, service=servico)
    view = BancoView(controller)
    controller.view = view # Ajuste de referência circular do MVC tradicional
    
    view.executar_interface()

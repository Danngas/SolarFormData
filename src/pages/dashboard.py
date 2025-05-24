# src/pages/dashboard.py
from flet import *

def TelaDashboard():
    return Column(
        controls=[
            Text("Bem-vindo à Dashboard", size=20, weight="bold"),
            Divider(),
            Text("Aqui você verá as estatísticas do sistema."),
        ]
    )

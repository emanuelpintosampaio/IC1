import os
import re
import sys
import matplotlib.pyplot as plt
from IPython.display import Image, display

# Menu das simulações da IC1. No Colab, rode a partir da pasta codigos/ com: %run menu_colab.py
if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

# Cada opção: descrição e script correspondente (None = mostra a figura do relatório).
SIMULACOES = {
    "1": ("Gráfico dos quatro experimentos (E-RT, E-T, E-R e E-CONTROL) | Euler", "IC1_GRAFICOS.py"),
    "2": ("Massa final dos quatro experimentos | Euler Backward", "2)-EULER_IMPLICITO(BACKWARD)_SIMPLIFICAÇÕES.py"),
    "3": ("Velocidade terminal U_f e tempo de vida τ_f", "tau_f.py"),
    "4": ("Solução analítica com r e T constantes (fator integrante)", "edo_fator_integrante.py"),
    "5": ("Figura 3 do relatório final", None),
}

OPCOES_RAIO = {"1": "30", "2": "100", "3": "250", "4": "500"}


def rodar(script, raio):
    """Executa o script sem alterar o arquivo: só o raio inicial r_i é trocado na memória."""
    with open(script, encoding="utf-8") as arquivo:
        codigo = arquivo.read()
    codigo = re.sub(r"^r_i\s*=.*$", f"r_i = {raio}e-6", codigo, count=1, flags=re.M)
    exec(compile(codigo, script, "exec"), {"__name__": "__main__", "__file__": os.path.abspath(script)})


while True:
    # Seleção do raio
    print("\nESCOLHA O RAIO INICIAL DA GOTA")
    for k, v in OPCOES_RAIO.items():
        print(f"{k} - {v} µm")
    opcao_raio = input("Opção: ").strip()
    if opcao_raio not in OPCOES_RAIO:
        print("Opção de raio inválida! Tente novamente.")
        continue
    raio = OPCOES_RAIO[opcao_raio]

    # Seleção da simulação
    print("\nESCOLHA A SIMULAÇÃO")
    for k, (descricao, _) in SIMULACOES.items():
        print(f"{k} - {descricao}")
    opcao_sim = input("Opção: ").strip()
    if opcao_sim not in SIMULACOES:
        print("Opção inválida! Tente novamente.")
        continue

    descricao, script = SIMULACOES[opcao_sim]
    print(f"\n{descricao} | Raio: {raio} µm\n")
    if script is None:
        display(Image(f"../figuras_relatorio/{raio}.png"))
    else:
        rodar(script, raio)
        plt.show()

    # Continuar?
    if input("\nDeseja fazer outra simulação? (s/n): ").strip().lower() != "s":
        print("\nEncerrando o programa...")
        break

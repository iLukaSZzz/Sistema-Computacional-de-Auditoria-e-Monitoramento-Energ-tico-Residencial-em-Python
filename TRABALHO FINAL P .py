# ==========================================================
# SISTEMA COMPUTACIONAL DE AUDITORIA E
# MONITORAMENTO ENERGÉTICO RESIDENCIAL
# Trabalho Final - Lógica de Programação em Python
# ==========================================================

equipamentos = []


# ==========================================================
# CÁLCULO DE CONSUMO
# ==========================================================
def calcular_consumo(potencia, horas):
    return (potencia * horas * 30) / 1000


# ==========================================================
# CLASSIFICAÇÃO ENERGÉTICA
# ==========================================================
def classificar_consumo(consumo):

    if consumo >= 250:
        return "ALTO CONSUMO"

    elif consumo >= 100:
        return "CONSUMO MODERADO"

    else:
        return "BAIXO CONSUMO"


# ==========================================================
# CADASTRO DE EQUIPAMENTOS
# ==========================================================
def cadastrar_equipamento():

    try:

        nome = input("\nNome do equipamento: ")

        potencia = float(
            input("Potência (W): ")
        )

        horas = float(
            input("Horas de uso por dia: ")
        )

        consumo = calcular_consumo(
            potencia,
            horas
        )

        classificacao = classificar_consumo(
            consumo
        )

        equipamento = {
            "nome": nome,
            "potencia": potencia,
            "horas": horas,
            "consumo": consumo,
            "classificacao": classificacao
        }

        equipamentos.append(
            equipamento
        )

        print(
            "\nEquipamento cadastrado com sucesso!"
        )

    except ValueError:

        print(
            "\nERRO: Digite apenas números."
        )


# ==========================================================
# RELATÓRIO
# ==========================================================
def exibir_relatorio():

    if len(equipamentos) == 0:

        print(
            "\nNenhum equipamento cadastrado."
        )

        return

    try:

        tarifa = float(
            input(
                "\nInforme a tarifa "
                "(R$/kWh): "
            )
        )

    except ValueError:

        print(
            "\nValor inválido."
        )

        return

    total_consumo = 0
    total_custo = 0

    print("\n")
    print("=" * 60)
    print("RELATÓRIO DE CONSUMO ENERGÉTICO")
    print("=" * 60)

    for equipamento in equipamentos:

        custo = (
            equipamento["consumo"]
            * tarifa
        )

        equipamento["custo"] = custo

        total_consumo += (
            equipamento["consumo"]
        )

        total_custo += custo

        print(
            f"\nEquipamento: "
            f"{equipamento['nome']}"
        )

        print(
            f"Potência: "
            f"{equipamento['potencia']} W"
        )

        print(
            f"Horas de uso: "
            f"{equipamento['horas']} h/dia"
        )

        print(
            f"Consumo: "
            f"{equipamento['consumo']:.2f} "
            f"kWh/mês"
        )

        print(
            f"Classificação: "
            f"{equipamento['classificacao']}"
        )

        print(
            f"Custo Mensal: "
            f"R$ {custo:.2f}"
        )

    print("\n" + "=" * 60)

    print(
        f"CONSUMO TOTAL: "
        f"{total_consumo:.2f} kWh/mês"
    )

    print(
        f"CUSTO TOTAL: "
        f"R$ {total_custo:.2f}"
    )

    print("=" * 60)


# ==========================================================
# RANKING DE CONSUMO
# ==========================================================
def ranking_consumo():

    if len(equipamentos) == 0:

        print(
            "\nNenhum equipamento cadastrado."
        )

        return

    equipamentos_ordenados = sorted(
        equipamentos,
        key=lambda x: x["consumo"],
        reverse=True
    )

    print("\n")
    print("=" * 50)
    print("RANKING DE CONSUMO")
    print("=" * 50)

    posicao = 1

    for equipamento in equipamentos_ordenados:

        print(
            f"{posicao}º - "
            f"{equipamento['nome']} "
            f"({equipamento['consumo']:.2f} kWh)"
        )

        posicao += 1


# ==========================================================
# RELATÓRIO TXT
# ==========================================================
def gerar_relatorio_txt():

    if len(equipamentos) == 0:

        print(
            "\nNenhum equipamento cadastrado."
        )

        return

    try:

        tarifa = float(
            input(
                "\nInforme a tarifa "
                "(R$/kWh): "
            )
        )

    except ValueError:

        print(
            "\nValor inválido."
        )

        return

    try:

        with open(
            "relatorio_energetico.txt",
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(
                "RELATÓRIO ENERGÉTICO\n"
            )

            arquivo.write(
                "=" * 60 + "\n"
            )

            total_consumo = 0
            total_custo = 0

            for equipamento in equipamentos:

                custo = (
                    equipamento["consumo"]
                    * tarifa
                )

                total_consumo += (
                    equipamento["consumo"]
                )

                total_custo += custo

                arquivo.write(
                    f"\nEquipamento: "
                    f"{equipamento['nome']}\n"
                )

                arquivo.write(
                    f"Potência: "
                    f"{equipamento['potencia']} W\n"
                )

                arquivo.write(
                    f"Horas de uso: "
                    f"{equipamento['horas']} h/dia\n"
                )

                arquivo.write(
                    f"Consumo: "
                    f"{equipamento['consumo']:.2f} "
                    f"kWh/mês\n"
                )

                arquivo.write(
                    f"Classificação: "
                    f"{equipamento['classificacao']}\n"
                )

                arquivo.write(
                    f"Custo Mensal: "
                    f"R$ {custo:.2f}\n"
                )

            arquivo.write(
                "\n" + "=" * 60 + "\n"
            )

            arquivo.write(
                f"CONSUMO TOTAL: "
                f"{total_consumo:.2f} kWh/mês\n"
            )

            arquivo.write(
                f"CUSTO TOTAL: "
                f"R$ {total_custo:.2f}\n"
            )

        print(
            "\nRelatório gerado com sucesso!"
        )

        print(
            "Arquivo salvo como "
            "'relatorio_energetico.txt'"
        )

    except Exception as erro:

        print(
            f"\nErro: {erro}"
        )


# ==========================================================
# MENU PRINCIPAL
# ==========================================================
def menu():

    while True:

        print("\n")
        print("=" * 60)
        print(
            "SISTEMA DE AUDITORIA ENERGÉTICA"
        )
        print("=" * 60)

        print("1 - Cadastrar Equipamento")
        print("2 - Exibir Relatório")
        print("3 - Ranking de Consumo")
        print("4 - Gerar Relatório TXT")
        print("5 - Sair")

        opcao = input(
            "\nEscolha uma opção: "
        )

        if opcao == "1":

            cadastrar_equipamento()

        elif opcao == "2":

            exibir_relatorio()

        elif opcao == "3":

            ranking_consumo()

        elif opcao == "4":

            gerar_relatorio_txt()

        elif opcao == "5":

            print(
                "\nSistema encerrado."
            )

            break

        else:

            print(
                "\nOpção inválida."
            )


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================
menu()
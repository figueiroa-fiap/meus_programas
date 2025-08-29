# FarmTech Solutions - Agricultura Digital
import csv

# Listas (vetores) para armazenar dados
culturas = []
areas = []
insumos = []

def calcular_area(cultura):
    if cultura.lower() == "milho":
        largura = float(input("Digite a largura do terreno (m): "))
        comprimento = float(input("Digite o comprimento do terreno (m): "))
        return largura * comprimento
    elif cultura.lower() == "soja":
        base = float(input("Digite a base do terreno (m): "))
        altura = float(input("Digite a altura do terreno (m): "))
        return (base * altura) / 2
    else:
        print("Cultura não reconhecida.")
        return 0

def calcular_insumo():
    produto = input("Digite o nome do produto: ")
    dosagem = float(input("Digite a dosagem em mL/metro: "))
    ruas = int(input("Digite o número de ruas: "))
    comprimento = float(input("Digite o comprimento de cada rua (m): "))
    total_ml = dosagem * ruas * comprimento
    total_litros = total_ml / 1000
    return f"{produto} - Total necessário: {total_litros:.2f} litros"

def mostrar_dados():
    if not culturas:
        print("Nenhum dado cadastrado ainda.")
    else:
        for i in range(len(culturas)):
            print(f"{i+1}. Cultura: {culturas[i]} | Área: {areas[i]:.2f} m² | Insumo: {insumos[i]}")

def exportar_csv():
    if not culturas:
        print("Nenhum dado cadastrado ainda.")
        return
    with open("C:/Users/rfigu/Desktop/dados_fazenda.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Cultura", "Área", "Insumo"])
        for i in range(len(culturas)):
            writer.writerow([culturas[i], areas[i], insumos[i]])
    print("Dados exportados para CSV com sucesso em C:/Users/rfigu/Desktop/dados_fazenda.csv")

# Loop principal
while True:
    print("\n--- FarmTech Solutions ---")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cultura = input("Digite a cultura (Milho ou Soja): ")
        area = calcular_area(cultura)
        insumo = calcular_insumo()
        culturas.append(cultura)
        areas.append(area)
        insumos.append(insumo)
        print("Dados cadastrados com sucesso!")

    elif opcao == "2":
        mostrar_dados()
        exportar_csv()

    elif opcao == "3":
        mostrar_dados()
        idx = int(input("Digite o número do item que deseja atualizar: ")) - 1
        if 0 <= idx < len(culturas):
            cultura = input("Digite a nova cultura (Milho ou Soja): ")
            area = calcular_area(cultura)
            insumo = calcular_insumo()
            culturas[idx] = cultura
            areas[idx] = area
            insumos[idx] = insumo
            print("Dados atualizados com sucesso!")
        else:
            print("Índice inválido.")

    elif opcao == "4":
        mostrar_dados()
        idx = int(input("Digite o número do item que deseja deletar: ")) - 1
        if 0 <= idx < len(culturas):
            culturas.pop(idx)
            areas.pop(idx)
            insumos.pop(idx)
            print("Dados deletados com sucesso!")
        else:
            print("Índice inválido.")

    elif opcao == "5":
        print("Encerrando o programa. Até mais! 👋")
        break

    else:
        print("Opção inválida. Tente novamente.")

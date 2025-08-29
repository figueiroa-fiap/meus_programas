# =====================================================
# Script de inserção massiva de dados - para teste
# =====================================================

import csv
import random

# Quantidade de registros a gerar
NUM_REGISTROS = 50

# Caminho do CSV
CSV_PATH = "C:/Users/rfigu/Desktop/dados_fazenda.csv"

# Listas para armazenar dados
culturas = []
areas = []
insumos = []

# Opções de culturas
opcoes_culturas = ["Milho", "Soja"]

# Produtos de insumo possíveis
produtos = ["Fertilizante A", "Fertilizante B", "Herbicida C", "Inseticida D"]

# Gerar dados massivos
for _ in range(NUM_REGISTROS):
    cultura = random.choice(opcoes_culturas)

    # Gerar área aleatória dependendo da cultura
    if cultura == "Milho":
        largura = random.uniform(10, 100)  # metros
        comprimento = random.uniform(20, 200)
        area = largura * comprimento
    elif cultura == "Soja":
        base = random.uniform(5, 80)
        altura = random.uniform(10, 150)
        area = (base * altura) / 2

    produto = random.choice(produtos)
    dosagem = round(random.uniform(50, 500), 2)  # mL/metro
    ruas = random.randint(1, 10)
    comprimento_rua = random.uniform(50, 200)
    total_ml = dosagem * ruas * comprimento_rua
    total_litros = total_ml / 1000
    insumo = f"{produto} - Total necessário: {total_litros:.2f} litros"

    culturas.append(cultura)
    areas.append(area)
    insumos.append(insumo)

# Exportar CSV
with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Cultura", "Área", "Insumo"])
    for i in range(NUM_REGISTROS):
        writer.writerow([culturas[i], areas[i], insumos[i]])

print(f"{NUM_REGISTROS} registros de teste inseridos com sucesso em {CSV_PATH}")

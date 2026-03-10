from files import *
from datetime import datetime

def report_animals():
    animals = view_datas("animals.json")

    print("\nRELATÓRIO DE ANIMAIS")
    print(f"\n|{'ID':7} |{'NOME':10} |{'ESPÉCIE':8} |{'IDADE':10} |{'PESO':7} |{'STATUS':8}")
    print("-" * 80)

    for a in animals:
        id = a["animal_id"]
        name = a["name"]
        species = a["specie"]
        age = f"{a['age']} meses"
        status = f"{a['status']}"
        weight = f"{a['weight']}kg"

        print(f"|{id:<7} |{name:10} |{species:8} |{age:10} |{weight:7} |{status:8}")

def report_plants():
    plants = view_datas("plants.json")

    print("\nRELATÓRIO DE PLANTAÇÕES")
    print(f"\n|{'ID':7} |{'CULTURA':10} |{'ÁREA':8} |{'DATA DE PLANTIO':15} |{'DATA DE COLHEITA':15} |{'STATUS':8}")
    print("-" * 80)

    for p in plants:
        id = p["plantation_id"]
        crop_type = p["crop_type"]
        area = f"{p['area']}m²"
        planting_date = p["planting_date"]
        harvest_date = p["harvest_date"]
        status = f"{p['status']}"

        print(f"|{id:<7} |{crop_type:10} |{area:8} |{planting_date:15} |{harvest_date:15} |{status:8}")

def report_inputs():
    inputs = view_datas("inputs.json")

    print("\nRELATÓRIO DE INSUMOS")
    print(f"\n|{'ID':7} |{'NOME':15} |{'QUANTIDADE':12} |{'CATEGORIA':20}")
    print("-" * 80)

    for i in inputs:
        id = i["input_id"]
        name = i["name"]
        quantity = f"{i['quantity']} {i['unit']}"
        category = i["category"]

        print(f"|{id:<7} |{name:15} |{quantity:12} |{category:20}")

def report_movements():
    movements = view_datas("movements.json")

    print("\nRELATÓRIO DE MOVIMENTAÇÕES")
    print(f"\n|{'DATA':20} |{'TIPO':10} |{'ID':7} |{'AÇÃO':20} |{'NOVO VALOR':20}")
    print("-" * 80)

    for m in movements:
        date = m["date"]
        entity_type = m["type"]
        obj_id = m["id"]
        action = m["action"]
        new_value = str(m["new_value"])

        print(f"|{date:20} |{entity_type:10} |{obj_id:<7} |{action:20} |{new_value:20}")

def general_movements_report():
    print("\nRELATÓRIO GERAL")
    report_animals()
    report_plants()
    report_inputs()
    report_movements()
    key = input("\nPressione Enter para voltar ao menu...")

def general_report():
    animals = view_datas("animals.json")
    plantations = view_datas("plants.json")
    inputs = view_datas("inputs.json")

    report_lines = []

    report_lines.append("RELATÓRIO GERAL DA FAZENDA")
    report_lines.append(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 60)

    # ANIMAIS
    report_lines.append("\nANIMAIS")
    for a in animals:
        report_lines.append(
            f"ID: {a['animal_id']} | Nome: {a['name']} | Espécie: {a['specie']} | Status: {a['status']}"
        )

    # PLANTAÇÕES
    report_lines.append("\nPLANTAÇÕES")
    for p in plantations:
        report_lines.append(
            f"ID: {p['plantation_id']} | Cultura: {p['crop_type']} | Data de Plantio: {p['planting_date']} | Data de Colheita: {p['harvest_date']} | Status: {p['status']}"
        )

    # INSUMOS
    report_lines.append("\nINSUMOS")
    for i in inputs:
        report_lines.append(
            f"ID: {i['input_id']} | Nome: {i['name']} | Quantidade: {i['quantity']} {i['unit']}"
        )

    report_lines.append("\n" + "=" * 60)
    report_lines.append("TOTAIS")

    report_lines.append(f"Total de animais: {len(animals)}")
    report_lines.append(f"Total de plantações: {len(plantations)}")
    report_lines.append(f"Total de insumos: {len(inputs)}")

    report_text = "\n".join(report_lines)

    return report_text

def save_report():

    report_text = general_report()

    path = verify("report.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(report_text)

    print("\nRelatório salvo com sucesso!")


def reports_menu():
    while True:
        print("=" * 50)
        print(" " * 15 + "Relatórios" + " " * 15 )
        print("=" * 50)
        print("[1] Ver relatório geral\n[2] Salvar relatório geral\n[0] Voltar")

        asw = int(input(">>> "))

        match asw:
            case 0:
                break

            case 1:
                general_movements_report()

            case 2:
                print("ATENÇÂO: Esse relatorio não salva as movimentações," \
                "apenas os dados atuais de animais, plantações e insumos.")
                save_report()

            case _:
                print("Digite uma opção valida")
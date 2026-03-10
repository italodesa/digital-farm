from files import *

def report_animals():
    animals = view_datas("animals.json")

    print("\nRELATÓRIO DE ANIMAIS")
    print(f"\n|{'ID':7} |{'NOME':10} |{'ESPÉCIE':8} |{'IDADE':10} |{'PESO':7} |{'STATUS':8}")
    print("-" * 60)

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
    print(f"\n|{'ID':7} |{'NOME':10} |{'QUANTIDADE':12} |{'CATEGORIA':20}")
    print("-" * 60)

    for i in inputs:
        id = i["input_id"]
        name = i["name"]
        quantity = f"{i['quantity']} {i['unit']}"
        category = i["category"]

        print(f"|{id:<7} |{name:10} |{quantity:12} |{category:20}")

def general_report():
    print("\nRELATÓRIO GERAL")
    report_animals()
    report_plants()
    report_inputs()
    key = input("\nPressione Enter para voltar ao menu...")
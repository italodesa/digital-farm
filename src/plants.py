from files import *
from datetime import datetime, timedelta
from reports import report_plants
crops = {
    "milho": 120,
    "alface": 45,
    "soja": 110,
    "arroz": 130
}

class Plantation:
    def __init__(self,crop_type,area,planting_date,status,plantation_id=None,harvest_date=None):
        self.plantation_id = plantation_id # None sera calculado depois
        self.crop_type = crop_type
        self.area = area
        self.planting_date = planting_date
        self.harvest_date = harvest_date #None, sera calculado depois
        self.status = status

    def calculate_harvest(self):
    # convert ISO string to date
        planting_date = datetime.fromisoformat(self.planting_date)

        days = crops[self.crop_type]
        harvest_date = planting_date + timedelta(days=days)

        return harvest_date.date()

def create_plantation():
    crop_type = input("informe o tipo de cultura plantada (ex: “milho”, “soja”): ").strip().lower()
    area = float(input("informe o tamanho da área cultivada em hectares: "))
    planting_date = input("informe a data de plantio, registrada no formato YYYY-MM-DD")
    status = input("Situação atual da cultura (planted, harvested, rotated, inactive): ")

    path = verify("plants.json")
    plants_data = view_datas("plants.json")

    if plants_data:
        # Pega o maior ID e soma 1
        next_id = max(a['plantation_id'] for a in plants_data) + 1
    else:
        next_id = 1  # Primeiro ID

    
    plantation = Plantation(crop_type,area,planting_date,status)

    harvest_date = plantation.calculate_harvest()

    plantation.harvest_date = str(harvest_date)
    plantation.plantation_id = next_id

    plantation_dict = plantation.__dict__
    plants_data.append(plantation_dict)

    with open(path,"w",encoding="utf-8") as f:
        json.dump(plants_data, f, indent=4, ensure_ascii=False)

def view_plantations():
    plants_data = view_datas("plants.json")
    for plant_data in plants_data:
        print(f"{'Campo':<10} | {'Valor':<10}")
        print("-" * 22)
        for chave, valor in plant_data.items():
            print(f"{chave:<10} | {valor:<10}")
        print("\n")

def view_unic_plantation():
    plantation = recover_plantation()
    if plantation:
        print(f"{'Campo':<10} | {'Valor':<10}")
        print("-" * 22)
        for chave, valor in plantation.__dict__.items():
            print(f"{chave:<10} | {valor:<10}")
    else:
        print("Plantação não encontrada.")

def recover_plantation():
    name = input("informe o tipo de cultura plantada: ")
    id = int(input("informe o id da plantação:"))
    plantations_data = view_datas("plants.json")
    plantation_dict = None

    for plantation in plantations_data:
        if plantation["crop_type"] == name or plantation["plantation_id"] == id:
            plantation_dict = plantation

    if plantation_dict:
        plantation = Plantation(
            plantation_dict["crop_type"],
            plantation_dict["area"],
            plantation_dict["planting_date"],
            plantation_dict["status"]
        )
        plantation.plantation_id = plantation_dict["plantation_id"]
        plantation.harvest_date = plantation_dict["harvest_date"]

        return plantation
    
    
# Em modificação
    
def delete_plantation(id):
    all_plants = view_datas("plants.json")
    path = verify("plants.json")
    
    for plantation in all_plants:
        if plantation["plantation_id"] == id:
            all_plants.remove(plantation)
            break
        else:
            print("Plantação não encontrada.")

    with open(path,"w",encoding="utf-8") as f:
              json.dump(all_plants, f, indent=4, ensure_ascii=False)

def update_plantation(atribute):
    path = verify("plants.json")

    plantation = recover_plantation()
    id = plantation.plantation_id

    delete_plantation(id)

    all_plants = view_datas("plants.json")

    valor = input(f"Informe o novo valor para {atribute}: ")

    setattr(plantation, atribute, valor)

    if atribute == "crop_type":
        harvest_date = plantation.calculate_harvest()
        plantation.harvest_date = str(harvest_date)

    plantation_dict = plantation.__dict__
    all_plants.append(plantation_dict)

    with open(path,"w",encoding="utf-8") as f:
        json.dump(all_plants, f, indent=4, ensure_ascii=False)

    print("plantação atualizada com sucesso!")

def update_plantation_menu():
    while True:
        try:
            print("=" * 50)
            print(" " * 15 + "Atualização de plantações" + " " * 15 )
            print("=" * 50)

            print("[1] Atualizar tipo de cultura\n[2] Atualizar área\n[3] Atualizar data de plantio\n"
            "[4] Atualizar status\n[0] voltar")

            asw = int(input(">>> "))

            match asw:
                case 0:
                    break
            
                case 1:
                    update_plantation("crop_type")

                case 2:
                    update_plantation("area")

                case 3:
                    update_plantation("planting_date")

                case 4:
                    update_plantation("status")

                case _:
                    print("Digite uma opção valida")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Certifique-se de que os dados foram inseridos corretamente e tente novamente.")

def plants_menu():
    while True:
        print("=" * 50)
        print(" " * 15 + "Sistema de plantações" + " " * 15 )
        print("=" * 50)

        print("[1] Criar plantação\n[2] Listar plantações\n[3] Atualizar status\n"
        "[4] Remover plantação\n[5] Relatorios de plantação\n[6] Registro de movimentação\n"
        "[7] Buscar plantações\n[0] voltar")

        asw = int(input(">>> "))

        match asw:
            case 0:
                break
        
            case 1:
                try:
                    create_plantation()
                except Exception as e:
                    print(f"Ocorreu um erro ao criar a plantação: {e}")
                    print("Certifique-se de que os dados foram inseridos corretamente e tente novamente.")

            case 2:
                view_plantations()

            case 3:
                update_plantation_menu()

            case 4:
                try:
                    id = int(input("informe o id da plantação a ser removida: "))
                    delete_plantation(id)
                except Exception as e:
                    print(f"Ocorreu um erro ao remover a plantação: {e}")
                    print("Certifique-se de que os dados foram inseridos corretamente e tente novamente.")

            case 5:
                report_plants()

            case 6:
                print("Em desenvolvimento")

            case 7:
                try:
                    view_unic_plantation()
                except Exception as e:
                    print(f"Ocorreu um erro ao buscar a plantação: {e}")
                    print("Certifique-se de que os dados foram inseridos corretamente e tente novamente.")

            case _:
                print("Digite uma opção valida")
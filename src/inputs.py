# inputs = insumos
import json
from files import * 

class Input:

    def __init__(self,name,quantity,unit,category,input_id=None):
        self.input_id = input_id

        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category

    def add_stock(self, amount):
        self.quantity += amount
        print(f"Estoque de {self.name} atualizado. Nova quantidade: {self.quantity}")

    def remove_stock(self, amount):
        if amount > self.quantity:
            print("Quantidade insuficiente em estoque.")
        else:
            self.quantity -= amount
            print(f"Estoque de {self.name} atualizado. Nova quantidade: {self.quantity}")

def create_input():
    name = input("Informe o nome do insumo: ")
    quantity = float(input("Informe a quantidade do insumo: "))
    unit = input("Informe a unidade de medida do insumo: ")
    category = input("Informe a categoria do insumo (ex: feed, fertilizer, seed, etc.): ")

    path = verify("inputs.json")
    inputs_data = view_datas("inputs.json")

    if inputs_data:
        # Pega o maior ID e soma 1
        next_id = max(a['input_id'] for a in inputs_data) + 1
    else:
        next_id = 1  # Primeiro ID


    input_obj = Input(name,quantity,unit,category)
    input_obj.input_id = next_id

    input_dict = input_obj.__dict__
    inputs_data.append(input_dict)

    with open(path,"w",encoding="utf-8") as f:
        json.dump(inputs_data, f, indent=4, ensure_ascii=False)

def view_inputs():
    inputs_data = view_datas("inputs.json")
    for input_data in inputs_data:
        print(f"{'Campo':<10} | {'Valor':<10}")
        print("-" * 22)
        for chave, valor in input_data.items():
            print(f"{chave:<10} | {valor:<10}")
        print("\n")

def view_unic_input():
    input_obj = recover_input()
    if input_obj:
        print(f"{'Campo':<10} | {'Valor':<10}")
        print("-" * 22)
        for chave, valor in input_obj.__dict__.items():
            print(f"{chave:<10} | {valor:<10}")
    else:
        print("Insumo não encontrado.")

def delete_input(id):

    inputs_data = view_datas("inputs.json")
    input_to_delete = None

    for inputt in inputs_data:
        if inputt["input_id"] == id:
            input_to_delete = inputt
            break

    if input_to_delete:
        inputs_data.remove(input_to_delete)
        path = verify("inputs.json")
        with open(path,"w",encoding="utf-8") as f:
            json.dump(inputs_data, f, indent=4, ensure_ascii=False)
        print("Insumo deletado com sucesso.")
    else:
        print("Insumo não encontrado.")

def recover_input():
    name = input("Informe o nome do insumo: ")
    id = int(input("Informe o ID do insumo: "))
    inputs_data = view_datas("inputs.json")
    input_dict = None

    for inputt in inputs_data:
        if inputt["name"] == name or inputt["input_id"] == id:
            input_dict = inputt
            break

    if input_dict:
        input_obj = Input(
            input_dict["name"],
            input_dict["quantity"],
            input_dict["unit"],
            input_dict["category"]
        )
        input_obj.input_id = input_dict["input_id"]
        return input_obj
    else:
        print("Insumo não encontrado.")
        return None
    
def update_input(atribute):
    path = verify("inputs.json")

    input_obj = recover_input()
    if not input_obj:
        return print("Insumo não encontrado.")

    delete_input(input_obj.input_id)

    all_inputs = view_datas("inputs.json")

    valor = input(f"Informe o novo valor para {atribute}: ")

    setattr(input_obj, atribute, valor)


    input_obj_dict = input_obj.__dict__
    all_inputs.append(input_obj_dict)

    with open(path,"w",encoding="utf-8") as f:
        json.dump(all_inputs, f, indent=4, ensure_ascii=False)

    print("insumo atualizado com sucesso!")

def update_input_menu():
    while True:
        try:
            print("=" * 50)
            print(" " * 15 + "Atualização de insumos" + " " * 15 )
            print("=" * 50)

            print("[1] Atualizar nome\n[2] Atualizar a unidade de medida \n"
            "[3] Atualizar categoria\n[0] voltar")

            asw = int(input(">>> "))

            match asw:
                case 0:
                    break

                case 1:
                    update_input("name")

                case 2:
                    update_input("unit")

                case 3:
                    update_input("category")

                case _:
                    print("Digite uma opção valida")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Certifique-se de que os dados foram inseridos corretamente e tente novamente.")

def add_input_stock():
    input_obj = recover_input()
    quantity = float(input("Informe a quantidade a ser adicionada: "))
    if input_obj:
            input_obj.add_stock(quantity)
    else:
        print("Insumo não encontrado.")

def remove_input_stock():
    input_obj = recover_input()
    quantity = float(input("Informe a quantidade a ser removida: "))
    if input_obj:
        input_obj.remove_stock(quantity)
    else:
        print("Insumo não encontrado.")

def input_menu():
    while True:
        print("=" * 50)
        print(" " * 15 + "Sistema de Insumos" + " " * 15 )
        print("=" * 50)

        print("[1] Criar insumo\n[2] Listar insumos\n[3] Atualizar informações do insumo\n"
        "[4] Remover insumo\n[5] Adicionar estoque\n[6] Retirar estoque\n"
        "[7] Buscar insumos\n[0] Voltar")

        asw = int(input(">>> "))

        match asw:
            case 0:
                break
                
            case 1:
                create_input()

            case 2:
                view_inputs()

            case 3:
                update_input_menu()

            case 4:
                id = int(input("Informe o ID do insumo a ser deletado: "))
                delete_input(id)

            case 5:
                add_input_stock()

            case 6:
                remove_input_stock()

            case 7:
                view_unic_input()
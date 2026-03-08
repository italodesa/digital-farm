
import json
from utils import verify,view_datas

class Animal:

    def __init__(self,name,specie,age,weight,status='active', animal_id=None):
        self.animal_id = animal_id

        self.name = name
        self.specie = specie
        self.age = age
        self.weight = weight
        self.status = status

    def inspect_animal(self):
        return f"ID: {self.animal_id}\nESPECIE: {self.specie}\nIDADE: {self.age}\nPESO: {self.weight}\nSTATUS: {self.status}"


    def update_animal(self):
    
        path = verify("animals.json")
        print("o que deseja alterar?")
        print("[1] nome\n[2] especie\n[3] idade\n[4] peso\n[5] status\n[6] Sair")

        try:
            asnw = int(input(">>> "))

            match asnw:

                case 1:
                    id = self.animal_id
                    delete_animal(id)

                    all_animals = view_datas("animals.json")

                    new_name = input("informe o novo nome: ")
                    self.name = new_name

                    animal_dict = self.__dict__
                    all_animals.append(animal_dict)

                    with open(path,"w",encoding="utf-8") as f:
                        json.dump(all_animals, f, indent=4, ensure_ascii=False)
                    print("especie atualizada com sucesso!")

                case 2:
                    id = self.animal_id
                    delete_animal(id)

                    all_animals = view_datas("animals.json")

                    new_specie = input("informe a nova especie: ")
                    self.specie = new_specie

                    animal_dict = self.__dict__
                    all_animals.append(animal_dict)

                    with open(path,"w",encoding="utf-8") as f:
                        json.dump(all_animals, f, indent=4, ensure_ascii=False)
                    print("especie atualizada com sucesso!")

                case 3:
                    id = self.animal_id
                    delete_animal(id)

                    all_animals = view_datas("animals.json")

                    new_age = int(input("informe a nova idade: "))
                    self.age = new_age

                    animal_dict = self.__dict__
                    all_animals.append(animal_dict)

                    with open(path,"w",encoding="utf-8") as f:
                        json.dump(all_animals, f, indent=4, ensure_ascii=False)

                    print("idade atualizada com sucesso!")

                case 4:
                    id = self.animal_id
                    delete_animal(id)

                    all_animals = view_datas("animals.json")

                    new_weight = float(input("informe o novo peso: "))
                    self.weight = new_weight

                    animal_dict = self.__dict__
                    all_animals.append(animal_dict)

                    with open(path,"w",encoding="utf-8") as f:
                        json.dump(all_animals, f, indent=4, ensure_ascii=False)

                    print("peso atualizado com sucesso!")

                case 5:
                    id = self.animal_id
                    delete_animal(id)

                    all_animals = view_datas("animals.json")

                    new_status = input("informe o novo status: ")
                    self.status = new_status

                    animal_dict = self.__dict__
                    all_animals.append(animal_dict)

                    with open(path,"w",encoding="utf-8") as f:
                        json.dump(all_animals, f, indent=4, ensure_ascii=False)
                    print("status atualizado com sucesso!")

                case 6:
                    pass

                case _:
                    print("digite uma opção valida")

        except Exception as e:
            print(f"ocorreu um erro: {e}")



def create_animal():
# Função que cria um animal na fazenda
        name = input("Digite um nome para o animal: ")
        specie = input("Digite a especie do animal: ")
        age = int(input("Digite a idade do animal (em meses): "))
        weight = float(input("Digite o peso do animal (em kilos):"))
        status = input("Digite o status do animal (active, sold ou death)")

        
       
        
        path = verify("animals.json")
        animals_data = view_datas("animals.json")

        if animals_data:
        # Pega o maior ID e soma 1
            proximo_id = max(a['animal_id'] for a in animals_data) + 1
        else:
            proximo_id = 1  # Primeiro animal

        animal = Animal(name,specie,age,weight,status)
        animal.animal_id = proximo_id

        animal_dict = animal.__dict__
        

        animals_data.append(animal_dict)


        
        with open(path,"w",encoding="utf-8") as f:
              json.dump(animals_data, f, indent=4, ensure_ascii=False)

def view_all_animals():
    animals_data = view_datas("animals.json")
    for animal in animals_data:
        print(animal)

def recover_animal():
    name = input("informe o nome do animal")
    id = int(input("informe o id "))
    animals_data = view_datas("animals.json")
    animal_dict = None

    for animal in animals_data:
        if animal["name"] == name or animal["animal_id"] == id:
            animal_dict = animal

    if animal_dict:
        animal = Animal(
            animal_dict["name"],
            animal_dict["specie"],
            animal_dict["age"],
            animal_dict["weight"],
            animal_dict["status"]
        )

        animal.animal_id = animal_dict["animal_id"]

        return animal
    
def delete_animal(id):
    all_animals = view_datas("animals.json")
    path = verify("animals.json")
    
    for animal in all_animals:
        if animal["animal_id"] == id:
            all_animals.remove(animal)

    with open(path,"w",encoding="utf-8") as f:
              json.dump(all_animals, f, indent=4, ensure_ascii=False)

    
def view_animal():
    animal = recover_animal()
    print(animal.inspect_animal())

def update_animal():
    animal = recover_animal()
    animal.update_animal()
    
def animals_menu():
    while True:
        print("=" * 50)
        print(" " * 15 + "Animais" + " " * 15 )
        print("=" * 50)
        print("[1] cadastrar animal\n[2] Registrar movimentação\n[3] relatorio \n[4] Pesquisar\n[0] voltar")
        asw = int(input(">>> "))

        match asw:
            case 0:
                break
        
            case 1:
                create_animal()

            case 2:
                update_animal()

            case 3:
                view_all_animals()

            case 4:
                view_animal()

            case _:
                print("Digite uma opção valida")
from animals import animals_menu
from plants import plants_menu
from files import clear
from inputs import input_menu
from reports import reports_menu

while True:
    clear()
    
    print("=" * 50)
    print(" " * 15 + "fazenda digital" + " " * 15 )
    print("=" * 50)
    print("[1] Animais\n[2] Plantações\n[3] Insumos \n[4] Relatório geral\n[0] Encerrar")
    try:
        asw = int(input(">>> "))

        match asw:
            case 0:
                break

            case 1:
                animals_menu()

            case 2:
                plants_menu()

            case 3:
                input_menu()

            case 4:
                reports_menu()

            case _:
                print("Digite uma opção valida")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
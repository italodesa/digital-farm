from animals import *
from plants import *
from files import clear

while True:
    clear()
    
    print("=" * 50)
    print(" " * 15 + "fazenda digital" + " " * 15 )
    print("=" * 50)
    print("[1] Animais\n[2] Plantações\n[3] Insumos \n[4] relatorio geral\n[0] encerrar")
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
                pass

            case 4:
                pass

            case _:
                print("Digite uma opção valida")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
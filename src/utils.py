from pathlib import Path
import json

def verify(path):
# Função para verificação de arquivos

        # variaveis que vão receber os caminhos dos arquivos
        DATA_DIR = Path("data")
        DATA_FILE = DATA_DIR / path

        #criar a pasta data caso ela não exista
        DATA_DIR.mkdir(exist_ok=True)

        #criar o arquivo caso ele não exista na pasta
        if not DATA_FILE.exists():
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                   json.dump([], f)
        
        #retorna o caminho do arquivo
        return DATA_FILE

def view_datas(a_path):
# Função que retorna o conteudo do arquivo argumentado

    path = verify(a_path)

    with open(path,"r",encoding="utf-8") as f:
            all_data = json.load(f)

    return all_data



              



      


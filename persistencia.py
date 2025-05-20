import json
from typing import List
from io import TextIOWrapper


# Funções para manipular o arquivo de compras
def gravar_compra(ficheiro_compras: str, compras: List[dict]) -> None:
    with open(ficheiro_compras, "w", encoding="utf-8") as file:
        assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
        json.dump(compras, file, ensure_ascii=False)

def carregar_compras(ficheiro_compras: str) -> List[dict]:
    try:
        with open(ficheiro_compras, "r", encoding="utf-8") as file:
            assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
            conteudo = file.read()
            if conteudo.strip():
                compras = json.loads(conteudo)
                return compras
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro de compras. O formato do arquivo pode estar corrompido.")
        return []

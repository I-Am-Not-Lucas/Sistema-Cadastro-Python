# Create, Read, Update, Delate
from datetime import date

def cria_arquivo() -> None:
    try:
        with open("Alunos.txt", "w+") as file:
            print()
    except Exception as e: 
        print(e)

def saudacao() -> None:
    texto = "Bem vindo ao sistema de cadastro versão 1.0"

    print('*' * len(texto))
    print(texto)
    print('*' * len(texto))

def mostra_opcoes() -> str: 
    print("[1] - Cadastrar Aluno")  
    print("[2] - Deletar Aluno")
    print("[3] - Atualizar dados de Aluno")
    print("[4] - Mostrar Aluno")
    print()

    opcao_escolhida = input(str(">>"))

    return opcao_escolhida

def chama_crud(string) -> None:

    match string:

        case "1":
            cadastro()

        case "2":
            deleta_aluno()

        case "3":
            atualiza_aluno()

        case "4":
            mostra_alunos()

        case _:
            "Opção inválida ou não funcional"


def cadastro():
    #Create
    print("Cadastro de novo aluno")

    data_pc = date.today()

    id = 0
    nome = input(str("nome: "))
    data_nascimento = input(str("Data de nascimento ( padrão dd/mm/aaaa): "))
    data_inscricao = f'{data_pc.day}/{data_pc.month}/{data_pc.year}'
    telefone = input(str("Telefone: "))

    dicionario =  {
        'id' : id,
        'Nome': nome,
        'data de inscrição': data_inscricao,
        'Data de nascimento': data_nascimento,
        'Telefone': telefone

    }
    

    with open("Alunos.txt", "w+") as file:
        file.write(str(dicionario))

def deleta_aluno():
    #Delete
    ...
def atualiza_aluno():
    #Update
    ...    
def mostra_alunos():
    #Read
    ...


if __name__ == "__main__":
    cadastro()
import ujson as json


def save_to_database(data: dict, database_path: str):
    with open(database_path, "w") as file:
       json.dump(data, file, indent=4)
    return None
    ## Crie uma lógica que faça com que os dados recebidos através do parâmetro data sejam persistidos no data.json com indentação de 4 espaços.
    ## Return none


def read_database(database_path: str):
    with open(database_path, 'r') as file:
        lista = json.load(file)
        print(lista)
        return lista
    ## Crie uma lógica onde, ao receber o parâmetro database_path, a função fará a leitura do arquivo data.json e retornará todos os usuários salvos
    ## Um dicionário com a chave users tendo como valor a lista dos dicionários dos usuários.
    #     {
    #   "users": [
    #       {
    #           "name": "Gilberto",
    #           "class": 20,
    #           "facilitator": "Chrystian",
    #           "email": "gilberto@mail.com"
    #       },
    #       ...
    #   ]
    # }

def register_students(data: dict):
    ...
    ## registrar estudante na lista
    ## se o email ja for utilizado retornar"email informado em uso. tente outro' se bem sucedido none


def get_studentes():
    ## retorna a lista de alunos registrados juntamente com o numero total de estudantes que estao registrados
    ## { users = [], total_students_number :   }
    ...
    
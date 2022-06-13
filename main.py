import ujson as json

from users.functions import read_database

## teste path
databasePath = './database/data.json'
## test dict
people = {'name':'Paulo', 'age': 31, 'gender':'male'}

def main():
    ## TESTES
    #read_database(databasePath)
    # list = []
    # with open(databasePath,'r') as file:
    #     list = json.load(file)
    #     print(list, 'dentro do with')
    # list['users'].append(people)
    # print(list, 'depois do with')
    # with open(databasePath, 'w') as file:
    #     json.dump(list, file, indent=4)
    ...

if __name__ == '__main__':
    main()




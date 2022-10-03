from tokenize import Name
from fastapi import FastAPI
from datetime import date

app = FastAPI()

menu = [
    {   'id': 1,
        'name': 'admin'
     },
    {
        'id': 2,
        'name': 'user',
        'cpf' : '123.456.789-10'
        'horario': '00-00-00 00:00:00'
    }
]

#@app.get("/")
#def hello_world_root():
#    return {"Hello": "World"}

my_date = date.today()
my_date = my_date.strftime("%d%m%Y %H:%M:%S")


@app.get('/get-item/{item_id}')
def get_item(
    item_id: int = Path(
        None,
        description="Insira o ID do usuário que deseja ver - 1 Admin / 2 User")):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Error': 'Usuário não existente'}

    return {'Item': search[0]}


@app.get('/get-by-name')
def get_item(name: Optional[str] = None):

    print("Busque por nome, sendo 1 - Admin e 2 - User")
    search = list(filter(lambda x: x["name"] == name, menu))

    if search == []:
        return {'item': 'Does not exist'}

    return {'Item': search[0]}


@app.get('/list-menu')
def list_menu():
    return {'Menu': menu}


@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item, name: str, item_name: Name, cpf : int, item_cpf: cpf, item_data: int, data: horario):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search != []:
        return {'Error': 'Item já possui registro'}

    item = item.dict()
    item['id'] = item_id
    item['name'] = item_name
    item['cpf'] = item_cpf
    my_date = date.today()
    my_date = my_date.strftime("%d%m%Y %H:%M:%S")
    item['horario'] = my_date

    menu.append(item)
    print("Item adicionado com sucesso")
    return item


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: Item, name: str, item_name: Name, cpf : int, item_cpf: cpf, item_data: int, data: horario):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Item': 'Não existente'}

    if item.id == search:
        search[0]['name'] = item.name
        search[0]['cpf'] = item.cpf
        search[0]['data'] = my_date

    return search


@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):
    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Item': 'Não existente'}

    for i in range(len(menu)):
        if menu[i]['id'] == item_id:
            del menu[i]
            break
    return {'Message': 'Item excluido com sucesso'}
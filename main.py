import sys
clients = [
    {
        'name': 'as',
        'company': "Google",
        "email": "pablo@.com",
        "position": "software engineer"
    },
    {
        'name': 'Ricardo',
        'company': "Facebook",
        "email": "ricardo@.com",
        "position": "Data engineer"
    }
]

print(type(clients))


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('what is the client {}?'.format(field_name))
    return field


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print("client already is in the client\'s list")


def search_client(client_name):
    for Client in clients:
        if Client['name'] != client_name:
            continue
        else:
            b = list(Client)
            print(type(b))
            list_clients(b)
            return True


def list_clients(clientsT=None):
    if not clientsT:
        clientsT = clients

    for idx, client in enumerate(clientsT):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_name, update_client_name):
    for idx, client in enumerate(clients):
        if client['name'] != client_name:
            continue
        else:
            clients[idx] = update_client_name
            return True


def delete_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client_name in client['name']:
            del clients[idx]
            break


def _print_welcome():
    print("Welcome to Platzi Ventas")
    print("*" * 5)
    print('what would you like to do today?')
    print("[C]create client")
    print("[U]update client")
    print("[D]delete client")
    print("[S]earch client")
    print("[L]ist clients")


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('what is the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name


def _get_client_diccionary():
    return {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        "email": _get_client_field('email'),
        "position": _get_client_field('position'),
    }


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()

    if command == "C":
        client = _get_client_diccionary()
        create_client(client)
        list_clients()

    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == "L":
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print("the client is in the client\'s list")
            update_clientt = _get_client_diccionary()
            update_client(client_name, update_clientt)
            list_clients()
        else:
            print('the client: {} is not in our client\'s list'.format(client_name))

    elif command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print("the client is in the client\'s list")
        else:
            print('the client: {} is not in our client\'s list'.format(client_name))

    else:
        print('Invalid command')

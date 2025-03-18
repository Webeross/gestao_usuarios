from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes
 
    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET) - Renderizar o forumulário para criar um cliente
    - /clientes/<id> (GET) - Obter dados de um cliente
    - /clientes/<id>/edit (GET) - Renderizar o forumulário para criar um cliente
    - /clientes/<id>/update (PUT) - Atualizar os dados de um cliente
    - /clientes/<id>/delete (DELETE) - Deleta registro de usuário

"""

@cliente_route.route('/')
def lista_clientes():
    """ Listar os clientes"""
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados de um cliente"""

    data = request.json
    
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }

    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    """Formulário para cadastrar um cliente"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """Formulário para cadastrar um cliente"""
    render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """Formulário para editar um cliente"""
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """Atualizar informações de um cliente"""
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    """Deletar informações de um cliente"""
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
    return {'deleted': 'ok'}

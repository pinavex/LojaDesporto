from flask import Flask, request, jsonify, render_template, redirect, session
from cliente import Cliente


app = Flask(__name__, template_folder='templates')

lista_clientes = []

@app.route('/')
def index():
    return render_template('kona.html', clientes=lista_clientes)

@app.route('/clientes', methods=['GET'])
def get_clientes():
    return jsonify([cliente.__dict__ for cliente in lista_clientes])

@app.route('/new_client', methods=['POST'])
def new_client():
    try:
        data = request.get_json()
        nif = data.get('nif')
        nome = data.get('nome')
        telefone = data.get('telefone')

        if not nif or not nome or not telefone:
            return jsonify({'error': 'Faltam informações obrigatórias'}), 400

        novo_cliente = Cliente(nif, nome, telefone)
        lista_clientes.append(novo_cliente)

        return jsonify({'message': 'Cliente adicionado com sucesso!', 'cliente': novo_cliente.__dict__}), 201
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

@app.route('/remove_client', methods=['DELETE'])
def remove_client():
    try:
        data = request.get_json()
        nif = data.get('nif')
        if not nif:
            return jsonify({'error': 'NIF não fornecido'}), 400

        global lista_clientes
        lista_clientes = [cliente for cliente in lista_clientes if cliente.nif != nif]

        return jsonify({'message': 'Cliente removido com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)


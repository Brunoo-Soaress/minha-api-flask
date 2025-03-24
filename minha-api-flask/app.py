from flask import Flask, jsonify, request

# Inicializando o Flask
app = Flask(__name__)

# Dados estáticos (lista de filmes)
filmes = [
    {"id": 1, "titulo": "O Poderoso Chefão", "descricao": "Um clássico do cinema."},
    {"id": 2, "titulo": "Interestelar", "descricao": "Ficção científica sobre viagem no espaço."},
    {"id": 3, "titulo": "Cidade de Deus", "descricao": "Drama brasileiro sobre a vida no Rio de Janeiro."}
]

# Rota raiz
@app.route('/')
def index():
    return "Olá, bem-vindo à minha API!"

# Rota para listar todos os filmes e adicionar um novo filme
@app.route('/filmes', methods=['GET', 'POST'])
def listar_filmes():
    if request.method == 'POST':
        novo_filme = request.json
        if not novo_filme or not 'titulo' in novo_filme or not 'descricao' in novo_filme:
            return jsonify({"mensagem": "Dados inválidos"}), 400

        novo_filme['id'] = len(filmes) + 1
        filmes.append(novo_filme)
        return jsonify(novo_filme), 201
    else:
        return jsonify(filmes)

# Rota para buscar um filme por ID
@app.route('/filmes/<int:id>', methods=['GET'])
def buscar_filme(id):
    filme = next((f for f in filmes if f['id'] == id), None)
    if filme:
        return jsonify(filme)
    else:
        return jsonify({"mensagem": "Filme não encontrado"}), 404

# Iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)
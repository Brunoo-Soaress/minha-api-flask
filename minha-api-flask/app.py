from flask import Flask, jsonify

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

# Rota para listar todos os filmes
@app.route('/filmes', methods=['GET'])
def listar_filmes():
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
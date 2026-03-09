from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Juan", "correo": "juan@email.com"},
    {"id": 2, "nombre": "Maria", "correo": "maria@email.com"},
    {"id": 3, "nombre": "Carlos", "correo": "carlos@email.com"}
]

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/usuarios")
def ver_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config["SECRET_KEY"]


def get_db_connection():
    conexion = sqlite3.connect(app.config["DATABASE"])
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla_usuarios():
    conexion = get_db_connection()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


crear_tabla_usuarios()


# ---------------- VALIDACIONES BACKEND ----------------

def validar_nombre(nombre):
    # Mínimo 3 caracteres, solo letras y números
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9]{3,}", nombre) is not None


def validar_email(email):
    # Formato básico de email válido
    return re.fullmatch(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email) is not None


def validar_password(password):
    # Mínimo 6 caracteres, solo letras y números
    return re.fullmatch(r"[A-Za-z0-9]{6,}", password) is not None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conexion = get_db_connection()

        usuario = conexion.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        conexion.close()

        if usuario and check_password_hash(usuario["password"], password):

            session["usuario_id"] = usuario["id"]
            session["usuario_nombre"] = usuario["nombre"]
            session["usuario_email"] = usuario["email"]

            return redirect(url_for("dashboard"))

        return render_template( "login.html",
        error= "Las credenciales no son correctas. Revisa tu correo y contraseña."
        )
    
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        nombre = request.form["nombre"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]
        confirm_password = request.form["confirmPassword"]

        # Validaciones de seguridad en servidor
        if not validar_nombre(nombre):
            return "Error: el nombre debe tener mínimo 3 caracteres y solo letras o números."

        if not validar_email(email):
            return "Error: el email no es válido."

        if not validar_password(password):
            return "Error: la contraseña debe tener mínimo 6 caracteres y solo letras o números."

        if password != confirm_password:
            return "Error: las contraseñas no coinciden."

        password_hash = generate_password_hash(password)

        conexion = get_db_connection()

        try:
            conexion.execute("""
                INSERT INTO users (nombre, email, password)
                VALUES (?, ?, ?)
            """, (nombre, email, password_hash))

            conexion.commit()

        except sqlite3.IntegrityError:
            conexion.close()
            return "Error: el email ya existe."

        conexion.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
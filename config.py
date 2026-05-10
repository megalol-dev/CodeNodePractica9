import os

# Clase de configuración principal
class Config:

    # Clave secreta para manejar sesiones en Flask
    SECRET_KEY = os.environ.get("SECRET_KEY") or "clave_super_secreta"

    # Ruta de la base de datos SQLite
    DATABASE = "database/users.db"
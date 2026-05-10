# WoW Auth - Flask Login System

Proyecto realizado con Flask simulando una pantalla de login inspirada en videojuegos tipo MMORPG / World of Warcraft.

El proyecto incluye:

- Sistema de registro y login
- Validaciones frontend con JavaScript
- Protección de rutas privadas mediante sesiones
- Dashboard privado
- Animaciones visuales tipo videojuego
- Sistema de capas visuales
- Diseño responsive para PC y móvil

---

# Tecnologías usadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Git / GitHub

---

# Funcionalidades principales

## Registro de usuarios

El usuario puede crear una cuenta mediante:

- Nombre
- Email
- Contraseña
- Confirmación de contraseña

### Validaciones implementadas

### Nombre
- Mínimo 3 caracteres
- Solo letras y números

### Email
- Validación mediante expresiones regulares

### Contraseña
- Mínimo 6 caracteres
- Letras y números permitidos

### Confirmación de contraseña
- Debe coincidir con la contraseña original

Las validaciones se realizan:

- En tiempo real mediante JavaScript
- También en backend con Flask para mayor seguridad

---

# Login

El sistema permite iniciar sesión mediante:

- Email
- Contraseña

Las contraseñas se almacenan usando:

```python
generate_password_hash()
```

y se validan mediante:

```python
check_password_hash()
```

Esto evita guardar contraseñas en texto plano.

---

# Sistema de sesiones

Se utiliza:

```python
session
```

para mantener autenticado al usuario.

Las rutas privadas como:

```txt
/dashboard
```

solo pueden abrirse si existe una sesión activa.

En caso contrario Flask redirige automáticamente al login.

---

# Dashboard privado

El dashboard muestra:

- Nombre del usuario
- Email
- Botón de cerrar sesión

---

# Animación principal del Index

La pantalla principal utiliza un sistema de capas inspirado en motores gráficos de videojuegos.

---

## Sistema de capas

### Capa 1 - Fondo animado

```txt
fondoCastillo.png
```

Es una textura animada que se desplaza continuamente de derecha a izquierda usando:

```css
@keyframes
```

y:

```css
transform: translateX()
```

---

### Capa 2 - Dragón animado

```txt
dragon.png
```

El dragón utiliza un sistema de sprite sheet.

Todos los frames están dentro de un único PNG horizontal.

Cada frame tiene el mismo tamaño y posición.

La animación funciona modificando:

```css
background-position
```

para mostrar cada frame en orden:

```txt
1 → 2 → 3 → 4 → 5 → 4 → 3 → 2 → 1
```

Esto crea el efecto de vuelo del dragón.

Además el dragón se desplaza por pantalla usando otra animación independiente.

---

### Capa 3 - Castillo

```txt
castillo.png
```

El castillo se pinta encima del dragón mediante:

```css
z-index
```

Esto permite crear profundidad visual.

---

# Responsive Design

El proyecto utiliza distintas imágenes para:

- PC
- Móvil

Esto se realiza mediante:

```css
@media
```

porque la proporción horizontal y vertical cambia mucho entre dispositivos.

---

# Estructura del proyecto

```txt
practica9/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── database/
│   └── users.db
│
├── static/
│   ├── css/
│   │   └── estilo.css
│   │
│   ├── js/
│   │   └── validaciones.js
│   │
│   └── img/
│       ├── fondo1.png
│       ├── fondoCastillo.png
│       ├── fondoCastilloPC.png
│       ├── castillo.png
│       ├── castilloPC.png
│       └── dragon.png
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── perfil.html
│
└── venv/
```

---

# Ejecutar el proyecto

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar Flask

```bash
python app.py
```

Abrir:

```txt
http://127.0.0.1:5000
```

---

# Autor

Proyecto realizado por:

```txt
José Luis Escudero Polo
```

Como práctica de Flask + Frontend UI inspirado en videojuegos.

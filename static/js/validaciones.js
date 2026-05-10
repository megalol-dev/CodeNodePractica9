// ---------------- VALIDACIONES ----------------

function validarNombre() {
    const nombre = document.getElementById("nombre");
    const error = document.getElementById("nombreError");

    if (!nombre) return true;

    const regex = /^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9]{3,}$/;

    if (!regex.test(nombre.value.trim())) {
        error.textContent = "Nombre inválido: mínimo 3 caracteres, solo letras y números.";
        error.style.color = "red";
        return false;
    }

    error.textContent = "Nombre válido";
    error.style.color = "green";
    return true;
}


function validarEmail() {
    const email = document.getElementById("email");
    const error = document.getElementById("emailError");

    if (!email) return true;

    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regex.test(email.value.trim())) {
        error.textContent = "Email no válido";
        error.style.color = "red";
        return false;
    }

    error.textContent = "Email válido";
    error.style.color = "green";
    return true;
}


function validarPassword() {
    const password = document.getElementById("password");
    const error = document.getElementById("passwordError");

    if (!password) return true;

    const regex = /^[A-Za-z0-9]{6,}$/;

    if (!regex.test(password.value)) {
        error.textContent = "Contraseña inválida: mínimo 6 caracteres, solo letras y números.";
        error.style.color = "red";
        return false;
    }

    error.textContent = "Contraseña válida";
    error.style.color = "green";
    return true;
}


function validarConfirmPassword() {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const error = document.getElementById("confirmPasswordError");

    if (!confirmPassword || !password) return true;

    if (confirmPassword.value !== password.value || confirmPassword.value === "") {
        error.textContent = "Las contraseñas no coinciden";
        error.style.color = "red";
        return false;
    }

    error.textContent = "Las contraseñas coinciden";
    error.style.color = "green";
    return true;
}


// ---------------- EVENTOS EN VIVO ----------------

const nombre = document.getElementById("nombre");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");

if (nombre) {
    nombre.addEventListener("input", validarNombre);
}

if (email) {
    email.addEventListener("input", validarEmail);
}

if (password) {
    password.addEventListener("input", () => {
        validarPassword();
        validarConfirmPassword();
    });
}

if (confirmPassword) {
    confirmPassword.addEventListener("input", validarConfirmPassword);
}


// ---------------- BLOQUEAR ENVÍO SI ALGO FALLA ----------------

const registerForm = document.getElementById("registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", function (event) {

        const nombreOk = validarNombre();
        const emailOk = validarEmail();
        const passwordOk = validarPassword();
        const confirmOk = validarConfirmPassword();

        if (!nombreOk || !emailOk || !passwordOk || !confirmOk) {
            event.preventDefault();
            alert("Corrige los campos antes de registrarte.");
        }
    });
}
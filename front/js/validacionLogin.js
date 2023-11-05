const form = document.getElementById("form");
const userInput = document.getElementById("usuario");
const passInput = document.getElementById("password");


const checkUserName = () => {
    let valid = false;

    const min = 4;
    const max = 16;

    const username = userInput.value.trim();

    if (isEmpty(username)) {
        showError(userInput, "*Campo obligatorio")
    } else if (!isBetween(username.length,min,max)) {
        showError(userInput, `El nombre debe tener entre ${min} y ${max} caracteres`)
    } else {
        showSuccess(userInput);
        valid = true;
    }
    return valid;
};

const checkPassword = () => {
    let valid = false;

    const password = passInput.value.trim();

    if (isEmpty(password)) {
        showError(passInput, "*Contraseña obligatoria" )
    } else if (!isPasswordOk(password)) {
        showError(passInput, "Debe tener por lo menos 8 caracteres, mayuscula, minuscula y simbolos")
    } else {
        showSuccess(passInput)
        valid = true;
    }
    return valid;
};

const isEmpty = (value) => value === "";

const isBetween = (length, min, max) => {
   return length < min || length > max ? 
   false : true;
};

const isPasswordOk = (pass) => {
    const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,}$/;

    return re.test(pass);
};

const showError = (input, message) => {
    const formField = input.parentElement;
    formField.classList.remove("success");
    formField.classList.add("error");
    const error = formField.querySelector("small");
    error.textContent = message;
};

const showSuccess = (input) => {
    const formField = input.parentElement;
    formField.classList.remove("error");
    formField.classList.add("success");
    const error = formField.querySelector("small");
    error.textContent = "";
};

form.addEventListener("submit", (e) => {
    e.preventDefault(); 
    const isValidUsername = checkUserName();
    const isValidPassword = checkPassword();

    if (isValidUsername && isValidPassword) {
        window.location.href = '../index.html';
    }
});
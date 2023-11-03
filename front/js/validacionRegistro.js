const form = document.getElementById("form");
const passInput = document.getElementById("password");
const userInput = document.getElementById("user_name");
const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone");
const pass2Input = document.getElementById("password2");
const addressInput = document.getElementById("address");


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

const checkEmail = () => {
    let valid = false;

    const emailValue = emailInput.value.trim();

    if (isEmpty(emailInput)) {
        showError(emailInput, "*Mail obligatorio")
    } else if (!isEmailOk(emailValue)) {
        showError(emailInput, "Mail no valido, debe contener un @ y un punto")
    } else {
        showSuccess(emailInput)
        valid = true;
    }
    return valid;
};

const checkPhone = () => {
    let valid = false;

    const phoneValue = phoneInput.value.trim();

    if (!isPhoneOk(phoneValue)) {
        showError(phoneInput, "Telefono no valido, debe contener 10 caracteres")
    } else {
        showSuccess(phoneInput);
        valid = true;
    }
    return valid;
};

const checkPasswordsMatch = () => {
    if (passInput.value !== pass2Input.value) {
      showError(pass2Input, "Las contraseñas no coinciden");
      return false;
    } else {
      showSuccess(pass2Input);
      return true;
    }
};

const checkAddress = () => {
    if (isEmpty(addressInput.value)) {
        showError(addressInput, "*Dirección requerida");
        return false;
    } else {
        showSuccess(addressInput);
        return true;
    }
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

const isEmailOk = (email) => {
    const re =  /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;

    return re.test(email);
};

const isPhoneOk = (phone) => {
    const re = /^[0-9]{10}$/

    return re.test(phone);
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
    const isValidEmail = checkEmail(); 
    const isValidPhone = checkPhone(); 
    const isValidPasswordMatch = checkPasswordsMatch();
    const isValidAdress = checkAddress(); 

    if (isValidUsername && isValidPassword && isValidEmail && isValidPhone && isValidPasswordMatch && isValidAdress) {
        window.location.href = '../index.html';
    }
});
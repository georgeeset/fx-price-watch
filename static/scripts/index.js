const loginForm = document.querySelector('.login-form');
const signupForm = document.querySelector('.signup-form');
const toggleForms = () => {
//   loginForm.classList.toggle('display');
//   signupForm.classList.toggle('display');
    print("login pressed")
};

const loginButton = document.querySelector('button[name="login"]');
loginButton.addEventListener('click', toggleForms);

const signupButton = document.querySelector('button[name="signup"]');
signupButton.addEventListener('click', toggleForms);
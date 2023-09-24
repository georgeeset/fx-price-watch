const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
const signupButton = document.getElementById("btnSignup");
const loginButton = document.getElementById("btnLogin");


var current_state="signup";

const showLogin = () => {
    loginForm.style.opacity = '1';
    loginForm.style.display = 'block';
    signupForm.style.opacity = '0';
    signupForm.style.display = 'none';
}

const showSignup = () => {
    loginForm.style.opacity = '0';
    loginForm.style.display = 'none';
    signupForm.style.opacity = '1';
    signupForm.style.display = 'block';
}

loginButton.addEventListener('click', showLogin);

signupButton.addEventListener('click', showSignup);
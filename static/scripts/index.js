const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
var current_state="signup";

const showLogin = () => {
    loginForm.style.opacity = '1';
    loginForm.style.visibility = 'visible';
    signupForm.style.opacity = '0';
    signupForm.style.visibility = 'hidden';
}

const showSignup = () => {
    loginForm.style.opacity = '0';
    loginForm.style.visibility = 'hidden';
    signupForm.style.opacity = '1';
    signupForm.style.visibility = 'visible';
}

const loginButton = document.getElementById("btnLogin");
loginButton.addEventListener('click', showLogin);

const signupButton = document.getElementById("btnSignup");
signupButton.addEventListener('click', showSignup);
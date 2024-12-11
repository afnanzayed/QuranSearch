const validUsername = "admin";
const validPassword = "123";


function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    if (username === validUsername && password === validPassword) {
        message.style.color = "green";
        message.textContent = "Login successful!";
        window.location.href = "QuranSearch.html";
    } else {
        message.style.color = "red";
        message.textContent = "Invalid username or password!";
    }
}

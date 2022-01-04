function hidelogin() {
    document.getElementById('login-block').style.transform = "translateY(-200%)";
    document.getElementById('signup-block').style.transform = "translateY(0%)";
    document.getElementById('login-block').style.opacity = "0";
    document.getElementById('signup-block').style.opacity = "1";
}

function showlogin() {
    document.getElementById('login-block').style.transform = "translateY(0%)";
    document.getElementById('signup-block').style.transform = "translateY(200%)";
    document.getElementById('login-block').style.opacity = "1";
    document.getElementById('signup-block').style.opacity = "0";
}
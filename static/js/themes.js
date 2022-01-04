var daynight = 0;

function changetheme() {
    document.body.classList.toggle("dark");
    if (daynight == 0) {
        daynight = 1;
    } else {
        daynight = 0;
    }
}
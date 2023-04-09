menu.onclick = function myFunction() {
    let x = document.getElementById("myNav");
    if(x.className === "topnav") {
        x.className += " responsive";
    } else{
        x.className = "topnav"
    }
}
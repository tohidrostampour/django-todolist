let menu = document.querySelector('.theme-container');

document.addEventListener('DOMContentLoaded', () => {
    let items = readFromLocalStorage('background');
    setElementColor(items);
});

let Background = document.querySelectorAll(".input-field input");

document.querySelector('.change-theme').addEventListener('click', function () {
    let backgroundColor = [Background[0].value, Background[1].value, Background[2].value, Background[3].value, Background[4].value, Background[5].value, Background[6].value, Background[7].value];

    setElementColor(backgroundColor);

    localStorage.setItem('background', backgroundColor);

})


let themeOpen = document.querySelector('.head-content .theme-open');

themeOpen.onclick = function () {
    menu.classList.toggle('active');
}

function readFromLocalStorage(key) {
    let items;
    if(localStorage.getItem(key) == null) {
        items = [];
    }
    else {
        items = localStorage.getItem(key).split(',');
    }
    return items;
}

function setElementColor(colors){
    document.querySelector(':root').style.setProperty('--main-color', colors[0]);
    document.querySelector(':root').style.setProperty('--main-box', colors[1]);
    document.querySelector(':root').style.setProperty('--title-color', colors[2]);
    document.querySelector(':root').style.setProperty('--lable-color', colors[3]);
    document.querySelector(':root').style.setProperty('--btn-color', colors[4]);
    document.querySelector(':root').style.setProperty('--btn-text', colors[5]);
    document.querySelector(':root').style.setProperty('--btn-hover', colors[6]);
    document.querySelector(':root').style.setProperty('--btn-text-hover', colors[7]);
}
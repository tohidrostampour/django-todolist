let menu = document.querySelector('.theme-container');

document.addEventListener('DOMContentLoaded', () => {
    let items;

    if (localStorage.getItem('background') === null) {
        items = [];
    } else {
        items = localStorage.getItem('background').split(',');
    }

    document.querySelector(':root').style.setProperty('--main-color', items[0]);
    document.querySelector(':root').style.setProperty('--main-box', items[1]);
    document.querySelector(':root').style.setProperty('--title-color', items[2]);
    document.querySelector(':root').style.setProperty('--lable-color', items[3]);
    document.querySelector(':root').style.setProperty('--btn-color', items[4]);
    document.querySelector(':root').style.setProperty('--btn-text', items[5]);
    document.querySelector(':root').style.setProperty('--btn-hover', items[6]);
    document.querySelector(':root').style.setProperty('--btn-text-hover', items[7]);
});

let Background = document.querySelectorAll(".input-field input");

document.querySelector('.change-theme').addEventListener('click', function () {
    document.querySelector(':root').style.setProperty('--main-color', Background[0].value);
    document.querySelector(':root').style.setProperty('--main-box', Background[1].value);
    document.querySelector(':root').style.setProperty('--title-color', Background[2].value);
    document.querySelector(':root').style.setProperty('--lable-color', Background[3].value);
    document.querySelector(':root').style.setProperty('--btn-color', Background[4].value);
    document.querySelector(':root').style.setProperty('--btn-text', Background[5].value);
    document.querySelector(':root').style.setProperty('--btn-hover', Background[6].value);
    document.querySelector(':root').style.setProperty('--btn-text-hover', Background[7].value);

    let backgroundColor = [Background[0].value, Background[1].value, Background[2].value, Background[3].value, Background[4].value, Background[5].value, Background[6].value, Background[7].value];

    localStorage.setItem('background', backgroundColor);

})


let themeOpen = document.querySelector('.head-content .theme-open');

themeOpen.onclick = function () {
    menu.classList.toggle('active');
}

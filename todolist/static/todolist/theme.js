document.addEventListener('DOMContentLoaded', () => {
    let items = readFromLocalStorage('background');
    setElementColor(items);
    if(items != null){
        Background[0].value = items[0];
        Background[1].value = items[1];
        Background[2].value = items[2];
        Background[3].value = items[3];
        Background[4].value = items[4];
        Background[5].value = items[5];
        Background[6].value = items[6];
        Background[7].value = items[7];
    }
});

document.querySelector('.change-theme').addEventListener('click', function () {
    let backgroundColor = [Background[0].value, Background[1].value, Background[2].value, Background[3].value, Background[4].value, Background[5].value, Background[6].value, Background[7].value];

    setElementColor(backgroundColor);

    localStorage.setItem('background', backgroundColor);

    menu.classList.remove('active');

})

let menu = document.querySelector('.theme-container');
let menu2 = document.querySelector('.theme-container2');

let Background = document.querySelectorAll(".input-field-c input");
let defaultBackgroundColor = document.querySelectorAll(".theme-container2 div");

let themeOpen = document.querySelector('.head-content .theme-open');

themeOpen.onclick = function () {
    menu.classList.toggle('active');
    menu2.classList.remove('active');
}

let themeOpen2 = document.querySelector('.head-content .theme-open2');

themeOpen2.onclick = function () {
    menu2.classList.toggle('active');
    menu.classList.remove('active');
}


defaultBackgroundColor[0].addEventListener('click', function(){
    colors = ['#080d0c','#2c403a','#b4d9d9','#9fbfbf','#8aa69e','#141414','#b8adb1','#ffffff'];
    setElementColor(colors);
    localStorage.setItem('background', colors);
});
defaultBackgroundColor[1].addEventListener('click', function(){
    colors = ['#0d0d0d','#404040','#d9d9d9','#a6a6a6','#737373','#ffffff','#7c7979','#d9d9d9'];
    setElementColor(colors);
    localStorage.setItem('background', colors);
});
defaultBackgroundColor[2].addEventListener('click', function(){
    colors = ['#202426','#4b4b49','#6c733d','#f2f2f2','#9da65d','#000000','#6c733d','#ffffff'];
    setElementColor(colors);
    localStorage.setItem('background', colors);
});
defaultBackgroundColor[3].addEventListener('click', function(){
    colors = ['#323c73','#5362b2','#d98c48','#ffffff','#d98c4a','#ffffff','#d9b1a3','#000000'];
    setElementColor(colors);
    localStorage.setItem('background', colors);
});
defaultBackgroundColor[4].addEventListener('click', function(){
    colors = ['#2e4559','#4a6d8c','#073c5f','#1a354d','#a9c6d9','#000000','#6a8aa6','#ffffff'];
    setElementColor(colors);
    localStorage.setItem('background', colors);
});
defaultBackgroundColor[5].addEventListener('click', function(){
    colors = ['#400106','#8b0e27','#f2bdc7','#ffffff','#f2bdc7','#000000','#ec748c','#fcfcfc'];
    setElementColor(colors);
    localStorage.setItem('background', colors);
});


function readFromLocalStorage(key) {
    let items;
    if (localStorage.getItem(key) == null) {
        items = null;
    } else {
        items = localStorage.getItem(key).split(',');
    }
    return items;
}

function setElementColor(colors) {
    if (colors.length != null) {
        document.querySelector(':root').style.setProperty('--main-color', colors[0]);
        document.querySelector(':root').style.setProperty('--main-box', colors[1]);
        document.querySelector(':root').style.setProperty('--title-color', colors[2]);
        document.querySelector(':root').style.setProperty('--lable-color', colors[3]);
        document.querySelector(':root').style.setProperty('--btn-color', colors[4]);
        document.querySelector(':root').style.setProperty('--btn-text', colors[5]);
        document.querySelector(':root').style.setProperty('--btn-hover', colors[6]);
        document.querySelector(':root').style.setProperty('--btn-text-hover', colors[7]);
    } else {
        document.querySelector(':root').style.setProperty('--main-color', 'rgb(27, 27, 27)');
        document.querySelector(':root').style.setProperty('--main-box', '#3F3A40');
        document.querySelector(':root').style.setProperty('--title-color', '#8ab0ca');
        document.querySelector(':root').style.setProperty('--lable-color', '#A67A29');
        document.querySelector(':root').style.setProperty('--btn-color', '#73685F');
        document.querySelector(':root').style.setProperty('--btn-text', '#ffffff');
        document.querySelector(':root').style.setProperty('--btn-hover', '#A67A29');
        document.querySelector(':root').style.setProperty('--btn-text-hover', '#8ab0ca');
    }
}



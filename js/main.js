const mntoggle = document.querySelector('.menu-toggle input');
const nav = document.querySelector('nav ul');
var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

mntoggle.addEventListener('click',function(){
   nav.classList.toggle('menushow');
})


function opentab(tabname){
    for(tablink of tablinks){
        tablink.classList.remove("active-links");
    }
    for(tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-links");
    document.getElementById(tabname).classList.add("active-tab");
}
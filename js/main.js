const mntoggle = document.querySelector('.menu-toggle input');
const nav = document.querySelector('nav ul');
var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

mntoggle.addEventListener('click',function(){
   nav.classList.toggle('menushow');
})


$(function () {
    const filePath = 'scrap_data/scrap.json';
    $.get(filePath, function (data) {
        var str = "<table border=1>";
        str += "<tr><td>No</td><td>Judul</td><td>Kategori</td><td>Waktu Publish</td><td>Waktu Scraping</td></tr>";

        $.each(data, function (n, item) {
            str += "<tr>";
            str += "<td>" + (n + 1) + "</td>";
            str += "<td>" + item.Judul + "</td>";
            str += "<td>" + item.Kategori + "</td>";
            str += "<td>" + item['Waktu-Publish'] + "</td>";
            str += "<td>" + item['Waktu-Scrapping'] + "</td>";
            str += "</tr>";
        });
        str += "</tabel>";
        $('#data').html(str);
    });
});



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


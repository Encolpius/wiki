let tabs = document.getElementsByClassName('tablinks');
let tabcontent = document.getElementsByClassName("tabcontent");

for (let i = 0; i < tabs.length; i++) {
    tabs[i].addEventListener("mouseover", openNavTab);
    tabs[i].addEventListener("mouseleave", closeNavTab);
}

for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].addEventListener("mouseenter", keepTabOpen);
    tabcontent[i].addEventListener("mouseleave", closeNavTab);
}

function openNavTab(tabName) {
    let tab = tabName.srcElement.innerHTML;
    for (let i = 0; i < tabs; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tab).style.display = "block";
    updateMargin(tab);
}

function updateMargin(tabName) {
    let tab = document.getElementById(tabName);
    tabName == "Players"      ?  tab.style.marginLeft = "2px" :
        tabName == "Sessions" ?  tab.style.marginLeft = "88px" : 
        tabName == "NPCs"     ?  tab.style.marginLeft = "145px": 
        tabName == "Places"   ?  tab.style.marginLeft = "242px" : 
        tabName == "Villains" ?  tab.style.marginLeft = "330px" : 
        tabName;
}

function closeNavTab() {
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
}

function keepTabOpen(tabName) {
    document.getElementById(tabName).style.display = "block";
}


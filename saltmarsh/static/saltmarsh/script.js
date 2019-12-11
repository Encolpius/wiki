function openNavTab(evt, tabName) {
    let tablinks = document.getElementsByClassName("tablinks");
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    updateMargin(tabName);
}

function updateMargin(tabName) {
    let tab = document.getElementById(tabName);
    tabName == "Players"      ?  tab.style.marginLeft = "8px" :
        tabName == "Sessions" ?  tab.style.marginLeft = "90px" : 
        tabName == "NPCs"     ?  tab.style.marginLeft = "185px": 
        tabName == "Places"   ?  tab.style.marginLeft = "250px" : 
        tabName == "Villains" ?  tab.style.marginLeft = "335px" : 
        tabName;
}

function closeNavTab() {
    let tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
}

function keepTabOpen(tabName) {
    document.getElementById(tabName).style.display = "block";
}


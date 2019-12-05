function openNavTab(evt, tabName) {
    let tabcontent = document.getElementsByClassName("tabcontent");
    let tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active"
    if (tabName == "Sessions") {
        document.getElementById(tabName).style.marginLeft = "90px";
    } else if (tabName == "NPCs") {
        document.getElementById(tabName).style.marginLeft = "180px";
    } else if (tabName == "Places") {
        document.getElementById(tabName).style.marginLeft = "250px";
    } else if (tabName == "Villains") {
        document.getElementById(tabName).style.marginLeft = "335px";
    }
}

function leaveTab(tabName) {
    document.getElementById(tabName).style.display = "none";
}

function carregar() {
    var msg = window.document.getElementById("msg")
    var img = window.document.getElementById("imagem")
    var now = new Date()
    var currentHour = now.getHours()
    msg.innerHTML= `Agora sao ${currentHour} horas.`
    var oldLink = document.getElementById('dynamic-favicon');
    document.head.removeChild(oldLink);
    link = document.createElement("link")
    link.id = "dynamic-favicon"
    link.rel="shortcut icon"
    link.type="image/x-icon"
    if(currentHour >= 0 && currentHour < 12) {
        msg.innerHTML += '<p><strong>Bom dia!'
        img.src = 'bomdia.png'
        document.body.style.background = "#EFDBC3"
        link.href="bomdia.ico"
    } else if(currentHour >= 12 && currentHour < 18){
        msg.innerHTML += '<p><strong>Boa tarde!'
        img.src = 'boatarde.png'
        document.body.style.background = "#E58C15"
        link.href="boatarde.ico"
    } else {
        msg.innerHTML += '<p><strong>Boa noite!</strong></p>'
        img.src = 'boanoite.png'
        document.body.style.background = "#071532"
        link.href="noite.ico"
    }
    document.head.appendChild(link);
}
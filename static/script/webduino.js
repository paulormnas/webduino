let toggle = false
function toggleClick() {
  toggle = !toggle
  if (toggle === true){
    document.getElementById("toggle-label").innerHTML = "LIGADO"
  } else {
    document.getElementById("toggle-label").innerHTML = "DESLIGADO"
  }
}


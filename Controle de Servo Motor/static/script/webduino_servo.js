let toggle = false
function toggleClick() {
  toggle = !toggle
  if (toggle === true){
    document.getElementById("toggle-label").innerHTML = "LIGADO"
  } else {
    document.getElementById("toggle-label").innerHTML = "DESLIGADO"
  }

  const xhttp = new XMLHttpRequest();
  xhttp.open('GET', 'http://localhost:8080/arduino', true);
  // TODO: Atualizar IP do serviço em produção
  xhttp.send();

  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      const dadosRecebidos = xhttp.responseText;
      console.log(dadosRecebidos)
    }
  };
}




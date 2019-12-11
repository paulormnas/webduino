const xhttp = new XMLHttpRequest();

function update() {
  xhttp.open('GET', 'http://localhost:8080/ler_temperatura', true);
  // TODO: Atualizar IP do serviço em produção
  xhttp.send();

  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      const dadosRecebidos = xhttp.responseText;
      console.log(dadosRecebidos);
      document.getElementById("value").innerHTML = dadosRecebidos;
    }
  };
}



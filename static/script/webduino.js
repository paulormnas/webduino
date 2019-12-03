let toggle
function toggleClick() {
  toggle = document.getElementById("toggle").value
  console.log(toggle);
  
  if (toggle === "on"){
    document.getElementById("toggle-label").innerHTML = "LIGADO"
  } else {
    document.getElementById("toggle-label").innerHTML = "DESLIGADO"
  }
}
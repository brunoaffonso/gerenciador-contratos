function marcaMenu(categoria) {
    var element = document.getElementById(categoria);
    element.classList.add("active");
}

function apagaMedicao() {
    confirm("Tem Certeza que deseja excluir a medição desejada?")
}
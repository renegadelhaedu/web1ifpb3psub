const camponome = document.getElementById('nome');
const msg = document.getElementById('msgerro');
function vertamanho(){
    if(camponome.value.length <= 4){
        msg.style.color = "red";
        msg.style.fontSize = "8px";

        msg.style.display = "block";
    }else{
        msg.style.display = "none";
    }

}
// Código JS para tornar ano não estático no footer

// Seleciona tag spam onde deve ser inserido o ano atual no footer
var spam = document.getElementById("ano_atual");

now = new Date;
seleciona_ano = now.getFullYear();

// Insere no HTML
spam.innerHTML += seleciona_ano; 


// Código JS da Galeria de imagens

// Seleciona todos os elementos com a classe "imagem_miniatura"
var imagens_miniaturas = document.getElementsByClassName("imagem_miniatura");

// Indica que, quando algum elemento da seleção for clicado, dispara a função tornar_destaque
for (var i = 0; i < imagens_miniaturas.length ; ++i){
  	imagens_miniaturas[i].onclick = tornar_destaque;
}

// Função responsável por retirar uma imagem em destaque e inserir outra 
function tornar_destaque(event) {

	// Se a imagem clicada contém a classe "imagem_selecionada"
    if (event.target.classList.contains("imagem_selecionada")) {
    	// pass
    } else {
    	// Seleciona o elemento que contém a classe "imagem_selecionada"
		var imagem_selecionada = document.getElementsByClassName("imagem_selecionada")[0];

		// Remove a classe "imagem_selecionada" do elemento
    	imagem_selecionada.classList.remove("imagem_selecionada");

    	// Adiciona a classe "imagem_selecionada" ao novo elemento que foi clicado
    	event.target.classList.add("imagem_selecionada");

    	// Seleciona o elemento que contém a classe "imagem_em_destaque"
    	var imagem_em_destaque = document.getElementsByClassName("imagem_em_destaque")[0];

    	// Troca o atributo "src" da imagem anterior pelo atributo "src" da nova imagem que foi clicada
    	imagem_em_destaque.setAttribute("src", event.target.src);

        // TESTES 
        
        // imagem_em_destaque.setAttribute("data-zoom-image", event.target.src);

        // teste = document.getElementsByClassName("zoomWindow")[0];

        // console.log(teste);

        // teste.target.style.backgroundImage = event.target.src;
    }
}

// Inicializa o zoom na imagem em destaque a partir da biblioteca ElevateZoom
$("#zoom").elevateZoom({
    // Tipo do zoom (nesse caso, zoom interno)
    zoomType: "inner",

    // Especifica o cursor do mouse
    cursor: "crosshair",

    // Ativa o deslize automático a partir do movimento do mouse
    easing: true,

    // Especifica intensidade do "delay" para o zoom aparecer e sair
    zoomWindowFadeIn: 600,
    zoomWindowFadeOut: 600
});


// // Carrosel das Plantas
// //Essa função controla que imagem deve aparecer no carrosel e coisas relacionadas a isso
// var carosel_index = 0;
// function show_slide (new_index)
// {
//     // Esconde o anterior e mostra o de agora.
//     document.getElementsByClassName('zoom_image')[carosel_index].setAttribute('hidden', 'true');
//     document.getElementsByClassName('zoom_image')[new_index].removeAttribute('hidden');
//     //Da pra melhorar a relação entre remover a classe em vez de setar para false
//     document.getElementsByClassName('slide_index')[carosel_index].classList.remove('select');
//     document.getElementsByClassName('slide_index')[new_index].classList.add('select');

//     carosel_index = new_index

// }

// zoom_image = document.getElementById('zoom_image');

// zoom_image.onmousemove = zoom;

// // Zoom nas imagens do Carrosel
// //Está funcão só controla que parte da imagem com zoom será mostrada em realção as coordenadas do mouse
// function zoom(event) {
//     console.log("oi");

//     //Faz a imagem de tamanho normal sumir
//     event.currentTarget.style.opacity = 0;

//     //converte a posição em coordenadas para porcentagem
//     var x = event.offsetX * 100 / event.currentTarget.offsetWidth;
//     var y = event.offsetY * 100 / event.currentTarget.offsetHeight;

//     // var x = event.offsetX;
//     // var y = event.offsetY;

//     // console.log(x);
//     // console.log(y);

//     event.currentTarget.style.backgroundPosition = "" + x + "%" + y + "%";

//     console.log(event.currentTarget.style.backgroundPosition)
// }

// //Fyuse e visualização em 360°
// function fyuse(){
//     a = document.getElementsByClassName('imagefyuse')[0];
//     if (a.hasAttribute('hidden')){
//         document.getElementsByClassName('carosel')[0].setAttribute('hidden', 'true');
//         document.getElementsByClassName('imagefyuse')[0].removeAttribute('hidden');
//     }
//     else {
//         document.getElementsByClassName('imagefyuse')[0].setAttribute('hidden', 'true');
//         document.getElementsByClassName('carosel')[0].removeAttribute('hidden');
//     }

// }

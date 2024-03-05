const searchButton = document.getElementById("ticker-search");

document.getElementById("ticker-input").addEventListener("input", function () {
  if (this.value.length > 0) {
    this.classList.add("has-content");
  } else {
    this.classList.remove("has-content");
  }
});

document
  .getElementById("ticker-input")
  .addEventListener("keypress", function (event) {
    // Verifica se a tecla pressionada é Enter (código de tecla 13)
    if (event.key === "Enter" || event.keyCode === 13) {
      event.preventDefault(); // Impede qualquer ação padrão do Enter, se necessário
      searchButton.click(); // Dispara o evento de clique do botão de pesquisa
    }
  });

searchButton.addEventListener("click", function () {
  // Adicione a classe 'active-state' ao elemento
  this.classList.add("active-state");

  searchTicker();
  // Defina um temporizador para remover a classe após 2 segundos (2000 milissegundos)
  setTimeout(() => {
    this.classList.remove("active-state");
  }, 2000);
});

function uppercaseAndLettersOnly(input) {
  // Salva a posição do cursor antes da mudança
  var cursorPosition = input.selectionStart;

  // Substitui qualquer caractere que não seja letra ou traço por uma string vazia e converte para maiúsculas
  var newValue = input.value.toUpperCase().replace(/[^A-Z-]/g, "");

  // Limita o valor a um máximo de 6 caracteres
  newValue = newValue.substring(0, 6);

  // Calcula quantos caracteres foram removidos até a nova posição do cursor
  var charactersRemoved = input.value.length - newValue.length;
  // Se a posição do cursor for maior que o comprimento do novo valor, ajusta-a para o final do novo valor
  if (cursorPosition > newValue.length) {
    cursorPosition = newValue.length;
  }

  // Atualiza o valor do input com o novo valor limitado a 6 caracteres
  input.value = newValue;

  // Ajusta a posição do cursor
  input.setSelectionRange(cursorPosition, cursorPosition);
}

function searchTicker() {
  var tickerValue = document.getElementById("ticker-input").value.toUpperCase();

  // Busca as informações do ticker e do nome da empresa em uma única chamada
  fetch(`http://localhost:3000/quote/${tickerValue}`)
    .then((response) => response.json())
    .then((data) => {
      // Extrai o preço de mercado regular e o nome da empresa dos dados
      const regularMarketPrice =
        data.quote.chart.result[0].meta.regularMarketPrice;
      const formattedPrice = regularMarketPrice.toFixed(2);
      const companyName = data.info ? data.info.Name : "Empresa não encontrada";

      // Atualiza a UI com o preço e o nome da empresa
      document.getElementById(
        "test-log"
      ).innerHTML = `<h2 id="price-now">${formattedPrice}</h2><p>${tickerValue} - ${companyName}</p>`;
    })
    .catch((error) => console.error("Erro ao buscar informações:", error));
}

<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Sistema de Cadastro de Funcionários</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 20px;
    }
    .container {
      max-width: 600px;
      background: white;
      padding: 30px;
      margin: auto;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h2 {
      text-align: center;
      color: #333;
    }
    input, button {
      padding: 10px;
      margin: 10px 0;
      width: 100%;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      margin: 5px 0;
      background: #eee;
      padding: 10px;
      display: flex;
      justify-content: space-between;
    }
    .remove-btn {
      background-color: red;
      color: white;
      border: none;
      cursor: pointer;
      padding: 5px 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Cadastro de Funcionários</h2>
    <input type="text" id="nomeInput" placeholder="Digite o nome do funcionário">
    <button onclick="cadastrar()">Cadastrar</button>

    <h3>Lista de Funcionários:</h3>
    <ul id="listaFuncionarios"></ul>
  </div>

  <script>
    const cadastro = [];

    function cadastrar() {
      const nome = document.getElementById("nomeInput").value.trim();
      if (nome === "") {
        alert("Digite um nome válido!");
        return;
      }

      cadastro.push(nome);
      document.getElementById("nomeInput").value = "";
      atualizarLista();
    }

    function remover(nome) {
      const index = cadastro.indexOf(nome);
      if (index !== -1) {
        cadastro.splice(index, 1);
        atualizarLista();
      }
    }

    function atualizarLista() {
      const lista = document.getElementById("listaFuncionarios");
      lista.innerHTML = "";

      cadastro.forEach(nome => {
        const li = document.createElement("li");
        li.innerHTML = `${nome} <button class="remove-btn" onclick="remover('${nome}')">Excluir</button>`;
        lista.appendChild(li);
      });
    }
  </script>
</body>
</html>


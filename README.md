# Simulador de Ataque de Phishing 👻
Este projeto é uma simulação de ataque de phishing, criado com o objetivo de ensinar como os ataques de engenharia social funcionam e como se proteger contra eles. O simulador finge ser uma página de login e coleta credenciais inseridas por um usuário em um ambiente controlado. O intuito é educativo, demonstrando como os atacantes podem capturar informações sensíveis.

## Tecnologias Utilizadas 🕵️
- Python - Linguagem principal para o desenvolvimento do servidor.
- Flask - Framework para desenvolvimento de web apps simples.
- HTML - Linguagem para criar a interface de login simulada.

## Funcionalidades 📌
Página de login simulada: Uma página simples onde o usuário pode inserir seu nome de usuário e senha.
Coleta de credenciais: Após o usuário tentar fazer login, as credenciais são salvas em um arquivo de texto chamado captured_credentials.txt.
Redirecionamento: Após o login, o usuário é redirecionado para uma página de agradecimento fictícia, onde é informado que a tentativa de login foi bem-sucedida.

## Requisitos 📌
- Python 3.x
- Flask (utilizado para servir a aplicação web)

## Instalação 🔔
Clone ou baixe este repositório.
Se você não tiver o Flask instalado, instale-o usando pip:
```
pip install Flask
```
Navegue até o diretório do projeto e execute o servidor Flask:
```
python app.py
```
O servidor irá iniciar e estará disponível em http://localhost:5001 (ou na porta definida no código).
Abra um navegador e vá para http://localhost:5001. Você verá a página de login simulada.

## Como Funciona
Ao acessar a página, você verá um formulário de login falso, que simula um serviço real.
Insira um nome de usuário e uma senha qualquer e clique em "Login".
As credenciais inseridas serão salvas no arquivo captured_credentials.txt (este arquivo é criado no mesmo diretório onde o script Python está localizado).
Após a submissão do formulário, o usuário será redirecionado para uma página de agradecimento fictícia.
As credenciais capturadas podem ser visualizadas no arquivo captured_credentials.txt.

Exemplo de Credenciais Capturadas
As credenciais capturadas serão armazenadas no arquivo captured_credentials.txt da seguinte forma:
```
Username: exemplo@gmail.com, Password: senha123
```
## Atenção ⚠️
Este projeto é apenas para fins educativos e não deve ser usado para fins maliciosos. O objetivo é mostrar como os ataques de phishing funcionam e como proteger-se deles.

## Contribuições 📚
Este projeto é simples e pode ser expandido com mais funcionalidades. Se você deseja contribuir ou melhorar o projeto, fique à vontade para fazer um fork e enviar pull requests.

## Licença 📍
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

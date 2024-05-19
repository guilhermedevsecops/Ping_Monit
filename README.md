# Telegram Report

## Descrição

O "Telegram Report" é um sistema de monitoramento desenvolvido em Python. Ele realiza um ping em todos os dispositivos da rede e, caso ocorra falha em três tentativas consecutivas de ping, uma mensagem é enviada para um canal específico no Telegram.

## Funcionalidades

- Realiza ping em todos os dispositivos da rede.
- Detecta falhas de conexão após três tentativas consecutivas de ping.
- Envia relatórios de falhas para um canal no Telegram.

## Como Usar

1. Clone o repositório do projeto.
2. Configure o arquivo de configuração com as informações da rede.
3. Execute o script Python para iniciar o monitoramento.
4. Verifique o canal no Telegram para relatórios de falhas.

## Requisitos

- Python 3.x
- Biblioteca Telegram API (se necessário para enviar mensagens para o Telegram)

## Configuração

Antes de usar o sistema, é necessário configurar as seguintes informações:

- Endereço IP e porta do servidor do Telegram.
- Token de autenticação do Telegram.
- Lista de dispositivos na rede para monitoramento.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE).

<div align="center">
    <img src="https://camo.githubusercontent.com/0eb5523ac2254d96f5b07821a632c353a57168b898293675338d25c54b8d7bbe/68747470733a2f2f692e696d6775722e636f6d2f6a5130593556362e706e67" width="154" />

    # Instagram Comment Bot

Este é um script Python que usa a biblioteca Selenium para automatizar tarefas no Instagram, especificamente fazer login e comentar fotos.

[![Python 3](https://img.shields.io/badge/Python%20Version-3-green)]()
[![Libs](https://img.shields.io/badge/Libs-Selenium-blue)]()

</div>

## Pre-requisitos

This script requires Python 3 and the following Python libraries:

- selenium

É necessário tambem ter o navegador Firefox instalado no seu computador.

## Instalação

Clone este repositório para sua máquina local:

```bash
  https://github.com/rodrigordgfs/bot-comentario-insta.git
  cd InstagramBot
```

Crie seu ambiente virtual:

```bash
  py -m venv venv
```

Instale as bibliotecas Python necessárias:

```bash
  pip install -r requirements.txt
```

## Lista de usuarios

Para o funcionamento do bot deve existir o arquivo _users.json_ na raiz do projeto. Cada linha do arquivo json é um comentário, como na estrutura abaixo.

```json
[
    "@username1 @username2",
    "@username3 @username4",
    "@username5 @username6",
    ...
]
```

## Variaveis de ambiente

Deve ser criado um arquivo chamado _.env_ com as seguintes variaveis

| Nome             | tipo   | descriçãp                                   |
| ---------------- | ------ | ------------------------------------------- |
| USERNAME         | String | Nome de login do usuário                    |
| PASSWORD         | String | Senha de login do usuário                   |
| GECKODRIVER_PATH | String | Path de onde esta o arquivo geckodriver.exe |
| FIREFOX_PATH     | String | Path de onde esta instalado o Firefox       |
| POST_URL         | String | URL do post que deseja ser comentao         |

## Uso/Exemplos

Para usar basta configurar o arquivo de debug do VSCode da seguinte maneira

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/igBot.py",
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/.env",
      "justMyCode": true
    }
  ]
}
```

Após isto basta executar e o bot começara a comentar na postagem selecionada.

OBS: Cuidado com o uso deste bot, pois o instagram pode bloquear sua conta de comentar por algumas horas.

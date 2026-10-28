# Calculadoras em Python

Este projeto contém dois programas de calculadora executados no terminal, sem dependências externas.

## Requisitos

- Python 3 instalado.
- Python 3.10 ou superior para executar `calculadorainterativa.py`, que usa `match/case`.

## Como executar

Abra um terminal na pasta do projeto e execute um dos comandos:

```powershell
python .\calculadora.py
```

```powershell
python .\calculadorainterativa.py
```

Se o comando `python` não estiver disponível no Windows, tente usar `py` no lugar dele.

## Programas

### `calculadora.py`

Calculadora simples com um menu interativo. Oferece:

- Adição
- Subtração
- Multiplicação
- Divisão

O programa valida a opção escolhida, trata entradas numéricas inválidas e impede divisão por zero.

### `calculadorainterativa.py`

Versão com operações adicionais:

- Adição, subtração e multiplicação
- Divisão
- Potência
- Raiz quadrada de números não negativos
- Resto da divisão
- Divisão inteira

Também valida as opções e trata entradas inválidas e operações de divisão por zero. Pressione `0` para sair; após cada operação, pressione Enter para voltar ao menu.

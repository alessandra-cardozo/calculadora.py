Markdown
# 🧮 Calculadora em Python

Projeto desenvolvido com o objetivo de praticar a lógica de programação, modularização, tratamento de exceções e estruturas de controle em **Python**. O repositório contém duas versões de calculadoras executadas diretamente pelo terminal.

---

## 🚀 Tecnologias Utilizadas
* **Python** (versão 3.10 ou superior recomendada para suporte ao `match/case`)
* Módulo nativo **`math`**

---

## 📁 Estrutura dos Programas

### 1. `calculadora.py` (Calculadora Simples)
Uma calculadora com um menu interativo básico para operações do dia a dia[cite: 3]. 
* **Operações suportadas:** Adição, Subtração, Multiplicação e Divisão[cite: 3].
* **Validações:** O programa valida as opções do menu, trata entradas numéricas inválidas (`ValueError`) e impede a divisão por zero (`ZeroDivisionError`)[cite: 3].

### 2. `calculadorainterativa.py` (Calculadora Avançada)
Uma versão modularizada e expandida, utilizando funções separadas para cada operação e a estrutura moderna `match/case`[cite: 3].
* **Operações suportadas:**
  * Adição (`+`)[cite: 3]
  * Subtração (`-`)[cite: 3]
  * Multiplicação (`*`)[cite: 3]
  * Divisão (`/`)[cite: 3]
  * Potência (`**`)[cite: 3]
  * Raiz Quadrada (`√`)[cite: 3]
  * Resto da Divisão (`%`)[cite: 3]
  * Divisão Inteira (`//`)[cite: 3]
* **Validações:** Tratamento completo de erros para entradas inválidas, raízes de números negativos e divisão por zero[cite: 3].

---

## 🛠️ Como Executar o Projeto

Certifique-se de ter o Python instalado no seu computador[cite: 3].

1. Clone este repositório ou descarregue os ficheiros[cite: 3].
2. Abra um terminal na pasta onde os ficheiros estão guardados[cite: 3].
3. Execute o programa desejado digitando um dos comandos abaixo[cite: 3]:

* Para a versão simples:
  ```bash
  python calculadora.py
(Se o comando python não estiver disponível no seu Windows, tente usar py)[cite: 3]

Para a versão interativa avançada:

Bash
python calculadorainterativa.py
💡 Como Usar
Ao iniciar o programa, um menu interativo aparecerá no seu terminal[cite: 3]. Basta digitar o número correspondente à operação desejada, inserir os números solicitados quando pedido e pressionar Enter para continuar[cite: 3]. Para encerrar a aplicação, basta escolher a opção de sair (0)[cite: 3].



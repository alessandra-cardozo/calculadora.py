
print("===== MINHA CALCULADORA =====")

while True:
    print("\nEscolha uma operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "0":
        print("Calculadora encerrada. Até logo!")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = numero1 + numero2

        elif opcao == "2":
            resultado = numero1 - numero2

        elif opcao == "3":
            resultado = numero1 * numero2

        elif opcao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
                continue
            resultado = numero1 / numero2

        print(f"Resultado: {resultado:g}")
 
    except ValueError:
        print("Erro: digite apenas números válidos.")


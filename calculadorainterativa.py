import math
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Não é possível dividir por zero!")
    return a / b
def potencia(a, b):
    return a ** b
def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Erro: Não existe raiz quadrada real de número negativo!")
    return math.sqrt(a)
def menu():
    print("\n" + "=" * 36)
    print("      CALCULADORA EM PYTHON")
    print("=" * 36)
    print("  [1] Somar (+)")
    print("  [2] Subtrair (-)")
    print("  [3] Multiplicar (*)")
    print("  [4] Dividir (/)")
    print("  [5] Potência (**)")
    print("  [6] Raiz Quadrada (√)")
    print("  [7] Resto da Divisão (%)")
    print("  [8] Divisão Inteira (//)")
    print("  [0] Sair")
    print("=" * 36)
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção (0-8): ").strip()
        if opcao == "0":
            print("\nObrigado por usar a Calculadora Python! Até logo!")
            break
        if opcao not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("\n⚠️ Opção inválida! Por favor, escolha um número de 0 a 8.")
            continue
        try:
            if opcao == "6":
                num = float(input("Digite o número para calcular a raiz: "))
                resultado = raiz_quadrada(num)
                print(f"\n✅ Resultado: √{num} = {resultado}")
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                match opcao:
                    case "1":
                        resultado = somar(num1, num2)
                        print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")
                    case "2":
                        resultado = subtrair(num1, num2)
                        print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")
                    case "3":
                        resultado = multiplicar(num1, num2)
                        print(f"\n✅ Resultado: {num1} * {num2} = {resultado}")
                    case "4":
                        resultado = dividir(num1, num2)
                        print(f"\n✅ Resultado: {num1} / {num2} = {resultado}")
                    case "5":
                        resultado = potencia(num1, num2)
                        print(f"\n✅ Resultado: {num1} ^ {num2} = {resultado}")
                    case "7":
                        if num2 == 0:
                            raise ZeroDivisionError("Erro: divisão por zero no resto!")
                        resultado = num1 % num2
                        print(f"\n✅ Resultado: {num1} % {num2} = {resultado}")
                    case "8":
                        if num2 == 0:
                            raise ZeroDivisionError("Erro: divisão inteira por zero!")
                        resultado = num1 // num2
                        print(f"\n✅ Resultado: {num1} // {num2} = {resultado}")
        except ValueError as e:
            print(f"\n❌ Entrada inválida: {e}")
        except ZeroDivisionError as e:
            print(f"\n❌ {e}")
        except Exception as e:
            print(f"\n❌ Ocorreu um erro inesperado: {e}")
        input("\nPressione ENTER para continuar...")
if __name__ == "__main__":
    main()

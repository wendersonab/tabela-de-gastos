# criar, ler, atualizar, apagar
# criar uma aplicação que eu possa adicionar ou modificar gastos, subtraindo-os da minha renda total
import time
import sys
import re
import os

linha_titulo = "="*62
titulo = "                    ORGANIZADOR DE GASTOS"
while True:
    print(f"{linha_titulo}\n{titulo}\n{linha_titulo}")
    print("1. Cadastrar um gasto\n2. Editar um gasto\n3. Remover um gasto\n4. Mostrar todos os gastos\n5. Adicionar/substituir renda fixa\n6. Calcular quanto da minha renda vai sobrar (renda fixa)\n7. Calcular quanto da minha renda vai sobrar (renda variável)\n8. Marcar como pago\n9. Marcar como pendente\n10. Sair da aplicação")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7 or opcao == 8 or opcao == 9:
        while opcao == 1:
            print()
            print("Você escolheu cadastrar um gasto")
            time.sleep(.5)
            nome = input("Digite o nome do seu gasto: ")
            valor = int(input(f"Digite quanto o gasto {nome} custa: R$ "))
            if valor > 0:
                with open("gastos.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"{nome} - R$ {valor}\n")
                print(f"{nome} - R$ {valor}: Adicionado")
                voltar = int(input("Digite 1 para voltar: "))
                if voltar == 1:
                    time.sleep(.5)
                    os.system("cls")
                time.sleep(.7)
                break
            else:
                print("Digite um valor válido.")
                time.sleep(.7)
        while opcao == 2:
            time.sleep(.5)
            print()
            print("Você escolheu editar um gasto")
            with open("gastos.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.read().splitlines()
                for i, linha in enumerate(linhas, start=1):
                    print(f"{i}. {linha}")
                numero_do_gasto = int(input("Digite o número do gasto que deseja editar: "))
                if 1 <= numero_do_gasto <= len(linhas):
                    print(f"Gasto selecionado: {linhas[numero_do_gasto - 1]}")
                    novo_nome = input("Digite um novo nome para o gasto: ")
                    novo_valor = int(input("Digite um novo valor para o gasto: R$ "))
                    linhas[numero_do_gasto - 1] = f"{novo_nome} - R$ {novo_valor}"
                    with open("gastos.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.write("\n".join(linhas))
                    print(f"Gasto editado com sucesso!")
                    time.sleep(.7)
                    voltar = int(input("Digite 1 para voltar: "))
                    if voltar == 1:
                        time.sleep(.5)
                        os.system("cls")
                        break
                    time.sleep(.7)
                    break
                else:
                    print("Digite um número válido.")
                    time.sleep(.7)
        while opcao == 3:
            time.sleep(.5)
            print()
            print("Você escolheu remover um gasto")
            with open("gastos.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.read().splitlines()
                for i, linha in enumerate(linhas, start=1):
                    print(f"{i}. {linha}")
                numero_do_gasto = int(input("Digite o número do gasto que deseja remover: "))
                if 1 <= numero_do_gasto <= len(linhas):
                    print(f"Gasto selecionado: {linhas[numero_do_gasto - 1]}")
                    for i in range(4):
                        removendo = "Removendo" + "." * i
                        sys.stdout.write("\r" + removendo)
                        sys.stdout.flush()
                        time.sleep(.7)
                    print()
                    linhas.pop(numero_do_gasto - 1)
                    with open("gastos.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.write("\n".join(linhas) + "\n")
                    print("Gasto removido com sucesso!")
                    voltar = int(input("Digite 1 para voltar: "))
                    if voltar == 1:
                        time.sleep(.5)
                        os.system("cls")
                        break
                    break
        while opcao == 4:
            print()
            print("Lista de gastos: ")
            with open("gastos.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.read().splitlines()
                for i, linha in enumerate(linhas, start=1):
                    print(f"{i}. {linha}")
                voltar = int(input("Digite 1 para voltar: "))
                if voltar == 1:
                    time.sleep(1)
                    os.system("cls")
                    print()
                    break
        while opcao == 5:
            print()
            print("Você escolheu adicionar/substituir renda fixa.")
            renda = float(input("Digite sua renda fixa: R$ "))
            if renda > 0:
                with open("renda.txt", "w") as arquivo_renda:
                    arquivo_renda.write(str(renda))
                for i in range(4):
                    adicionando = "Adicionando renda fixa" + "."*i
                    sys.stdout.write("\r" + adicionando)
                    time.sleep(.7)
                print()
                print("Renda adicionada com sucesso!")
                voltar = int(input("Digite 1 para voltar: "))
                if voltar == 1:
                    time.sleep(.5)
                    os.system("cls")
                    break
                time.sleep(1)
                break
            else:
                print(f"Digite uma renda diferente de R$ {renda}.")
                print()
                time.sleep(1)
        while opcao == 6:
            print("Você escolheu calcular quanto vai sobrar da sua renda se retirar os gastos.")
            with open("renda.txt", "r") as arquivo_renda:
                renda = float(arquivo_renda.read().strip())
                with open("gastos.txt", "r") as arquivo_gastos:
                    linhas = arquivo_gastos.read().splitlines()
                    soma = 0
                    for linha in linhas:
                        numeros = re.findall(r"\d+\.?\d*", linha)
                        if numeros:  # se encontrou algum número
                            valor_gastos = float(numeros[-1])  # pega o último número da linha
                            soma += valor_gastos  # adiciona ao total
                    valor_restante = renda - soma
                    print(f"Sobrará {valor_restante} da sua renda após pagar todos os gastos.")
                    voltar = int(input("Digite 1 para voltar: "))
                    if voltar == 1:
                        time.sleep(.5)
                        os.system("cls")
                        break
        while opcao == 7:
            print("Você escolheu calcular quanto vai sobrar da sua renda (variada) se retirar os gastos.")
            renda = float(input("Digite sua renda: R$ "))
            with open("gastos.txt", "r") as arquivo_gastos:
                linhas = arquivo_gastos.read().splitlines()
                soma = 0
                for linha in linhas:
                    numeros = re.findall(r"\d+\.?\d*", linha)
                    if numeros:  # se encontrou algum número
                        valor_gastos = float(numeros[-1])  # pega o último número da linha
                        soma += valor_gastos  # adiciona ao total
                valor_restante = renda - soma
                print(f"Sobrará {valor_restante} da sua renda após pagar todos os gastos.")
                voltar = int(input("Digite 1 para voltar: "))
                if voltar == 1:
                    time.sleep(.5)
                    os.system("cls")
                    break
    if opcao == 10:
        for i in range(4):
            saindo = "Saindo" + "."*i
            sys.stdout.write("\r" + saindo)
            sys.stdout.flush()
            time.sleep(1)
        print()
        break
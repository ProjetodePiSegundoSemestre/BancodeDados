import psutil as p

import mysql.connector

cnx = mysql.connector.connect(
    host="10.18.33.43",
    port=3306,
    user="AeroGuard",
    password="aeroguard2026!",
    database="AeroGuard")

cur = cnx.cursor()

def buscar_dados(hardware=None, tipo=None):
    if hardware and tipo:
        sql = "SELECT hardware, tipo, caputura, horario FROM psutil WHERE hardware = %s AND tipo = %s"
        cur.execute(sql, (hardware, tipo))
    elif hardware:
        sql = "SELECT hardware, tipo, caputura, horario FROM psutil WHERE hardware = %s"
        cur.execute(sql, (hardware,))
    else:
        sql = "SELECT hardware, tipo, caputura, horario FROM psutil"
        cur.execute(sql)
       
    resultados = cur.fetchall()
   
    if not resultados:
        print("\nNenhum dado encontrado para essa pesquisa.")
        return

    print(f"\n{'Hardware':<12} | {'Tipo de Dado':<20} | {'Valor Capturado':<15} | {'Horário da Captura'}")
    print("-" * 55)
    for linha in resultados:
        print(f"{linha[0]:<12} | {linha[1]:<20} | {linha[2]:<15} | {linha[3]}")

while True:

    print("\n----- MENU -----")

    print("Digite o número para solicitar uma ação:")

    print("1 - Vizualizar todos os dados capturados")
    print("2 - Visualizar dados capturados da CPU")
    print("3 - Visualizar dados capturados da Memória")
    print("4 - Visualizar dados capturados do Disco")
    print("5 - Visualizar usos capturados da CPU")
    print("6 - Visualizar frequências capturadas da CPU")
    print("7 - Visualizar quantidade de núcleo capturados da CPU")
    print("8 - Visualizar memória utilizada capturados")
    print("9 - Visualizar memória total capturados")
    print("10 - Visualizar memória disponivel capturados")
    print("11 - Visualizar uso capturados do Disco")
    print("12 - Visualizar espaço total capturados do Disco")
    print("13 - Sair")


    opcao = int(input("\nDigite sua opção: "))

    if opcao == 1:
        print("\n--- Exibindo todos os dados da tabela ---")
        buscar_dados()

    elif opcao == 2:
        buscar_dados(hardware="CPU")

    elif opcao == 3:
        buscar_dados(hardware="Memória")

    elif opcao == 4:
        buscar_dados(hardware="Disco")

    elif opcao == 5:
        buscar_dados(hardware="CPU", tipo="Uso percentual")

    elif opcao == 6:
        buscar_dados(hardware="CPU", tipo="Frequencia atual")
       
    elif opcao == 7:
        buscar_dados(hardware="CPU", tipo="núcleos")

    elif opcao == 8:
        buscar_dados(hardware="Memória", tipo="Utilizada")

    elif opcao == 9:
        buscar_dados(hardware="Memória", tipo="Total")

    elif opcao == 10:
        buscar_dados(hardware="Memória", tipo="Disponível")

    elif opcao == 11:
        buscar_dados(hardware="Disco", tipo="Uso porcentual")

    elif opcao == 12:
        buscar_dados(hardware="Disco", tipo="Total GB C")

    elif opcao == 13:
        print("\nDesligando programa...")
        cur.close()
        cnx.close()
        break

    else:

        print("\nOpção inválida!")

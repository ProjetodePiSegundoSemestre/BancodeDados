import mysql.connector
import socket

hostname_atual = socket.gethostname()

cnx = mysql.connector.connect(
    host="10.18.33.54",
    port=3306,
    user="AeroGuard",
    password="aeroguard2026!",
    database="AeroGuard"
)

cur = cnx.cursor()

def obter_id_usuario(hostname):
    sql = "SELECT id FROM usuarios WHERE hostname = %s ORDER BY id DESC LIMIT 1"
    cur.execute(sql, (hostname,))
    resultado = cur.fetchone()
    if resultado:
        return resultado[0]
    else:
        print(f"Aviso: Usuário com hostname '{hostname}' não foi encontrado no banco.")
        return None

fk_usuario_id = obter_id_usuario(hostname_atual)

def buscar_dados(hardware=None, tipo=None):
    if not fk_usuario_id:
        print("Impossível consultar: Usuário não identificado.")
        return

    sql = "SELECT hardware, tipo, captura, horario FROM capturas WHERE fk_usuario = %s"
    parametros = [fk_usuario_id]

    if hardware and tipo:
        sql += " AND hardware = %s AND tipo = %s"
        parametros.extend([hardware, tipo])
    elif hardware:
        sql += " AND hardware = %s"
        parametros.append(hardware)

    cur.execute(sql, tuple(parametros))
    resultados = cur.fetchall()

    if not resultados:
        print("\nNenhum dado encontrado para essa pesquisa.")
        return

    print(f"\n{'Hardware':<12} | {'Tipo de Dado':<25} | {'Valor Capturado':<15} | {'Horário da Captura'}")
    print("-" * 75)
    for linha in resultados:
        print(f"{linha[0]:<12} | {linha[1]:<25} | {linha[2]:<15} | {linha[3]}")

while True:
    print("\n----- MENU -----")
    print("Digite o número para solicitar uma ação:")
    print("1 - Visualizar todos os dados capturados")
    print("2 - Visualizar dados capturados da CPU")
    print("3 - Visualizar dados capturados da Memória")
    print("4 - Visualizar dados capturados do Disco")
    print("5 - Visualizar usos capturados da CPU")
    print("6 - Visualizar frequências capturadas da CPU")
    print("7 - Visualizar quantidade de núcleos capturados da CPU")
    print("8 - Visualizar memória utilizada capturada")
    print("9 - Visualizar memória total capturada")
    print("10 - Visualizar memória disponível capturada")
    print("11 - Visualizar uso capturado do Disco")
    print("12 - Visualizar espaço total capturado do Disco")
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
        buscar_dados(hardware="CPU", tipo="Quantidade de nucleos")

    elif opcao == 8:
        buscar_dados(hardware="Memória", tipo="Utilizada (GB)")

    elif opcao == 9:
        buscar_dados(hardware="Memória", tipo="Total (GB)")

    elif opcao == 10:
        buscar_dados(hardware="Memória", tipo="Disponível (GB)")

    elif opcao == 11:
        buscar_dados(hardware="Disco", tipo="Uso percentual")

    elif opcao == 12:
        buscar_dados(hardware="Disco", tipo="Total (GB)")

    elif opcao == 13:
        print("\nDesligando programa...")
        cur.close()
        cnx.close()
        break

    else:
        print("\nOpção inválida!")
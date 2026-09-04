import mysql.connector 
import psutil as p
import time
import socket

hostname_atual = socket.gethostname()

cnx = mysql.connector.connect(
    host="10.18.33.54",
    port=3306,
    user="AeroGuard",
    password="aeroguard2026!",
    database="AeroGuard")

cur = cnx.cursor()


def salvar_usuario(hostname):
    sql = "INSERT INTO usuarios(hostname) VALUES (%s)"
    cur.execute(sql, (hostname,))
    cnx.commit()
    print(f"Usuário {hostname} cadastrado no banco.")

    fk_id = cur.lastrowid  
    print(f"Usuário {hostname} cadastrado com o ID {fk_id}")
    return fk_id


def salvar_dado(hardware, tipo, valor, fk_usuario_id):
    sql = "INSERT INTO capturas (hardware, tipo, captura, fk_usuario) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (hardware, tipo, float(valor), fk_usuario_id))
    cnx.commit()


fkUsuarios = salvar_usuario(hostname_atual)

while True:
    cpuPorcentagem = p.cpu_percent(interval=1)
    salvar_dado("CPU", "Uso percentual", cpuPorcentagem, fkUsuarios)

    cpuFrequencia = p.cpu_freq().current
    salvar_dado("CPU", "Frequencia atual", cpuFrequencia, fkUsuarios)

    cpuContagem = p.cpu_count()
    salvar_dado("CPU", "Quantidade de nucleos", cpuContagem, fkUsuarios)

    ramPorcentagem = p.virtual_memory().percent
    salvar_dado("Memória", "Uso percentual", ramPorcentagem, fkUsuarios)

    memoriaVirtual = round(p.virtual_memory().used / (1024**3), 2)
    salvar_dado("Memória", "Utilizada (GB)", memoriaVirtual, fkUsuarios)

    memoriaTotal = round(p.virtual_memory().total / (1024**3), 2)
    salvar_dado("Memória", "Total (GB)", memoriaTotal, fkUsuarios)

    memoriaDisponivel = round(p.virtual_memory().available / (1024**3), 2)
    salvar_dado("Memória", "Disponível (GB)", memoriaDisponivel, fkUsuarios)

    discoPorcentagem = p.disk_usage('C://').percent
    salvar_dado("Disco", "Uso percentual", discoPorcentagem, fkUsuarios)

    espacoDisco = round(p.disk_usage("C://").total / (1024**3), 2)
    salvar_dado("Disco", "Total (GB)", espacoDisco, fkUsuarios)

    print("Métricas capturadas e enviadas ao AeroGuard!")
    time.sleep(10)

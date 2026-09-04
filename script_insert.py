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
    cur.execute(sql,(hostname,))
    cnx.commit()
    print(f"Usuário {hostname} cadastro")

    fk_id = cur.lastrowid  
    print(f"Usuário {hostname} cadastrado com o ID {fk_id}")
    return fk_id



def salvar_dado(hardware, tipo, valor, fkUsuarios):
  sql = "INSERT INTO capturas (hardware, tipo, captura, fkusuarios) VALUES (%s, %s, %s, %s)"
  cur.execute(sql, (hardware, tipo, float(valor), fkUsuarios))
  cnx.commit()

fkUsuarios = salvar_usuario(hostname_atual)

while True:

            cpuPorcentagem = p.cpu_percent(interval=1)
            salvar_dado("CPU", "Uso percentual", cpuPorcentagem, fkUsuarios)

            ramPorcentagem = p.virtual_memory().percent
            salvar_dado("CPU", "Frequencia atual", ramPorcentagem, fkUsuarios)

            discoPorcentagem = p.disk_usage('/').percent
            salvar_dado("CPU", "núcleos", discoPorcentagem, fkUsuarios)

            cpuFrequencia = p.cpu_freq().current
            salvar_dado("CPU", "Frequencia atual", cpuFrequencia, fkUsuarios)

            cpuContagem = p.cpu_count()
            salvar_dado("CPU", "núcleos", cpuContagem, fkUsuarios)

            memoriaVirtual = round(p.virtual_memory().used / (1024**3), 2)
            salvar_dado("Memória", "Utilizada", memoriaVirtual, fkUsuarios)

            memoriaTotal = round(p.virtual_memory().total / (1024**3), 2)
            salvar_dado("Memória", "Total", memoriaTotal, fkUsuarios)

            memoriaDisponivel = round(p.virtual_memory().available / (1024**3), 2)
            salvar_dado("Memória", "Disponível", memoriaDisponivel, fkUsuarios)

            espacoDisco = round(p.disk_usage("/").total / (1024**3), 2)
            salvar_dado("Disco", "Uso porcentual", espacoDisco, fkUsuarios)
    
            time.sleep(10)








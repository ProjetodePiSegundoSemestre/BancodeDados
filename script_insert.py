import mysql.connector 
import psutil as p
import time

cnx = mysql.connector.connect(
    host="10.18.33.43",
    port=3306,
    user="AeroGuard",
    password="aeroguard2026!",
    database="AeroGuard")

cur = cnx.cursor()

def salvar_dado(hardware, tipo, valor):
  sql = "INSERT INTO capturas (hardware, tipo, caputura) VALUES (%s, %s, %s)"
  cur.execute(sql, (hardware, tipo, float(valor)))
  cnx.commit()


while True:
            usuario = input('Qual é seu nome: ')

            cpuPorcentagem = p.cpu_percent(interval=1)
            salvar_dado("CPU", "Uso percentual", cpuPorcentagem)

            ramPorcentagem = p.virtual_memory().percent
            salvar_dado("CPU", "Frequencia atual", ramPorcentagem)

            discoPorcentagem = p.disk_usage('C:\\').percent
            salvar_dado("CPU", "núcleos", discoPorcentagem)

            cpuFrequencia = p.cpu_freq().current
            salvar_dado("CPU", "Frequencia atual", cpuFrequencia)

            cpuContagem = p.cpu_count()
            salvar_dado("CPU", "núcleos", cpuContagem)

            memoriaVirtual = round(p.virtual_memory().used / (1024**3), 2)
            salvar_dado("Memória", "Utilizada", memoriaVirtual)

            memoriaTotal = round(p.virtual_memory().total / (1024**3), 2)
            salvar_dado("Memória", "Total", memoriaTotal)

            memoriaDisponivel = round(p.virtual_memory().available / (1024**3), 2)
            salvar_dado("Memória", "Disponível", memoriaDisponivel)

            espacoDisco = round(p.disk_usage("C:\\").total / (1024**3), 2)
            salvar_dado("Disco", "Uso porcentual", espacoDisco)

    
            time.sleep(10)








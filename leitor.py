import csv

with open("dados.csv", "r") as arquivo_dados:
    leitor = csv.reader(arquivo_dados)
    for linha in leitor:
        print(f"{linha[0]:<20} {linha[2]:<40} {linha[1]:>20}")



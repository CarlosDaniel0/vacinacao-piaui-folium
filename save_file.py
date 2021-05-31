import csv
import requests

CSV_URL = 'https://docs.google.com/spreadsheets/d/1tttGLST1VR5duGWbvcQ2EyrllpAINXGe5W3fYEaZj0E/gviz/tq?tqx=out:csv&sheet=tratamento_dados'
file = open('vacinados.csv', 'w')
csv_file = csv.writer(file)


def decode_lines(lines):
    line_decoded = []
    count = 0
    for line in lines:
        row = line.decode('UTF-8').replace('"', "").split(',')
        if count == 0:
            line_decoded.append(row)
        else:
            n_row = []
            for i in range(len(row)):
                aux = 0
                aux = int(row[i])
                if i == 2:
                    aux = float(aux/100)
                n_row.append(aux)
            line_decoded.append(n_row)
        count += 1
    return line_decoded


with requests.get(CSV_URL) as r:
    lines = decode_lines(r.iter_lines())
    #(line.decode('UTF-8') for line in r.iter_lines())
    csv_file.writerows(lines)

file.close()

from prettytable import PrettyTable

data = [
    ["Kode", "C1", "C2", "C3", "C4"],
    ["D1", 90, 81, 89, 77],
    ["D2", 70, 80, 80, 85],
    ["D3", 85, 69, 78, 80],
    ["D4", 95, 80, 83, 80],
    ["D5", 82, 75, 85, 82],
    ["D6", 76, 85, 80, 87],
    ["D7", 72, 80, 75, 78],
    ["D8", 68, 72, 79, 86]
]

bobot = [
    ["C1", "C2", "C3", "C4"],
    [25, 30, 25, 20]
]

def print_table(matrix):
    table = PrettyTable()
    table.field_names = matrix[0]
    for row in matrix[1:]:
        table.add_row(row)
    print(table)

print("Tahap 1: Pembentukan matriks keputusan (X)")
print_table(data)
print()

min_values = [min(row[i] for row in data[1:]) for i in range(1, len(data[0]))]
max_values = [max(row[i] for row in data[1:]) for i in range(1, len(data[0]))]

normalized_data = [data[0]]
for row in data[1:]:
    normalized_row = [row[0]] + [(row[i] - min_values[i - 1]) / (max_values[i - 1] - min_values[i - 1]) for i in range(1, len(row))]
    normalized_data.append(normalized_row)

print("Tahap 2: Matriks Keputusan (X) Setelah Normalisasi:")
print_table(normalized_data)
print()

weighted_matrix = [data[0]]
for row in normalized_data[1:]:
    weighted_row = [row[0]] + [row[i] * bobot[1][i-1] + bobot[1][i-1] for i in range(1, len(row))]
    weighted_matrix.append(weighted_row)

print("Tahap 3: Perhitungan Elemen Matriks Tertimbang (V):")
print_table(weighted_matrix)
print()

G = ["G"]
for i in range(1, len(weighted_matrix[0])):
    column_values = [row[i] for row in weighted_matrix[1:]]
    product = 1
    for value in column_values:
        product *= value
    G.append(product ** (1/8))

print("Tahap 4: Matriks Area Perkiraan Batas (G):")
G_table = PrettyTable()
G_table.field_names = weighted_matrix[0]
G_table.add_row(G)
print(G_table)
print()

Q = [["Alternatif"] + weighted_matrix[0][1:]]
for i in range(1, len(weighted_matrix)):
    Q_row = [weighted_matrix[i][0]]
    for j in range(1, len(weighted_matrix[i])):
        Q_value = weighted_matrix[i][j] - G[j]
        Q_row.append(Q_value)
    Q.append(Q_row)

print("Tahap 5: Matriks Jarak (Q):")
print_table(Q)
print()

ranking_scores = {}
for row in Q[1:]:
    alternative = row[0]
    score = sum(row[1:])
    ranking_scores[alternative] = score

print("Tahap 6: Perangkingan Alternatif")
ranking_table = PrettyTable()
ranking_table.field_names = ["Alternatif", "Skor"]
for alternative, score in ranking_scores.items():
    ranking_table.add_row([alternative, score])
print(ranking_table)

sorted_ranking = sorted(ranking_scores.items(), key=lambda x: x[1])
print()

print("Peringkat Alternatif:")
ranking_sorted_table = PrettyTable()
ranking_sorted_table.field_names = ["Peringkat", "Alternatif", "Skor"]
for rank, (alternative, score) in enumerate(sorted_ranking, start=1):
    ranking_sorted_table.add_row([rank, alternative, score])
print(ranking_sorted_table)

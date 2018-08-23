import csv

labels = \
    ["Network name", 'Jaccard Index', 'Normalized Arithmetic Mutual Information', 'Normalized Variation of Information']

with open("comparison_results.txt", "r") as f:
    lines = f.readlines()

names = []
jaccardIndex = []
NMIA = []
NVIM = []
for i in range(len(lines)):
    if lines[i].split(":")[0] == "Partition2":
        names.append(lines[i-1].split('/')[3].replace("\n", "") + "  vs  " + lines[i].split(":")[1].split("/")[1]
                     .replace("\n", ""))

    if 'Jaccard Index' in lines[i]:
        jaccardIndex.append(float(lines[i].split(': ')[1].replace("\n", "")))

    if 'Normalized Mutual Information Index (arithmetic)' in lines[i]:
        NMIA.append(float(lines[i].split(': ')[1].replace("\n", "")))

    if 'Normalized Variation Of Information Metric' in lines[i]:
        NVIM.append(float(lines[i].split(': ')[1].replace("\n", "")))

data = [labels]
for i in range(len(names)):
    data.append([names[i], jaccardIndex[i], NMIA[i], NVIM[i]])

with open('comparison_table.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)


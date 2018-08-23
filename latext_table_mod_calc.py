
"""
Name: Latex Table Generator based on Modularity Calculation
Author: Pablo Eliseo Reynoso Aguirre
Date: May 7, 2017
Desrcription: Generates a latex table based on radatools modularity computation files.

"""

networks_names = [

    "20x2+5x2",
    "graph3+1+3",
    "graph4+4",
    "star",
    "256_4_4_2_15_18_p",
    "256_4_4_4_13_18_p",
    "rb125",
    "cat_cortex_sim",
    "dolphins",
    "football",
    "zachary_unwh"

];

measures = ['Network', 'Partition', 'Overall Modularity Q', 'Modularity Q(1)'];
with open('modularity_calculations.txt', 'r') as f:
    lines = f.readlines();

data = [];


def remove_paths(file_name):

    if 'A3_nets/toy/' in file_name:
        file_name = file_name.replace('A3_nets/toy/', ' ');
    if 'A3_nets/model/' in file_name:
        file_name = file_name.replace('A3_nets/model/', ' ');
    if 'A3_nets/real/' in file_name:
        file_name = file_name.replace('A3_nets/real/', ' ');
    if 'comm_detection/' in file_name:
        file_name = file_name.replace('comm_detection/', ' ');
    return file_name.split('.')[0];

for i in range(len(lines)):
    if 'A3_nets/' in lines[i]:

        name_line = lines[i].split(' + ');
        network = name_line[0];
        network = remove_paths(network);
        partition = name_line[1].split(' ')[0];
        partition = remove_paths(partition);
        overall_mod = lines[i+1].split('=')[1].split('=')[0];
        modularity_q1 = lines[i+2].split('=')[1].split('=')[0];

        data.append([network, partition, overall_mod, modularity_q1]);



latex_tables = [];


latex_table_header = "\n\obegin{quote}\n\obegin{table}[htb]\n\centering\n\obegin{tabular}{S[table-format=1.1]S[table-format=-1.1]S[table-format=-1.1]S[table-format=-1.1,table-auto-round=false]}\otoprule";
latex_table_headerf = "\n{$ Network $}   & {$ Partiton $}  & {$ Q $} & {$ Q(1) $} \o\ \midrule";
latex_table_footer = "\n\end{tabular}\n\caption{Partitions comparissons in network ABCD}\n\label{tab:networks_models}\n\end{table}\n\end{quote}";


for network_name in networks_names:
    latex_lines = "";
    i = 1;
    for row in data:
        if network_name in row[0]:

            latex_line = "\n{$ " + row[0].strip() + " $} & " + "{$ " + row[1].strip() + "$} & {$ "+ row[2].strip() + "$} & {$ " + row[3].strip() + "$} \o\ ";
            latex_lines += latex_line;
            # print(latex_line);
            if i == 9:
                latex_lines += "\obottomrule";
            i += 1;
    latex_tables.append(latex_table_header + latex_table_headerf + latex_lines + latex_table_footer);


print(latex_tables[1]);

latex_file = open("../latex_table_modularity_calculations.txt", "w");
for table in latex_tables:
    latex_file.write(table);
latex_file.close()




"""
Name: Latex Table Generator based on Partition Comparisson
Author: Pablo Eliseo Reynoso Aguirre
Date: May 7, 2017
Desrcription: Generates a latex table based on radatools partition comparisson files.

"""

measures = ["Network name", 'Jaccard Index', 'Normalized Arithmetic Mutual Information', 'Normalized Variation of Information'];

networks_paths = [

    "../A3_nets/toy/partition_comp/20x2+5x2_",
    "../A3_nets/toy/partition_comp/graph3+1+3_",
    "../A3_nets/toy/partition_comp/graph4+4_",
    "../A3_nets/toy/partition_comp/star_",
    "../A3_nets/model/partition_comp/256_4_4_2_15_18_p_",
    "../A3_nets/model/partition_comp/256_4_4_4_13_18_p_",
    "../A3_nets/model/partition_comp/rb125_1_",
    "../A3_nets/model/partition_comp/rb125_2_",
    "../A3_nets/model/partition_comp/rb125_3_",
    "../A3_nets/real/partition_comp/cat_cortex_sim_",
    "../A3_nets/real/partition_comp/dolphins_",
    "../A3_nets/real/partition_comp/football_",
    "../A3_nets/real/partition_comp/zachary_unwh_"

];

partition_algorithms = [

    "rw3_ctsv",
    "rw50_ctsv",
    "rw300_ctsv",
    "l_ctsv",
    "lp_ctsv",
    "lev1_ctsv",
    "lev10_ctsv",
    "lev100_ctsv"

];

file_ext = ".txt";

latex_tables = [];


latex_table_header = "\n\obegin{quote}\n\obegin{table}[htb]\n\centering\n\obegin{tabular}{S[table-format=1.1]S[table-format=-1.1]S[table-format=-1.1]S[table-format=-1.1]S[table-format=-1.1,table-auto-round=false]}\otoprule";
latex_table_headerf = "\n{$ network\_partition_1 $}   & {$ network\_partition_2 $}  & {$ Jaccard Index $} & {$ 'Normalized Arithmetic Mutual Information' $} & {$ Normalized Variation of Information $}  \o\ \midrule";
latex_table_footer = "\n\end{tabular}\n\caption{Partitions comparissons in network ABCD}\n\label{tab:networks_models}\n\end{table}\n\end{quote}";



for path in networks_paths:
    latex_lines = "";
    i = 1;
    for algorithm in partition_algorithms:
        with open(path+algorithm+file_ext, "r") as f:
            lines = f.readlines()
            latex_line = "\n{$ "+lines[0].split("/")[2].strip()+" $} & "+"{$ "+lines[1].split("/")[3].strip()+"$} & {$ "+lines[13].split(":")[1].strip()+"$} & {$ "+lines[19].split(":")[1].strip()+"$} & {$ "+lines[29].split(":")[1].strip()+"$} \o\ ";
            latex_lines += latex_line;
            #print(latex_line);
        if i == len(partition_algorithms):
            latex_lines += "\obottomrule";
        i+=1;
    latex_tables.append(latex_table_header+latex_table_headerf+latex_lines+latex_table_footer);


print(latex_tables[1]);

latex_file = open("../latex_table_partition_comparissons.txt", "w");
for table in latex_tables:
    latex_file.write(table);
latex_file.close()



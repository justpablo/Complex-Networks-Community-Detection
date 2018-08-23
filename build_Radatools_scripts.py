# Automatically generates comparePartitions.sh, computeModularity.sh and detectPartitionsExtended.sh
import os

heuristics = ["srfr"]
if not os.path.exists("code/partition_results"):
    os.mkdir("code/partition_results")

# Generate comparePartitions.sh ########################################################################################
net2path = {'20x2+5x2': '../A3-networks/toy/',
            'graph3+1+3': '../A3-networks/toy/',
            'graph4+4': '../A3-networks/toy/',
            'star': '../A3-networks/toy/',
            '256': '../A3-networks/model/',
            'rb125': '../A3-networks/model/',
            'cat': '../A3-networks/real/',
            'dolphins': '../A3-networks/real/',
            'football': '../A3-networks/real/',
            'zachary': '../A3-networks/real/'}

origPRaw = sorted(os.listdir("A3-networks/toy"))
origPRaw.extend(sorted(os.listdir("A3-networks/model")))
origPRaw.extend(sorted(os.listdir("A3-networks/real")))
origPartitions = [name for name in origPRaw if 'clu' in name]
partitionsRaw = sorted(os.listdir("code/partition_results"))
partitions = [name for name in partitionsRaw if ('.txt' not in name and 'airports' not in name)]

file = open('code/comparePartitions.sh', 'w')
file.write('mkdir -p comparison_results\n')
k = 1
for partition in partitions:
    if 'rb125' in partition:
        key = [elem for elem in net2path.keys() if elem in partition]
        origPart = [elem for elem in origPartitions if elem.split('.')[0].split('-')[0] in partition]
        command = "../radatools-4.0-linux64/Communities_Tools/Compare_Partitions.exe " + net2path[key[0]] + 'rb125-1.clu' + \
                  ' partition_results/' + partition + ' comparison_results/out' + str(k) + '.txt 4\n'
        k += 1
        file.write(command)
        command = "../radatools-4.0-linux64/Communities_Tools/Compare_Partitions.exe " + net2path[
            key[0]] + 'rb125-2.clu' + \
                  ' partition_results/' + partition + ' comparison_results/out' + str(k) + '.txt 4\n'
        k += 1
        file.write(command)
        command = "../radatools-4.0-linux64/Communities_Tools/Compare_Partitions.exe " + net2path[
            key[0]] + 'rb125-3.clu' + \
                  ' partition_results/' + partition + ' comparison_results/out' + str(k) + '.txt 4\n'
        k += 1
        file.write(command)
    else:
        key = [elem for elem in net2path.keys() if elem in partition]
        origPart = [elem for elem in origPartitions if elem.split('.')[0].split('-')[0] in partition]
        command = "../radatools-4.0-linux64/Communities_Tools/Compare_Partitions.exe " + net2path[key[0]] + origPart[0] + \
                  ' partition_results/' + partition + ' comparison_results/out' + str(k) + '.txt 4\n'
        k += 1
        file.write(command)

file.write(r'printf "\n########################################################\n" > comparison_results.txt' + '\n')
for i in range(k-1):
    file.write("less comparison_results/out" +str(i+1)+ ".txt >> comparison_results.txt\n")
    file.write(
        r'printf "\n########################################################\n" >> comparison_results.txt' + '\n')
file.close()


# Create modularityComputation.sh ######################################################################################
partitionsRaw = sorted(os.listdir("code/partition_results"))
partitions = [name for name in partitionsRaw if '.txt' not in name]
origNet = sorted(os.listdir("A3-networks/toy"))
originalNetworks = ["A3-networks/toy/" + name for name in origNet if '.net' in name]
originalPartitions = ["../A3-networks/toy/" + name for name in origNet if '.clu' in name]
origNet = sorted(os.listdir("A3-networks/model"))
originalNetworks.extend(["A3-networks/model/" + name for name in origNet if '.net' in name])
originalPartitions.extend(["../A3-networks/model/" + name for name in origNet if '.clu' in name])
origNet = sorted(os.listdir("A3-networks/real"))
originalNetworks.extend(["A3-networks/real/" + name for name in origNet if '.net' in name])
originalPartitions.extend(["../A3-networks/real/" + name for name in origNet if '.clu' in name])
originalPartitions.extend(['partition_results/' + elem for elem in partitions])

file = open('code/computeModularity.sh', 'w')
for originalNet in originalNetworks:
    for part in originalPartitions:
        if originalNet.split('/')[2].split('.')[0] in part:
            file.write('../radatools-4.0-linux64/Communities_Tools/Modularity_Calculation.exe ' + '../' + originalNet +
                       ' ' + part + ' UN 4\n')

file.close()

"""
# create detectPartitionsExtended.sh ###################################################################################

input = open('code/detectCommunitiesReference.sh', 'r')
output = open('code/detectCommunitiesExtended.sh', 'w')
content = input.read()
for h in heuristics:
    current = content
    output.write(current.replace("heuristicName", h))

input.close()
output.close()
"""

import os, shutil
from collections import Counter
import pandas as pd


def clean_files():
    folders = ["./intermediate_opcode_clean", "./intermediate_opcode_malware",
              "./opcode_freq_clean", "./opcode_freq_malware"]
    for each_folder in folders:
        for the_file in os.listdir(each_folder):
            file_path = os.path.join(each_folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

def write_files(filepath, flag):
    if flag == 0:
        folder_name = "cleanFiles"
        inter_opcode = "intermediate_opcode_clean"
    else:
        folder_name = "malwareFiles"
        inter_opcode = "intermediate_opcode_malware"

    with open("./" + folder_name + "/" + filepath, "r") as f:
        all_opcode = list()
        for line in f:
            line = line[75:]
            line = line.split(" ")
            if not line[0]:
                if len(line) >= 2 and "0x" not in line[1]:
                    all_opcode.append(line[1])
            else:
                if len(line) >= 2 and "0x" not in line[0]:
                    all_opcode.append(line[0])
        with open("./"+ inter_opcode + "/" + filepath, "a+") as r:
            for each_op in all_opcode:
                if "\n" in each_op:
                    r.write(str(each_op))
                else:
                    r.write(str(each_op))
                    r.write("\n")
    return all_opcode


def write_individual_freq(opcodes, each_file, flag):
    if flag == 0:
        opcode_freq_folder = "opcode_freq_clean"
    else:
        opcode_freq_folder = "opcode_freq_malware"

    with open("./" + opcode_freq_folder + "/" + each_file, "a+") as opcode_frq:
        freq = Counter(opcodes)
        for key, value in freq.items():
            if "\n" in key:
                opcode_frq.write(str(value) + " " + str(key))
            else:
                opcode_frq.write(str(value) + " " + str(key))
                opcode_frq.write("\n")
                print("individual file writes done")


def make_csv(global_dict, global_count_clean, global_count_malware):
    print("i was called")
    print(global_count_clean)
    global_dict = Counter(global_dict)
    dataframe = pd.DataFrame(columns=global_dict.keys())
    for each_malware in global_count_malware:
        each_malware = Counter(each_malware)
        dataframe = dataframe.append([each_malware], ignore_index=True)
    for each_clean in global_count_clean:
        each_clean = Counter(each_clean)
        dataframe = dataframe.append([each_clean], ignore_index= True)
    dataframe = dataframe.fillna(0)
    print(dataframe)
    dataframe.to_csv("features.csv", encoding='utf-8', index=False)
    print("csv should be there")


if __name__ == "__main__":
    flag = 0
    global_dict = list()
    global_count_clean = list()
    global_count_malware = list()
    clean_files()
    for i in range(2):
        if flag == 0:
            folder_name = "cleanFiles"
        else:
            folder_name = "malwareFiles"
        for clean_files in os.walk("./" + folder_name):
            for each_file in clean_files[2]:
                opcodes = write_files(each_file, flag)
                global_dict.extend(opcodes)
                if folder_name == "malwareFiles":
                    opcodes.append('malware')
                    global_count_malware.append(opcodes)
                else:
                    opcodes.append('clean')
                    global_count_clean.append(opcodes)
                write_individual_freq(opcodes, each_file, flag)
        flag = 1
    print("The work is done")
    global_dict.append("class")
    print("calling makecsv")
    make_csv(global_dict, global_count_clean, global_count_malware)





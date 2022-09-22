import re
from ctb_src import collectTag
import os
from pathlib import Path

def get_tag_length(lst):
    main_lst = []
    sup_lst = []
    for i, tag in enumerate(lst):
        if "-U-" in tag:
            print('oo')
            if sup_lst:
                main_lst.append(sup_lst)
                sup_lst = []
            main_lst.append([tag])
        else:

            if "-B-" in tag:
                if sup_lst:
                    main_lst.append(sup_lst)
                    sup_lst = []
                else:
                    pass
            sup_lst.append(tag)
             #print(tag,sup_lst)
            # last case
    if "-L-" in tag:
        main_lst.append(sup_lst)
        sup_lst = []
    else:
        if i == len(lst) - 1 and "-U-" not in tag:
            main_lst.append(sup_lst)
            sup_lst = []
    return main_lst



def recover_data(fake_dict, lines):
    fun = lambda lst: lst.pop(0)
    tags = fake_dict.keys()
    new_file = []  # just init
    for tag in tags:
        pattern="\[\("+tag+"-[A-Z]-[A-Za-z]+-[A-Z]{0,2}-{0,1}\d+\)\]"
        synthetic_data = fake_dict[tag]
        if new_file:
            lines = new_file.copy()
            new_file = []
        for line in lines:
            new_line = []
            for word in line.split():

                if re.search(re.compile(pattern), word):
                    text = re.search(re.compile(pattern), word)[0][2:-2]
                    prev_tag = synthetic_data['tags'][0].replace(' ', '-')
                    if prev_tag == text:
                        value = fun(synthetic_data['value'])
                        _ = fun(synthetic_data['tags'])
                        new_line.append(value)
                    else:
                        print(synthetic_data['tags'][0],text)
                        # assert False "Tag mismatch"
                        quit("Need to check")
                else:
                    new_line.append(word)
            new_file.append(" ".join(new_line))
    return new_file




src_path='input/bill.txt'
des_path='output/out_sample_dl.txt'




def correction_curr(text):
    text = re.sub("-Float-WC ", "-Float-WC-", text)
    text = re.sub("-Float-C ", "-Float-C-", text)
    return text




def main(src_path, des_path):
    fake_data = {}
    data = open(src_path, 'r').read()
    collect = collectTag()
    tag_names = ['Full_Name', 'Account_number', 'Reference_number', 'Date_Of_Issue', 'Client_Address', 'Total_Amount_Due']
    for tag in tag_names:
        pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
        # pattern = "" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+"
        all_tag_list = re.findall(re.compile(pattern), data)
        all_tag_list = [tag[2:-2] for tag in all_tag_list]
        if all_tag_list:
            tag_length = get_tag_length(all_tag_list)
            new_dict = collect.call_tags(tag, tag_length)
            fake_data[tag] = new_dict
            print(tag_length)
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print(new_dict)
        else:
            new_dict = {"parent_name": [], "value": [], 'tags': []}
            fake_data[tag] = new_dict
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,', tag)
            
    data = correction_curr(data)
    lines = data.split('\n')
    file = recover_data(fake_data, lines)
    text = "\n".join(file)
    f = open(des_path, 'w')
    f.write(text)
    f.close()



result = main(src_path, des_path)
print(result)

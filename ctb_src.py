import pandas as pd
import numpy as np

data = open('Downloads/bill.txt', 'r').read()
data


# Date of issue
tag_names = ['Date_Of_Issue']

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


get_ipython().system('pip3 install Faker')


from faker import Faker
fake = Faker('en_GB')
print(fake.date())


import re
tag_names = ['Date_Of_Issue']
for tag in tag_names:
    pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
    all_tag_list = re.findall(re.compile(pattern), data)
    all_tag_list = [tag[2:-2] for tag in all_tag_list]
    tag_length = get_tag_length(all_tag_list)
    
print(tag_length)

tags_lst = [['Date_Of_Issue-U-Date-10']]

import datetime
def date_of_issue(tags_lst, multi_tag, same_length):
    start_date = datetime.date(year=1970, month=1, day=1)
    end_date = datetime.date(year=1999, month=1, day=1)
    doi = fake.date_between(start_date=start_date, end_date=end_date)
    eng_date = {1:'JAN' , 2:'FEB' , 3:'MAR' , 4:'APR' , 5:'MAY' , 6:'JUN' , 7:'JUL' , 8:'AUG' , 9:'SEP' , 10:'OCT' , 11:'NOV' , 12:'DEC'} 
    day = str(doi.day)
    en_month = eng_date[doi.month]
    year = str(doi.year)
    tags_flat = [item for sublist in tags_lst for item in sublist]
    dates_lst = []
    for single_tag in tags_lst:
        date_of_issue = day+'-'+en_month+'-'+year
        dates_lst.append(date_of_issue.split())
    
    dates_flat = [item for sublist in dates_lst for item in sublist]
    full_date = {"parent_name": '', "value": dates_flat, 'tags': tags_flat}
    
    return full_date


print(date_of_issue(tags_lst, True, True))


# Name
tag_names = ['Full_Name']
tag_names

import re
tag_names = ['Full_Name']
for tag in tag_names:
    pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
    all_tag_list = re.findall(re.compile(pattern), data)
    all_tag_list = [tag[2:-2] for tag in all_tag_list]
    tag_length = get_tag_length(all_tag_list)
    
print(tag_length)


def create_name(tag_length, multi_tag, same_length, length):
    names = [fake.name().split() for _ in range(200)]
    flat_list = [item for sublist in names for item in sublist]
    tags_flat = [item for sublist in tag_length for item in sublist]
    name_lst = []
    for single_lst in tag_length:
        parent_name = fake.random_elements(elements=flat_list, length=len(single_lst), unique=False)
        lst2 = ['Mrs', 'Mr', "Dr", "Ms"]
        for ele in lst2:
            try:
                index = parent_name.index(ele)
                if index:
                    parent_name[0], parent_name[index] = parent_name[index], parent_name[0]
            except:
                pass
        name_lst.append(parent_name)

    name_flat = [item for sublist in name_lst for item in sublist]
    full_name = {"parent_name": '', "value": name_flat, 'tags': tags_flat}
    return full_name


print(create_name(tag_length, True, True, True))


# Account no.
tag_names = ['Account_number']
tag_names

import re
tag_names = ['Account_number']
for tag in tag_names:
    pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
    all_tag_list = re.findall(re.compile(pattern), data)
    all_tag_list = [tag[2:-2] for tag in all_tag_list]
    tag_length = get_tag_length(all_tag_list)
    
print(tag_length)   


def account_no(tag_length, multi_tag, same_length, length):
    pass_no=[]
    tags_flat = [item for sublist in tag_length for item in sublist]
    for single_tag in tag_length:
        _, _, _, acc_len = single_tag[0].split('-')
        digits = int(acc_len)
        num = str(fake.random_number(digits=digits,fix_len=True)).split()
        if len(single_tag)==1:
            pass_no.append(num)
        else:
            quit(" ACC_NUM", tags_flat)
            
    value = [item for sublist in pass_no for item in sublist]
    full = {"parent_name": '', "value": value, 'tags': tags_flat} 
    return full

print(account_no(tag_length, True, True, True))


# Reference number
tag_names = ['Reference_number']
tag_names

import re
tag_names = ['Reference_number']
for tag in tag_names:
    pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
    all_tag_list = re.findall(re.compile(pattern), data)
    all_tag_list = [tag[2:-2] for tag in all_tag_list]
    tag_length = get_tag_length(all_tag_list)
    
print(tag_length)   


def reference_no(tag_length, multi_tag, same_length, length):
    pass_no=[]
    tags_flat = [item for sublist in tag_length for item in sublist]
    for single_tag in tag_length:
        _, _, _, acc_len = single_tag[0].split('-')
        digits = int(acc_len)
        num = str(fake.random_number(digits=digits,fix_len=True)).split()
        if len(single_tag)==1:
            pass_no.append(num)
        else:
            quit(" REF_NUM", tags_flat)
            
    value = [item for sublist in pass_no for item in sublist]
    full = {"parent_name": '', "value": value, 'tags': tags_flat} 
    return full

print(reference_no(tag_length, True, True, True))


# Client Address
tag_names = ['Client_Address']
tag_names


import re
tag_names = ['Client_Address']
for tag in tag_names:
    pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
    all_tag_list = re.findall(re.compile(pattern), data)
    all_tag_list = [tag[2:-2] for tag in all_tag_list]
    tag_length = get_tag_length(all_tag_list)
    
print(tag_length)

tag_length = [['Client_Address-B-Alphanumeric-1', 'Client_Address-I-Alphanumeric-7', 'Client_Address-I-Alphanumeric-5', 'Client_Address-I-Alphanumeric-12', 'Client_Address-I-Alphanumeric-12', 'Client_Address-I-Alphanumeric-7', 'Client_Address-I-Alphanumeric-7', 'Client_Address-I-Alphanumeric-4', 'Client_Address-L-Alphanumeric-3', 'Client_Address-I-Alphanumeric-4', 'Client_Address-L-Alphanumeric-3']]

len((str(tag_length).split()))

def create_address(tag_length, multi_tag, same_length, length):
    tags_flat = [item for sublist in tag_length for item in sublist]
    city = [fake.city().split() for _ in range(20)]
    city_flat = [item for sublist in city for item in sublist]
    street = (' '.join(fake.street_address().split('\n'))).split()
    postcode = fake.postcode().split()
    street_len = len(street)
    postcode_len = len(postcode)
    data = []
    for single_tag in tag_length:
        tag_len = len(single_tag)
        sp_len = street_len + postcode_len
        new_len = tag_len - sp_len
        if new_len>0:
            cities = fake.random_elements(elements=city_flat, length=new_len, unique=False)
            address = street + cities + postcode
            data.append(address)
            print(address)
            #address = (' '.join(street) + ' ' + ' '.join(cities) + ' ' + ' '.join(postcode))
        else:
            new_street = street[:new_len]
            cities = fake.random_elements(elements=city_flat, length=1, unique=False)
            address = new_street + cities + postcode
            data.append(address)
    value = [item for sublist in data for item in sublist]
    full = {"parent_name": '', "value": value, 'tags': tags_flat}       
    return full      


print(create_address(tag_length, True, True, True))


# Total amount due
tag_names = ['Total_Amount_Due']
tag_names

import re
tag_names = ['Total_Amount_Due']
for tag in tag_names:
    pattern = "\[\(" + tag + "-[A-Z]-[A-Za-z]+-[A-Z]{0,2}\s{0,1}\d+\)\]"
    all_tag_list = re.findall(re.compile(pattern), data)
    all_tag_list = [tag[2:-2] for tag in all_tag_list]
    tag_length = get_tag_length(all_tag_list)
    
print(tag_length)

def amount_due(tag_length, multi_tag, same_length, length):
    amt_lst=[]
    tags_flat = [item for sublist in tag_length for item in sublist]
    for single_tag in tag_length:
        _, _, _, acc_len = single_tag[0].split('-')
        curr = acc_len.split()[0]
        print(curr)
        amt = fake.pricetag()
        if len(single_tag)==1:
            amtt = [amt.replace('$', '') if curr == 'WC' else amt.replace('$', '£')]
            amt_lst.append(amtt)
        else:
            for in_tag in single_tag:
                amtt = [amt.replace('$', '') if curr == 'WC' else amt.replace('$', '£')]
                amt_lst.append(amtt)
    value = [item for sublist in amt_lst for item in sublist]
    full = {"parent_name": '', "value": value, 'tags': tags_flat} 
    return full           


print(amount_due(tag_length, True, True, True))




# Replacing of text
class collectTag:
    def __init__(self):
        self.org = {}
    
    def call_tags(self, tag, tag_length):
        multi_tag= True if len(tag_length)>1 else False
        len_lst=[len(lst) for lst in tag_length]
        same_length=True if len(set(len_lst))==1 else False
        length= len_lst[0] if same_length else max(len_lst)
        if tag == 'Full_Name':
            new_dict = create_name(tag_length, multi_tag, same_length, length)
        elif tag == 'Account_number':
            new_dict = account_no(tag_length, multi_tag, same_length, length)
        elif tag == 'Reference_number':
            new_dict = reference_no(tag_length, multi_tag, same_length, length)    
        elif tag == 'Date_Of_Issue':
            new_dict = date_of_issue(tag_length, multi_tag, same_length)
        elif tag == 'Client_Address':
            new_dict = create_address(tag_length, multi_tag, same_length, length)
        elif tag == 'Total_Amount_Due':
            new_dict = amount_due(tag_length, multi_tag, same_length, length)    
        else:
            pass
        
        self.org[tag] = new_dict['parent_name']  
    
        return new_dict


import pandas as pd

def pairs_generator():
    #reading file with list of file names to be trained on
    data = pd.read_csv('D:\\nkasturi122817\\signatureverification\\NISDCC-offline-all-001-051-6g\\data.csv')
    ind = 0
    columns = ['ID','names', 'names_2', 'Label']
    pairs = pd.DataFrame(columns=columns)
    for index, rows in data.iterrows():
        for i in data[data.writers==rows.originals]['names']:
            pairs = pairs.append({'ID':ind ,'names': rows.names, 'names_2': i, 'Label': 'null'}, ignore_index=True)
            ind = ind+1
    return pairs


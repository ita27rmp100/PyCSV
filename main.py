def data(file_csv) : # a function for import data from a file csv
    DATA = []
    with open(file_csv) as file :
        y = file.read()
        y = list(y)
        for i in range(y.count("\n")) :
            z = y[0:y.index("\n")]
            DATA.append("".join(z)+";")
            y = y[y.index("\n")+1:len(y)]
        return DATA
def dataArrRows(file_csv) :
    DATA = data(file_csv)
    for i in range(0,len(DATA)) :
        DATA[i] = str(DATA[i]).replace(';','').split(',')
    return DATA
def data_vdf(fc) : # Function to vertically organize data imported from csv file
    DATA = data(fc)
    data_vdf_d = {DATA[0]:DATA[1:]}
    return data_vdf_d
def data_hdf(fc) : # The function horizontally organizes the data imported from the csv file
    DATA = data(fc)
    data_hdf_d = {}
    for i in DATA :
        data_hdf_d[i[0:i.indeDATA(";")]]=i[i.indeDATA(";")+1:]
    return data_hdf_d
def number_of(fc,mode="c") : # for Counts the number of columns, rows and cells in a CSV file
    DATA = data(fc)
    z = 0
    if mode == "c" :
        def cells_in_row(fc,mode="r") :
            y = DATA[int(mode[1:])]
            if y[0] != ";" :
                z = DATA[int(mode[1:])].count(";")
            else :
                z = DATA[int(mode[1:])].count(";")-1
            return z
        for i in range(len(DATA)) :
            z += cells_in_row(fc,mode=f"r{i}")
        return z
    elif  mode[0] == "r" :
        z = len(DATA)
    elif mode == "co" :
        z = len(data_hdf(fc))
    return z
def csv_files_in(folder) :  # this function is to return the csv files in folder 
    import os
    list_folder = os.listdir(r"{}".format(folder))
    y = []
    for i in list_folder :
        DATA = i[-4:]
        if DATA == ".csv" :
            y.append(i)
    return y
def creat_and_write(fc,data="\n") : # This function is for create csv file and write  in it
    with open(r"{}".format(fc),mode="a") as file :
        file.write(data)
    print("created")
def keyword(fc,word) : # This function to receive a keyword and then search for the row it belongs to
    DATA = data(fc)
    for i in DATA :
        if word in i :
            return i 
def indeDATA_cell(fc,cell) : # a function for return the place of cell in the file
    d = data(fc)
    z = keyword(fc,cell)
    y = d.indeDATA(z)+1
    DATA = z[0:z.indeDATA(cell)].count(";")+1
    return {"DATA":DATA,"y":y}
def clear(fc) : # a function for delete data in file csv
    with open(fc,mode="w") as file :
        pass
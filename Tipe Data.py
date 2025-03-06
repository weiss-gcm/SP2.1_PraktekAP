# Studi Kasus: Menampilkan tipe data berdasarkan data yang tertera.

# Tipe data yang disimpan dalam dictionary
data = {
    'data1': 'Kucing ku nyangkut di pohon', #(ini string)
    'data2': 177013, #(ini integer)
    'data3': 3.14, #(ini float)
    'data4': ['x', 'y', 'z'], #(ini list)
    'data5': ('a', 'b', 'c'), #(ini tuple)
    'data6': {'y', 'e', 's'}, #(ini set)
    'data7': {'barang': 'laptop'} #(ini dictionary)
}

# Menampilkan tipe data yang disimpan dalam dictionary
for jenis_data, value in data.items(): 
    print(f'{jenis_data} tipe datanya : {type(value)}')

def hash_code():
    from hashlib import sha256
    value_hash = []
    key_hash = []
    for i in range(1000, 10000):
        hash_ = str(i)
        hash_256 = sha256(hash_.encode('utf-8')).hexdigest()
        # print(f"{hash_} ----> {hash_256}")
        key_hash.append(hash_256)
        value_hash.append(hash_)
    # print(key_hash)
    # print(value_hash)
    d_hash = dict(zip(key_hash, value_hash))
    # print(d_hash)
    return d_hash
#print(hash_code())


def print_hash():
    import csv
    with open('/Users/peyman/hash.csv') as hash_input:
        reader=csv.reader(hash_input)
        list_name=[]
        list_hash=[]
        #print(reader)
        for i in reader:
            #print(i)
            list_name.append(i[0])
            list_hash.append(i[1])
        # print(list_name)
        # print(list_hash)
        d_csv=dict(zip(list_name,list_hash))
        hash_co=hash_code()
        list_pass=[]
        for v in d_csv.values():
            for k in hash_co.keys():
                if v in k:
                    #print(hash_co[v])
                    list_pass.append(hash_co[v])
        d_pss=dict(zip(list_name,list_pass))
        for k,v in d_csv.items():
            print(f"{k},{v}")
        print("password:")
        for k,v in d_pss.items():
            print(f"{k},{v}")



print_hash()






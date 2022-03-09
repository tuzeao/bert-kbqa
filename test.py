from test_func import process

def load_file(path,length):#all_message
    data=[]
    with open(path,'r') as f:
        for i in f:
            x=i.split('\t')
            if len(x)!=length:
                continue
            data.append(x)
    return data


data = [x[0] for x in load_file("test", 1)]
for query in data:
    result = process(query)
    print("\t".join(result))




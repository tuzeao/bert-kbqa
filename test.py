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

data = load_file("test", 1)
data = [x[0].strip() for x in data]
for query in data:
    result = process(query)
    print("\t".join(result))



import json


with open("hero_list.json",'r',encoding="utf-8") as load_f:
    data = load_f.read()
    #print(data)
    #print(type(data))
    dict_data = json.loads(data)
    print(dict_data)
    heros = dict_data['hero']
    #load_dict = json.load(load_f)
    #print(load_dict)
    print(heros)
    print(len(heros))
    for item in heros:
        #print(item)
        print(item['heroId'],"\t",item['name']," ",item['title'],"\t",item['alias'])
    load_f.close()
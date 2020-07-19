import json

name_emb = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
}

def json_dumps():
    '''
        將 dict 轉 str
    '''
    js_obj = json.dumps(name_emb)

    print(name_emb)
    print(type(name_emb))
    print(type(js_obj))


def json_loads():
    '''
        將 str 轉 dict
        open read 進來的都是 str 格式
    '''
    json_dumps = json.dumps(name_emb)
    json_loads = json.loads(json_dumps)

    print(name_emb)
    print(json_dumps)
    print(json_loads)
    print(type(name_emb))
    print(type(json_dumps))
    print(type(json_loads))

def json_dump():
    '''
        寫入 json file
    '''
    print(type(name_emb))
    json_dump = json.dumps(name_emb)
    print(type(json_dump))

    # method 1
    with open('./json_ex.json', 'w', encoding='utf8') as f:
        f.write(json_dump)

    # method 2
    json.dump(name_emb, open('./json_ex.json', 'w', encoding='utf-8'))

def json_load():
    '''
        讀取 json file
    '''

    json_load = json.load(open('./json_ex.json', 'r', encoding='utf-8'))
    print(json_load)
    print(type(json_load))
    for key in json_load.keys():
        print('key: %s  value: %s' % (key, json_load.get(key)))

json_load()
gg = {'Time / Traction': {'x': 'Time', 'y': 'Traction', 'obj': 'xaxa'}, 'Time / Weight': {'x': 'Time', 'y': 'Weight', 'obj': 'xaxa'}}



def aye(obj):
    if not isinstance(obj,dict):
        print("Данный обьект не является словарем!!!")
        return
    for name_graph, dictt in obj.items():
        if not "obj2" in dictt:
            dictt["obj2"] = "хихи"
    print(obj)

aye(gg)
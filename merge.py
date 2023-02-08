from modules.search import search

def merge(values, key1, key2):
    
    v = str(search(values, key2))
    for i in values[str(search(values, key2))]:
        values[str(search(values, key1))].append(i)
    values.pop(v)
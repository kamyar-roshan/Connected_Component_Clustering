def search(values, searchFor):
    
    for k in values:
        for c in values[str(k)]:
            if [searchFor] == c:
                return k
    return None
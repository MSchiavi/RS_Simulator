def format(items,quantity,value):
    results = []
    for i in range(0,len(items)):
        results.append([items[i],quantity[i],value[i]])
    return results
def Total(Formated):
    total = 0
    for i in range(0,len(Formated)):
        total = total + Formated[i][2]
    return total

def perhour(total,TripTime):
    return (total*3600)/(TripTime)

def tuples_to_dictionaries(data,keys):
    send = []
    data_length_not_same = False

    #if keys does not match size of each tuple then
    #a list index out of range will occur
    #thhus if size are not same then return with null
    for a in range(0,len(data)):
        if (len(data[a]) != len(keys)):
            data_length_not_same = True
            break

    if(not data_length_not_same):
        #take keys and put every row data in a dictionary
        #and then append it to a list
        for row in data:
            refinedata = {}
            for a in range(0, len(keys)):
                refinedata[keys[a]] = row[a]
            send.append(refinedata)

    return send

def tuple_to_onekeydic(data):
    send = {}
    data_length_not_same = False

    for a in range(0, len(data)):
        if (len(data[a]) < 2):
            data_length_not_same = True
            break

    if (not data_length_not_same):
        for a in data:
            send[a[0]] = a[1]

    return send

def make_dictionary(keys,values):

    send = {}
    if(len(keys) == len(values)):
        for index in range(0,len(keys)):
            send[keys[index]] = values[index]

    return send

def tuples_to_lists(data):
    send = []
    if(len(data) > 1 ):
        for t in data:
            tmp = []
            for a in t:
                tmp.append(a)
            send.append(tmp)
    return send

def lists_to_list(data):
    send = []
    if(len(data) > 1 ):
        for t in data:
            for a in t:
                send.append(a)
    return send

def tuple_to_list(data):
    send = []
    for t in data:
        send.append(t)
    return send


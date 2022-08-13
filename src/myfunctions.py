


def clean_spec(element,list,remain): # remain is the value that is given if no match is found, 'same' leaves the same value
    sk=[i.capitalize() for i in list if i in str(element).lower()]
    if sk==[]:
        if remain=='same':
            sk=element
        else:
            sk=remain
    else:
        sk=str(sk[0]) 
    return sk
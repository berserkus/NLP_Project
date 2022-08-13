from config.mongoconfig import c
# GET
# funciton to get info
def all_sentences(name):
    query={"character_name":f"{name}"} #Albus Dumbeldore
    sent= list(c.find(query,{"_id":0}))
    return sent


# POST
# 
def inserting(dict_):
    # function to insert info
    c.insert_one(dict_)
    return f"I inserted {dict_} into the db"
    

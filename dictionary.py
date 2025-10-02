dict = {
    "key" : "value" ,
    # samajhla na?

    "friends" : ["Waghya","Darshan","Nihar","Neelya"],
    "family" : ("Datta","Chhaya","Rohan","Kirteesh"),
    "age" : 19,
    "CGPA" : 8.1,
    "Am i Goated ?" : True,
}
print(dict["CGPA"])
dict["CGPA"]= 9.8 #overwrite
print(dict["CGPA"])
null_dict = {
    "name" : "Kirteesh D. Rakshe",
    "CET" : {
        "physics" : "96",
        "chem" : "97",        #a dictionary in a dictionary , is called nested dictionary...
        "maths" : "98",
    }
    } 
print(null_dict)
print(null_dict["CET"]["chem"])  #can access values in the new dict .
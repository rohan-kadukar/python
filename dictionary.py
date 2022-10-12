#  Dictory
dic={"Rohan":{"1":"75","2":"93","3":"NA"},"Rohit":"95","Pankaj":"88","Sagar":"99"}
print(dic["Rohit"])
print(dic["Rohan"]["1"])
dic["Aditya"]="755"
print(dic)
dic["Omkar"]={"1":"888","2":"999"}
print(dic)
del dic["Omkar"]
print(dic)
# create new dic1 and get pointer of dic
dic1=dic
del dic1["Aditya"]
print(dic) # It delete Aditya becayse we assin the pointer to dic1
# Thats why we use copy function
dic2=dic.copy()
del dic2["Sagar"]    #it delete element of dic2 not dic
print("dic= ",dic)
print("dic2= ",dic2)
# Getting value 
print(dic.get("Pankaj"))
dic.update({"A":"11"})
print(dic)
# for getting dictionaries keys
print(dic.keys())
# for getting dictionaries items
print(dic.items())

import json

# Reading json file

myfile=open('problem.json','r')
data=myfile.read()

#validate json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True



#try:
#    with open('problem.json') as json_file:
#        data = json.load(json_file)
#        isvalid =  validateJSON(data)
#        if (isvalid == True):
#            # Print the type of data variable
#            print("Type:", type(data))
#            # Print the data of dictionary
#            print("\n",data)
#        else:
#            error = "The file is not json valid"
#            f = open("error_log.txt", "a")
#            f.write('\n')
#            
#            f.write(str(current_datetime()))
#
#            # writing in the file
#            f.write(str(error))
#            # closing the file
#            f.close()
#except Exception as Argument:
#    logging.exception("\t Error!!, This is not a valid path.\n")
#    # creating/opening a file
#    f = open("error_log.txt", "a")
#    f.write('\n')
#
#   f.write(str(current_datetime()))
#
#    # writing in the file
#    f.write(str(Argument))
#    # closing the file
#    f.close()

#Comverting into dictionary

jobj=json.loads(data)

#functions 

def rev_str(str):
    return str[::-1]


def sqr_num(num):
    return (num**2)


# Create your dictionary class
#class my_dictionary(dict):
 
  # __init__ function
  #def __init__(self):
   # self = dict()
 
  # Function to add key:value
#  def add(self, key, value):
 #   self[key] = value
 
 
# Main Function
#dict_obj = my_dictionary()


#creating operations

def operation(jobj):
    list_demo = []              ######3
    for v in jobj.values():
        if type(v)==str:
            a=rev_str(v)
            #print(a)
            list_demo.append(a)
            print("data added into list")
        elif type(v)==int and float:
            b=sqr_num(v)
            #print(b)
            list_demo.append(b)
            print("data added into list")

        elif type(v)==list:
            result_list = []
            for i in v:
                if type(i)==str:
                    c=rev_str(i)
                    result_list.append(c)
                elif type(i)== int and float:
                    d=sqr_num(i)
                    result_list.append(d)
                elif type(i) == list:
                    nested_list=[]
                    for j in i:
                        if type(j)==str:
                            c=rev_str(j)
                            nested_list.append(c)
                        elif type(j)==int and float:
                            d=sqr_num(j)
                            nested_list.append(d)
                    result_list.append(nested_list)
            list_demo.append(result_list)
    return list_demo
                    

dict_values = list(operation(jobj))

dict_keys = jobj.keys()
dict_keys


res = {}
for key in dict_keys:
    for value in dict_values:
        res[key] = value
        dict_values.remove(value)
        

#print(res)

print("FINAL OUTPUT DECTIONARY = " + repr(res))

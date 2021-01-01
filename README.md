# Freshworks---Engineering---Assignment


Build a file-based Key-Value data Store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as a local storage for one single process on one laptop. The data store must be exposed as a library to clients that can instantiate a class and work
with the data store. The data store will support the following functional requirements

# Languages:
Ideally, we would not restrict you from working on a language of your choice. However, it would be preferable if you stick with one of these -
• NodeJS
• Java
• Python
• GoLang
• Ruby
• C/C++
# Submission:
Submit a link to the source code, ideally committed to Github.
Code accompanied by thorough unit tests is typically a mark of quality work.
Ideally, your data store will work on most operating systems. If this is not the case, please specify which OSes are supported.







## Importent Note: - We can Perform Update Operation By using Updatedata(key, value)    i.e : -

def updatedata(key,value):
    b=database[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in database:
                print("Error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                database[key]=l
        else:
            print("Error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in database:
            print("Error: Key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            database[key]=l
            print("Value for",key,"updated to",value)

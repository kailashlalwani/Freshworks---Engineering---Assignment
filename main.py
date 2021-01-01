import os
from threading import *
import time

#'database' is the database, dictionary in which we store the data
database={} 



#for create operation 
def createdata(key,value,timeout=0):
#use syntax "createdata(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout that is given into Problem
    if key in database:  # Check if given key is already store in Database
        print("error: this key already exists") #error message1, Because key is already in Database
    else:
        if(key.isalpha()):
            if len(database)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jason object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:  #constraints for input key_name capped at 32chars
                    database[key]=l
                print("Key",key,"with value",value,"successfully Created!")
            else:
                print("error: Memory limit exceeded!! ")    #error message2, because of memory limit extened
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")   #error message3, Because we insert special chaackers intoi key- value



#for read operation
def readdata(key): #use syntax "readdata(key_name)"
    if key not in database:     # Ckeck if given key existing in Database or not..?
        print("error: given key does not exist in database. Please enter a valid key")  #error message4, because entered key not in database
    else:
        b=database[key]
        if b[1]!=0:
            if time.time()<b[1]:    #compare the present time with the expire time
                stri=str(key)+":"+str(b[0])  #to return the value in the format of Jason Object i.e. "key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5, Because of given time is over
        else:
            stri=str(key)+":"+str(b[0])
            return stri


#for delete operation
def deletedata(key): # use syntax "deletedata(key_name)"
    if key not in database:     # Check whether key available in Database or not...? 
        print("error: given key does not exist in database. Please enter a valid key") #error message, Because key not existing in Database
    else:
        b=database[key]
        if b[1]!=0:
            if time.time()<b[1]: #ompare the present time with the expire time
                del database[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #error message5, Because of given time is over
        else:
            del database[key]
            print("key",key,"is successfully deleted")   # Database key is deleted successfully





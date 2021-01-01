import main as run
'''
This file is to display the use of the script.
This is the file made of the sample interactive mode.
all outputs are declared as comments below each line of code respectively.
'''

#imported the main file as a library

#creating key-value pair data to store in local system
run.createdata("Kailash",22)
#Key Kailash with the value 22 creation successfully !

res = run.readdata("Kailash") #returns JSON object
print(res)
#Kailash:22

#if entered duplicate key, shows error
run.createdata("Kailash",30)
#error:key already exists

#Using TIME-TO-LIVE property
run.createdata("Jaipur",14,360) #time-360 seconds
#Key Jaipur with value 14 creation successful!
res = run.readdata("Jaipur")
print(res)
#Jaipur:14


#after 360 seconds
res = run.readdata("Jaipur")
#error: time-to-live of Jaipur has expired


#to delete data and free memory
run.deletedata("Kailash")
## key Kailash is successfully deleted
print(run.readdata("Kailash"))
#error: given key does not exist in database. Please enter a valid key


#entering wrong key name
res = run.readdata("Manan")
#error: given key does not exist in database. Please enter a valid key

#wrong key name while creation
run.createdata("Manan_12",20)
#error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers




#This code also returns other errors:  
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

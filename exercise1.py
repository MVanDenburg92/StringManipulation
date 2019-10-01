# Name: Miles Van Denburg
# Assignment title: OldMacdonald Capitalization
# Time to complete: 20 minutes
# Description: Capitalize the 1st and 4th letters in the name "Old MacDonald"

#Created a function with takes input "name1"
#The function slices first letter value at index 0 and the 4th letter value at index 4, capitalizing them using the .capitlalize method.
#The sliced sections of the name are concatenated together along with the none capitalized sections of the name and stored in name2
#The function then returns the value within name2
#The value of name2 is then printed.  
def old_macdonald(name1):
        name2 = name1[0].capitalize() + name1[1:3] + name1[4:5].capitalize() + name1[5:]
        return name2
print(old_macdonald("old macdonald"))




#def old_macdonald(name):
    #name2 = name.capitalize()
    #name2 = []
    #name2 = name.split()
    #name2[0,3.upper()
    #name 3 = name2.join()
    #print(name2)
    
#old_macdonald(name)
    ##for i in name2
        ##if i == 0
        # replace this line with code
          
#def old_macdonald(name):
    #print("Enter in a word to capitalize the 1sta and 4th character)
    #index = 0
    #for i in name
    #   if name[0].islower():
            #return name[0].capitalize() + name[1:4] + name[4:5]
       #elif ireturn name2
    #else:
       #print("You done goofed")

#print(old_macdonald("timmy"))


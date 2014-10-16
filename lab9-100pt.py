
############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.



print "A Ebola approaches! Prepare to fight!"


a= True

while(a):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "You have a Fever!                                              "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "What is your Temperature?                                      "
    print "1. A tempurature above 100F and been to West africa recently   "
    print "2. A temperature over 102F and have been sick in the last 24Hrs"
    print "3. A temperature over 105F                                     "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    userInput = int(raw_input())
    if userInput == 1:
        print "Sir you.... DO have ebola!"
        print "Please step to the side for Decontamination"
        print "Sorry! I meant to say Decapitation! Have fun!"
        a = False
    elif userInput == 2:
        print "Sir you... DO.......NT have ebola! You have what is known as a 'Common Cold'."
        print "You will be released after you fill out your paperwork"
    elif userInput == 3:
        print "Sir you.... DO have ebola!"
        print "Please step to the side for Decontamination"
        print "Sorry! I meant to say Decapitation! Have fun!"
        a = False
    elif userInput > 3: 
        print "That wasnt an option. Answer correctly please"




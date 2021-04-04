## This will help track calls on a daily basis
from time import time, ctime

print("Thanks for using the ticket script. please follow the instructions below: ")
print("When you are asked for the company number, use the following guide: ")
print("0 for A \n 1 for company b\n 2 for company c \n 3 for company d")

class Printing():
    name = input("Thank you for calling the service desk, my name is john, can I have your first and last name please? ")
    companytuple = ("A", "B", "C", "D")
    company = companytuple[int(input("Enter company #"))]
    print(company)
    ctype = input("Is this reguarding a new or existing issue?")

## This will run when we have a new call
    if ctype == 'new':
        description = input("What is the issue you are having? ")
        password = input('is this a password issue? ')
        if password == 'yes':
            pwissue = input("Is the account locked out? ")
            if pwissue == 'yes':
                print('I unlocked your account ')
            elif pwissue == 'no':
                    print('I reset your password ')
            else:
                pass
        elif password == 'no':
            length = input("When did this occur? ")
            trouble = input("Did you do any troubleshooting? ")
            metroub = input("Troubleshooting I did ")
            esc = input("escallated? ")
            print("Ticket script:")
            finalfile = print("at ", ctime(time()), " ",name, " called from ", company,", reporting that they",description,". They did the following troubleshooting steps: ", trouble,". While on the phone, I did the following troubleshooting steps: ",metroub,". Did I escallate? ",esc )
            if trouble is None:
                print(trouble)
            else:
                pass
    elif ctype == 'existing':
        tickno = input("Whats your ticket number? ")
        if tickno is None:
                print("Ok let me look it up by your name, one moment. ")
                #once you find it
                checkup = input("What are we calling about today?")
                if checkup == 'Follow Up':
                    print("Ok let me look at the ticket")
                    happen = input("What happened with the ticket?")
                    print(name,"called in to check up on an existing ticket. The update of the ticket was given as", happen, "a follow up on this phone call will happen if nessessary")
                elif checkup == 'Resolved':
                    selfresolve = input("How did the incident get resolved? ")
                    print(name,"called in to advise us that the issue was self-resolved under the following information: ",selfresolve)
                    print("Go ahead and close the ticket")
                elif checkup == 'Broken':
                    newissue = input("What is the new issue that we need to re-open the ticket for? ")
                    newsteps = input("What additional troubleshooting steps did the user take? ")
                    newengst = input("What additional troubleshooting steps did the engineer take? ")
                    escto = input("Are we escallating this ticket? ")
                else:
                    pass
                    
        else:
            checkup = input("What are we calling about today?")
            if checkup == 'Follow Up':
                print("Ok let me look at the ticket")
                happen = input("What happened with the ticket?")
                print(name,"called in to check up on an existing ticket. The update of the ticket was given as", happen, "a follow up on this phone call will happen if nessessary")
            elif checkup == 'Resolved':
                selfresolve = input("How did the incident get resolved? ")
                print(name,"called in to advise us that the issue was self-resolved under the following information: ",selfresolve)
                print("Go ahead and close the ticket")
            elif checkup == 'Broken':
                newissue = input("What is the new issue that we need to re-open the ticket for? ")
                newsteps = input("What additional troubleshooting steps did the user take? ")
                newengst = input("What additional troubleshooting steps did the engineer take? ")
                escto = input("Are we escallating this ticket? ")
            else:
                pass


Printing()



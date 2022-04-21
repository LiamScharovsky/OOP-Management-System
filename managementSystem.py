class Lists ():
    def __init__(self):
        self.managerList = []
        self.allList = []
        self.teamsList = []
        self.employee = []
    def putLists(self, employees):
        self.employee = employees
        if self.employee[1] == "yes":
            self.managerList.append(self.employee[0])
        self.allList.append(self.employee[0])
        self.teamsList.append(self.employee[2])
        self.teamsList = list(dict.fromkeys(self.teamsList))
        return (self.managerList, self.allList, self.teamsList)
    

        
class Inputting():    
    def __init__ (self):
        self.manager = ""
        self.team=""
        self.yesOrNo= []
        self.managerList = []
        self.allList = []
        self.teamsList = []
    def run(self):
        lists = Lists()
        while True:
                    self.yesOrNo = []
                    decision = input("Is it a manager? ").lower()
                    if decision == "yes":
                        firstName = input("What's the employee's first name? ")
                        lastName = input ("What's the employee's last name? ")
                        title = input("What's the employees title? ")
                        self.team = input("What team do they manage? ")
                        self.manager = "yes"
                        email = firstName+lastName+"@gmail.com"
                        employees = [firstName, lastName, title, self.team, email]
                        self.yesOrNo = [employees, self.manager, self.team]

                    if decision == "no":
                        firstName = input("What's the employee's first name? ")
                        lastName = input ("What's the employee's last name? ")
                        title = input("What's the employees title? ")
                        self.team = input("What team are they in? ")
                        self.manager = "no"
                        email = firstName+lastName+"@gmail.com"
                        employees =[firstName, lastName, title, self.team, email]
                        self.yesOrNo = [employees, self.manager, self.team]
                    
                    allLists = lists.putLists(self.yesOrNo)
                    self.managerList.append(allLists[0])
                    self.allList.append(allLists[1])
                    self.teamsList.append(allLists[2])
                    decision = input("Would you like to input another employee? ")
                    if decision == "no":
                        break
        #print (allLists)
    def getManagers(self):
        return self.managerList
    def getTeams(self):
        for teams in self.teamsList:
            for next in self.teamsList:
                if teams == next:
                    self.teamsList.remove(teams)
        return self.teamsList
    def getAll(self):
        return self.allList
    def deleteEmp (self, email):
        for employee in self.allList:
            if employee[-1] == email:
                self.allList.remove(employee)
                for emp in self.managerList:
                    if emp == employee:
                        self.managerList.remove(employee)

class Main(object):
    def run(self):
        lists = Lists()
        inputting = Inputting()
        while True:
            decision = input("Click 1 to add an employee, click 2 to see employee list, click 3 to delete an employee, click 9 to exit. ")    
            if decision == "1":
                print(inputting.run())
            if decision == "2":
                newdecision = input ("Click 1 to see the teams, click 2 to see a managers list, or click 3 to see a full directory ")
                if newdecision == "1": 
                    print (inputting.getTeams())
                if newdecision == "2":
                    print (inputting.getManagers())
                if newdecision == "3":
                    print (inputting.getAll())
            if decision == "3":
                newdecision = input("Enter employees' email: ")
                inputting.deleteEmp(newdecision)
            if decision == "9":
                break

main = Main()
main.run()     

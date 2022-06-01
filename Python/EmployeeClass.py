class Employee:
    def __init__(self,name,id,age,gender):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender

class Organization:
    def __init__(self,name,empList):
        self.name=name
        self.empList=empList
    
    def addEmployee(self,name,id,age,gender):
        emp=Employee(name,id,age,gender)
        self.empList.append(emp)

    def getEmployees(self):
        for e in self.empList:
            print(e.id)
            print(e.name)
            print(e.age)
            print(e.gender)
    
    def getEmployeeCount(self):
        return len(self.empList)

    def findEmployeeDetails(self,id):
        found=0
        for e in self.empList:
            if(e.id==id):
                print(e.id)
                print(e.name)
                print(e.age)
                print(e.gender)
                found=1
                break
        if(found==0):print("Record not found")

if __name__=='__main__':
    employees=[]
    o=Organization('TCS',employees)
    t=int(input())
    for i in range(t):
        name=input()
        id=input()
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)
    qid=input()
    qname=input()
    o.findEmployeeDetails(qid)

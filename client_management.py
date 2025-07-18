# Client Management Solution


class Client:
    def __init__(self,i,c,n,s,t,b):
        self.cid = i
        self.company = c
        self.name = n
        self.service = s
        self.tenure = t
        self.budget = b

    def __str__(self):
        return f"ID  :{self.cid}\nCompany :{self.company}\nName :{self.name}\nService :{self.service}\n.Tenure :{self.tenure}\nBudget :{self.budget}"

        
        

c1 = Client(101,"Archana Industries","Archan","Instagram Marketing",3.5 ,40000)
c2 = Client(102,"Gaytri cosmetics","Gaytri","Facebook Marketing",6.0 ,50000)
c3 = Client(103,"Dev Construction","Dev","Website Devlopment",4.5 ,60000)

Client_list = [c1,c2,c3]

def show_Clients():
    for cli in Client_list:
        print(cli)

def add_client():
    cid = int(input("Enter Client Id:"))
    company = input("Enter Client Company:")
    name = input("Enter Client Name:")
    service = input("Enter Client Service:")
    tenure = int(input("Enter Client Tenure:"))
    budget = int(input("Enter Client Budget:"))
    c4 = Client(Cid,Company,Name,Service,Tenure,Budget)
    Client_list.append(c4)
    print("\nCLIENT ADDED SUCCESFULLY!")

def find_client(i):
    for cli in Client_list:
        if i == cli.cid:
            return cli
    return False

def delete_client():
    i = int(input("Enter Client ID toDelete:"))
    cli = find_client(i)
    if cli !=False:
        Client_list.remove(cli)
        print("\nCLIENT DELETE SUCCESFULLY!")
    else:
        print("\nNO SUCH CLIENT FOUND TO DELETE!:")

def update_client():
    i = int(input("Enter Client ID TO Update:"))
    cli = find_client(i)
    if cli !=False:
        b = int(input("Enter Client's Update Budget:"))
        cli.budget = b
        print("\nCLIENT UPDATE SUCCESFULLY!")
    else:
        print("\nNO SUCH CLIENT FOUND TO UPDATE!")

while True:
    ch = int(input("\nEnter Choice:\n1.Show All Clients\n2.Add New Client\n3.Update A Client\n4.Delete A Client\n5.Exit:"))
    print()
    if ch == 1:
             print("1.Show All Clients")
             show_Clients()
    elif ch == 2:
        print("2.Add A New Client")
        add_client()
    elif ch == 3:
        print("3.Update A Client")
        update_client()
    elif ch == 4:
        print("Delete A Client")
        delete_client()

    elif ch == 5:
        print("5.Exit")
        break
    else:
        print("INVALID CHOICE!")
        
        

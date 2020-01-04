import sqlite3
import math

'''
Database, item and customer database
'''

class Item:
    ''' 
    class of each item
    including their name.type,etcq    
    '''
    totalquantity = 0
    item_index = 0

    def __init__(self,type,brand_name,RAM,Size,Screen,Cost,Supplier):
        self.type = type        #laptop or tablet
        self.brand_name = brand_name    #Hp, Lenovo,etc
        self.ram = RAM      #Size of RAM
        self.storage = Size     #Drive storage
        self.screen = Screen    #Screen size
        self.cost = Cost        #Cost of device
        self.supplier = Supplier      #Name of supplier
        Item.totalquantity +=1      #increase as each item is instantiated
        self.item_index = Item.totalquantity

    def get_type(self): #return whether Laptop or Tablet, useful for classifying
        return self.type
    def get_name(self): #returns brand name
        return self.brand_name
    def get_ram(self):  #returns the RAM size
        return self.ram
    def get_size(self): #returns the storage size
        return self.storage
    def get_cost(self): #returns cost just in case use wants to start from costly or least costly
        return self.cost

    def show_info(self): #shows details about device, useful in display panel
        return str(self.brand_name) +" "+ str(self.type)+"\nSpecifications: \n\tRAM: "+ self.ram +\
               "\n\tStorage size: "+ str(self.storage) + "\n\tScreen size: "+ str(self.screen)+\
              "\nSupplier: "+ self.supplier


sales = 0

class Customer:
    '''
    class for the each customer access the site or database
    '''
    name = ""
    age = 0
    address = ""
    gender = ""
    email = ""
    password = ""
    zip_code = ""
    customer_id = "" #uniquely identifies the customer
    number = 0
    city = ""

    def __init__(self):
        Customer.number+=1 #increase by one as each customer signs up
        if len(str(Customer.number))==1:
            self.customer_id = "000" + str(Customer.number)
        elif len(str(Customer.number))==2:
            self.customer_id = "00" + str(Customer.number)
        elif len(str(Customer.number))==3:
            self.customer_id = "0" + str(Customer.number)
        else:
            self.customer_id = Customer.number

    def set_name(self,name): #sets customer name
        self.name = name 
    def set_age(self,age): #sets customer age
        self.age = age
    def set_address(self,addr): #sets customer address
        self.address = addr
    def set_gender(self,sex): #sets customer sex
        self.gender = sex
    def set_email(self,mail): #sets customer email
        self.email = mail
    def set_zip_code(self, zipcd): #sets customer zipcode
        self.zip_code = zipcd
    def set_city(self,city): #sets customer city
        self.city = city

    def get_name(self): #returns customer name
        return self.name
    def get_age(self):  #returns customer age
        return self.age
    def get_address(self):  #returns customer address
        return self.address
    def get_gender(self):   #returns customer sex
        return self.gender  
    def get_email(self):   #returns customer email
        return self.email
    def get_zip_code(self):   #returns customer zipcode
        return self.zip_code
    def get_city(self):   #returns customer city
        return self.city
    def get_customer_id(self):  #returns customer id
        return self.customer_id

''' 
Text file extraction
The methods below extract the data from the text file and sort them in a database
'''
#read file
fo = open('ProductCatalogue.txt','r')

conn = sqlite3.connect('Sapertien_data.db')     #<dbname>.connect(database = '<dbname>', user = '<name>', password = '<#####>', host = '<127.0.0.1>', port = '<8080>')
c = conn.cursor()

def create_table():
     c.execute('CREATE TABLE IF NOT EXISTS inventory(Item_type TEXT, brand_name TEXT, RAM TEXT, Storage TEXT, Screen_Size INTEGER, Cost INTERGER, Supplier TEXT)')
     c.execute('CREATE TABLE IF NOT EXISTS customers(customer_id TEXT, Name TEXT, Age INTEGER, Email TEXT, Address TEXT, Zip TEXT, City TEXT)')
     c.execute( 'CREATE TABLE IF NOT EXISTS sales(customer_id TEXT, Purchase_date TEXT, Items_purchased TEXT, Supplier TEXT, Amount_paid FLOAT)')
create_table()

laptop_list = []
tablet_list = []

for line in fo:
    list = line.split(";")
    item_type, brand_name, RAM, Storage, Screen_Size, Cost \
    = list[0], list[1], list[2]+'GB', list[3]+'GB', int(list[4]), int(list[5])
    a = list[6]
    Supplier = ""
    for i in range(len(a)-1):
        Supplier+= a[i]

    # c.execute("INSERT INTO inventory VALUES (?,?,?,?,?,?,?)", (item_type, brand_name, RAM, Storage, Screen_Size, Cost, Supplier))
    # conn.commit()
    # nitem = Item(item_type,brand_name,RAM,Storage,Screen_Size,Cost,Supplier)    #intialize it to the class item
    # if nitem.type == "Laptop":  #makes laptop list
    #     laptop_list.append(nitem)
    # elif nitem.type == "Tablet": #makes tablet name
    #     tablet_list.append(nitem)

'''
The function will require a set to carry out the similarity function
Please do not discard the fact that will be using the attributes of each objects in the list as parameter
for the function
'''
laptop_set = set(laptop_list)   #converts laptop list to a set
tablet_set = set(tablet_list)   #converts tablet list to a set
#get each line of the text
#create database and table 
#append each item to database
'''
Sample test of the fetch algorithm
This will compare the line of text in the search string and bring out similar elements
The key is to first categorize each item
Then apply the formula
M
'''
c.execute('SELECT * FROM inventory')
database = c.fetchall()
c.close()
each_item = []

def call_items():
    for i in database:
        device = Item(i[0],i[1],i[2],i[3],i[4],i[5],i[6]) #creates device object add makes it part of the class
        each_item.append(device)

type_list = ['Laptop','LAPTOP','laptop','tablet', 'Tablet', 'TABLET', 'tab', 'Tab', 'TAB']

def itemotype(type):
    Laptop_group = ['Laptop','LAPTOP','laptop']
    Tablet_group = ['tablet', 'Tablet', 'TABLET', 'tab', 'Tab', 'TAB']
    if type in Laptop_group:
        return 1
    elif type in Tablet_group:
        return 2

brand_list = ['ACER', 'Acer', 'acer','Asus', 'ASUS', 'asus','Dell', 'DELL','dell','Hp','HP','hp',
              'Lenovo', 'LENOVO', 'lenovo','samsung','Sharp', 'SHARP','sharp','Techno', 'TECHNO', 'techno']
              
def itemBrand(brand):

    Acer = ['ACER', 'Acer', 'acer']
    Asus = ['Asus', 'ASUS', 'asus']
    Dell = ['Dell', 'DELL', 'dell']
    Hp = ['Hp','HP','hp']
    Lenovo = ['Lenovo', 'LENOVO', 'lenovo']
    Samsung = ['Samsung','SAMSUNG','samsung']
    Sharp = ['Sharp', 'SHARP', 'sharp']
    Techno = ['Techno', 'TECHNO', 'techno']

    if brand in Acer:
        return 1
    elif brand in Asus:
        return 2
    elif brand in Dell:
        return 3
    elif brand in Hp:
        return 4
    elif brand in Lenovo:
        return 5
    elif brand in Samsung:
        return 6
    elif brand in Sharp:
        return 7
    elif brand in Techno:
        return 8
    else:
        return 0


ramlist = ['1GB','2GB','3GB','4GB','5GB','6GB','7GB','8GB']
def itemRam(ram):
    for i in range(len(ramlist)):
        if ram == ramlist[i]:
            return i+1
    else:
        return 0

storagelist = ['30GB','50GB','150GB','200GB','250GB','300GB','350GB','500GB','750GB','1000GB']
def itemStorage(stor):
    for i in range(len(storagelist)):
        if stor == storagelist[i]:
            return i+1
    else:
        return 0

#Assign weight values for each parameter
brand_weight = len(brand_list)-1
ram_weight = len(ramlist)-1
type_weight = len(type_list)-1
storage_weight = len(storagelist)-1

rank_list = []

#ranking function based on Heterogenous Eclidean Overlap Metric(HEOM)
def rank(search):
    call_items()
    diction = {}
    search = search.split(' ')
    ranking = []

    for device in each_item:
        sum = 0
        for j in search:
            if j in type_list:
                if itemotype(j) == itemotype(device.type):
                    sum+=0
                else:
                    sum+=math.fabs(itemotype(j)-itemotype(device.type))/type_weight
            elif j in brand_list:
                if itemBrand(j) == itemBrand(device.brand_name):
                    sum+=0
                else:
                    sum+=math.fabs(itemBrand(j)-itemBrand(device.brand_name))/brand_weight
            elif j in ramlist:
                if itemRam(j) == itemRam(device.ram):
                    sum+=0
                else:
                    sum+=math.fabs(itemRam(j)-itemRam(device.ram))/ram_weight
            elif j in storagelist:
                if itemStorage(j) == itemStorage(device.storage):
                    sum+=0
                else:
                    sum+=math.fabs(itemStorage(j)-itemStorage(device.storage))/storage_weight
        value = sum
        diction[value] = device
    listing = sorted(diction)
    for i in range(len(listing)):
        if i <= 10:
            rank_list.append(diction[listing[i]])
    for i in rank_list:
        ranking.append(i.show_info())
    return ranking

print(rank('4GB ram Hp laptop'))
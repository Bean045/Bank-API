import json

class Customer:
    def __init__(self, first_name, last_name, email, phone_no, address, aadhar_card_no, pan_card_no, zip_code, balance, acc_no, bank_details, account_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        self.address = address
        self.aadhar_card_no = aadhar_card_no
        self.pan_card_no = pan_card_no
        self.zip_code = zip_code
        self.balance = balance
        self.acc_no = acc_no
        self.bank_details = bank_details
        self.account_type = account_type
    
    def change_details(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount:float):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdraw amount")
    
    def transfer(self, amount, customer):
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")
        if 0 < amount <= self.balance:
            self.balance -= amount
            customer.deposit(amount)
        else:
            raise ValueError("Invalid transfer amount")
    
    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

class Bank:
    def __init__(self, name, branch, initials, address, phone_nos, email, ifsc_code):
        self.name = name
        self.branch = branch
        self.initials = initials
        self.address = address
        self.phone_nos = phone_nos
        self.email = email
        self.customers_list = []
        self.ifsc_code = ifsc_code
    
    def change_details(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers_list.append(customer)
        else:
            raise ValueError("Invalid customer")
    
    def find_customer_by_acc_no(self, acc_no):
        for customer in self.customers_list:
            if customer.acc_no == acc_no:
                return customer
        return None
    
    def find_customer_by_name(self, first_name, last_name):
        for customer in self.customers_list:
            if customer.first_name == first_name and customer.last_name == last_name:
                return customer
        return None
    
    def find_customer_by_email(self, email):
        for customer in self.customers_list:
            if customer.email == email:
                return customer
        return None
    
    def find_customer_by_mobile_no(self, mobile_no):
        for customer in self.customers_list:
            if customer.phone_no == mobile_no:
                return customer
        return None
    
    def delete_customer(self, acc_no):
        customer = self.find_customer_by_acc_no(acc_no)
        if customer:
            self.customers_list.remove(customer)
            return True
        return False
    
    def get_total_balance(self):
        total_balance = sum(customer.balance for customer in self.customers_list)
        return total_balance
    
    def to_json(self):
        bank_dict = self.__dict__.copy()
        bank_dict['customers_list'] = [customer.__dict__ for customer in self.customers_list]
        return json.dumps(bank_dict, indent=4)

# Creating a bank instance
bank = Bank(
    name="Apna Sahakari Bank Ltd.",
    branch="Naigaon",
    initials="ASBL",
    address="Opp. Sadakant Dhavan, Dadar-Naigaon",
    phone_nos=["123-456-7890", "234-657-651"],
    email="contact@apna.bank",
    ifsc_code="ASBL456123"
)

# Creating a customer instance
customer1 = Customer(
    first_name="Vishal",
    last_name="Loke",
    email="vishal.loke@gmail.com",
    phone_no="1234567890",
    address="1014, Parijat",
    aadhar_card_no=123456789012,
    pan_card_no="ABCDE1234F",
    zip_code=400012,
    balance=1000.0,
    acc_no="ASBL12345",
    bank_details={"name": "Apna Sahakari Bank Ltd.", "branch": "Naigaon", "ifsc_code": "ASBL12345"},
    account_type="savings"
)

# Adding customer to the bank
bank.add_customer(customer1)

# Get bank details in JSON
print(bank.to_json())

# Get customer details in JSON
print(customer1.to_json())

# Deposit money
customer1.deposit(500)
print(customer1.check_balance())

# Withdraw money
customer1.withdraw(200)
print(customer1.check_balance())

# Transfer money
customer2 = Customer(
    first_name="Rohan",
    last_name="Juikar",
    email="rohan.juikar@gmail.com",
    phone_no="0123456789",
    address="912, Ganesh Sai",
    aadhar_card_no=987654321012,
    pan_card_no="VWXYZ1234U",
    zip_code=400012,
    balance=500.0,
    acc_no="ASBL67890",
    bank_details={"name": "Apna Sahakari Bank Ltd.", "branch": "Naigaon", "ifsc_code": "ASBL12345"},
    account_type="current"
)
bank.add_customer(customer2)

customer1.transfer(300, customer2)
print(customer1.check_balance())  
print(customer2.check_balance())

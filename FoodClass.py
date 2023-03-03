import random


# class definition
class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.__customerid = customerid
        self.__name = name
        self.__add = address
        self.__email = email
        self.__phone = phone
        self.__memstatus = member_status

    # accessor methods for customer class
    def get_customerid(self, customerid):
        self.__customerid = customerid
        return customerid

    def get_name(self, name):
        self.__name = name
        return name

    def get_address(self, address):
        self.__address = address
        return address

    def get_email(self, email):
        self.__email = email

    def get_phone(self, phone):
        self.__phone = phone
        return phone

    def get_member_status(self):
        return self.__memstatus


# second class definition
class Transaction:
    def __init__(self, date, item_name, cost, cust_id):
        self.__date = date
        self.__itemname = item_name
        self.__cost = cost
        self.cust_id = cust_id

    # accessor methods for transaction class
    def get_date(self, date):
        self.__date = date

    def get_item(self, itemname):
        self.__itemname = itemname
        return itemname

    def get_cost(self, cost):
        self.__cost = cost
        return cost

    def get_cust_id(self, cust_id):
        self.__cust_id = cust_id
        return cust_id

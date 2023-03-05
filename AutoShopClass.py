import random


class Customer:         #class
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__manufact = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, y):
        self.__retail_price = y

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        tax = 0.0825

        self._sales_tax = (
            float(self.get_parts_charges()) + float(self.get_labor_charges())
        ) * tax

        return self._sales_tax

    def get_total_charges(self):
        self._total_charges = (
            float(self.get_parts_charges())
            + float(self.get_labor_charges())
            + float(self.get_sales_tax())
        )
        return self._total_charges

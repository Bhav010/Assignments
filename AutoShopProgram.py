#program for Joe’s Automotive Shop using classes

import AutoShopClass as a

name = "John Doe"
address = "123 Main St. Waco TX 76706"
phone = "214-555-1112"
make = "Honda"
model = "Accord LX "
year = "2016"
parts = float(1210.50)
labor = float(765.00)


auto1 = a.Customer(name, address, phone)
auto2 = a.Car(make, model, year)
auto3 = a.ServiceQuote(parts, labor)

print()
print(
    f"Customer: {auto1.get_name()} \t Address: {auto1.get_address()} \t Phone:{auto1.get_phone()} \n"
)
print(
    f"Car Make: {auto2.get_make()} \t Car Model: {auto2.get_model()} \t Car Year: {auto2.get_year()} \n"
)
print("Service Quote \n")
print(f"Parts: ${auto3.get_parts_charges():,.2f} \n")
print(f"Labor: ${auto3.get_labor_charges():,.2f} \n")
print(f"Sales Tax: ${auto3.get_sales_tax():,.2f} \n")
print(f"Total Charges: ${auto3.get_total_charges():,.2f}")

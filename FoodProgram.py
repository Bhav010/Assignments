# import Class
import FoodClass as fc


# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}


# Run the program using Customer-1 data first and then using Customer-2 data in second run to get the desired output
def main():
    # Customer1 data
    id = 570
    Name = "Danni Sellyar"
    Address = "97 Mitchell Way Hewitt Texas 76712"
    Email = "dsellyarft@gmpg.org"
    Phone = str("254-555-9362")
    Mem_status = "False"

    """
    # Customer2 data
    id = 569
    Name = "Aubree Himsworth"
    Address = "1172 Moulton Hill Waco Texas 76710"
    Email = "ahimsworthfs@list-manage.com"
    Phone = str("254-555-2273")
    Mem_status = "True"
    """
    # Customer class object
    food = fc.Customer(id, Name, Address, Email, Phone, Mem_status)

    # variables used for calculation, initialised to 0
    order_total = 0
    discount = 0

    # To print desired output for customer
    print(f"Customer Name: {food.get_name(Name)}")
    print(f"Phone: {food.get_phone(Phone)}")

    for i in dict.values():
        # transaction class object
        transact = fc.Transaction(i[0], i[1], i[2], i[3])

        # compare customer id of customer class object & transaction class object
        if food.get_customerid(id) == transact.get_cust_id(i[3]):
            print(
                f"Order Item: {transact.get_item(i[1])}   Price: ${transact.get_cost(i[2]):.2f}"
            )
            x = transact.get_cost(i[2])
            order_total += x  # order_total gets updated
    print(f"Total Cost: ${order_total:.2f}")

    if food.get_member_status() == "True":  # Member discount validation
        discount = order_total * 0.20
        print(f"Member Discount: ${discount:.2f}")
        print(f"Total cost after discount: ${(order_total-discount):.2f}")
        order_total *= 0.80


# Call the main function
main()

'''
Entity: product
------------------------
    State:
    -----
        Attributes: pID, Price,name, company
        values: FH789, 70,000, smartTV, sony
        datatype: str, int, str, str
    Behaviour:
    ---------
        Create: Adding a product
        Retrieve: Retrieve product information by pid
        Update: change price of product
        Delete: Remove a product

Entity: customer
------------------------
    State:
    -----
        Attributes: CID, Name, Email, Phone Number
        values: 100, dora, dora@gmail.com, 987065437
        datatype: int, str, str, str
    Behaviour:
    ---------
        Create: create a customer info
        Retrieve: Retrieve customer information by cid
        Update: change mailid
        Delete: remove a customer


Entity: order
--------------
    State:
    -----
        Attributes: Order ID, Customer ID, price, Payment Method
        values: 34878, 782, 90000,creditcard
        datatype: int, int, int, str
    Behaviour:
    ---------
        Create: Generate a new order when a customer makes a purchase.
        Retrieve: get order price
        Update: modify the order price
        Delete: mark order is completed



Entity: store
--------------
    State:
    -----
        Attributes: storeid, Location, Address, contact
        values: 34878, city electronics, st nagar, 9674890656
        datatype: int, str, str,str
    Behaviour:
    ---------
        Create: Add a new store location to the system.
        Retrieve: Retrieve information like store location
        Update: Modify store details like phone number
        Delete: remove a store location.



Entity: store_employee
--------------
    State:
    -----
        Attributes: eid, Name, position, sal
        values: 201, shri, store manager, 50000
        datatype: int, str, str,int
    Behaviour:
    ---------
        Create: Hire a new employee and add their information.
        Retrieve: Access employee details eid
        Update: update the salary
        Delete: Terminate the employee

Entity: supplier
--------------
    State:
    -----
        Attributes: sid, name, con_person, contact
        values: 201, shri, smith, 965721463
        datatype: int, str, str,int
    Behaviour:
    ---------
        Create: add a new supplier
        Retrieve: Retrieve supplier details through sid
        Update: Modify supplier information contact
        Delete: Remove a supplier



'''
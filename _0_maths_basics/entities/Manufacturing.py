'''
Entity: product
---------------
    State:
    -----
        Attributes: pid, pname, price, wght
        values: 15648, Widget X, 60000, 1kg
        datatype: int, str, int, str
    Behaviour:
    ---------
        Create: Add a new product to the database.
        Retrieve: Retrieve product information by the product ID .
        Update: Modify the attributes of an existing product price and weight .
        Delete: Remove a product from the database.

Entity: Bill of materials
-------------------------
    State:
    -----
        Attributes: BOMid, pid, componentid, quant
        values: 15648, 55451, C565448, 2
        datatype: int, int, str, int
    Behaviour:
    ---------
        Create: Create a new BOM record.
        Retrieve: Retrieve BOM information by bill of materials id.
        Update: Modify the BOM for a attributes like quantity.
        Delete: Delete a BOM record .


Entity: Bulk order
------------------
    State:
    -----
        Attributes: B_id, pid, qunat, status
        values: 454154, 134, 100, in progress
        datatype: int, int, int, str
    Behaviour:
    ---------
        Create: Generate a new order .
        Retrieve: Retrieve order details by bulk order id.
        Update: Update the status of the bulk order.
        Delete: Cancel a bulk order.


Entity: Supplier
----------------
    State:
    -----
        Attributes: sid, sname, cont_info
        values: 4654, Vishnu, 632147895
        datatype: int, str, str
    Behaviour:
    ---------
        Create: Add new supplier information to the database.
        Retrieve: Retrieve supplier details by sid.
        Update: Update supplier information like contact info.
        Delete: Remove a supplier .

Entity: Employee
----------------
    State:
    -----
        Attributes: eid, fstname, lstname, position, dept
        values: 4654845, vyshu, kalangi, production supervisor, Manufacturing
        datatype: int, str, str, str, str
    Behaviour:
    ---------
        Create: Add new employee to the record.
        Retrieve: Retrieve employee details by eid.
        Update: Update employee information like dept.
        Delete: Remove employee record.


Entity: Machine
----------------
    State:
    -----
        Attributes: mid, mname, loc, maintenance_schd
        values: 4584, MachineA, Factory floor, Every 10hrs of operation
        datatype: int, str, str, str,
    Behaviour:
    ---------
        Create: Add products to a customer shopping cart.
        Retrieve: Retrieve the contents cart id.
        Update: Modify the quantity of products in the cart .
        Delete: Clear the entire shopping cart.

Entity: Quality control
-----------------------
    State:
    -----
        Attributes: Inspect_id, pid, inspect_date, P/F_status
        values: 4614, 4656, 2023-0-20, pass
        datatype: int, str, str, str,
    Behaviour:
    ---------
        Create: Add products to a customer shopping cart.
        Retrieve: Retrieve the contents cart id.
        Update: Modify the quantity of products in the cart .
        Delete: Clear the entire shopping cart.

'''
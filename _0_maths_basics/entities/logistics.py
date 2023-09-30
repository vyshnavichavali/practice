'''

Entity: product
---------------
    State:
    -----
        Attributes: prod_name, wght, manuf
        values: iphone, 0.9(kg), Apple
        datatype: str, str, str
    Behaviour:
    ---------
        Create: Add a new product to the database.
        Retrieve: Retrieve product information through manufacturer.
        Update: Modify product details such as price .
        Delete: Remove a product.

Entity: Supplier
---------------
    State:
    -----
        Attributes: sup_name, sup_id, cont_mem, ph_num, addr
        values: ABC electronics, GG37t3, smith, 9123475621, 235 mainstreet bglr
        datatype: str, str, str, str, str
    Behaviour:
    ---------
        Create: Add a new supplier database.
        Retrieve: Retrieve supplier information like supplier id.
        Update: Update supplier contact information .
        Delete: Remove a supplier data from database.

Entity: warehouse
---------------
    State:
    -----
        Attributes: wrehou_name, wrehou_id, loc
        values: donny, WH6768, bglr
        datatype: str, str, str
    Behaviour:
    ---------
        Create: Register a new warehouse location.
        Retrieve: Retrieve information like warehouse id.
        Update: Modify warehouse location.
        Delete: remove warehouse data

Entity: customer
---------------

    State:
    -----
        Attributes: coust_name, coust_id, cont_person, ph_num
        values: ABC corporation, GH66757, jhon, 612475963
        datatype: str, str, str, int
    Behaviour:
    ---------
        Create: Add a new customer to the customer database.
        Retrieve: Retrieve customer details by customer id.
        Update: Update customer information phone number.
        Delete: Remove a customer record .

Entity: shipment
---------------

    State:
    -----
        Attributes: shpmnt_id, shpmnt_date, destin
        values: SHP878, 2023-90-15, ABC corporation
        datatype: str, str, str
    Behaviour:
    ---------
        Create: Create a new shipment record .
        Retrieve: retrieve information by shipment id.
        Update: Update information like shipment status."
        Delete: remove shipment records.

Entity: carrier
---------------

    State:
    -----
        Attributes: carr_name, carr_id, cont_person, ph_num
        values: Fastfre shipping, CAR5758, mike, 6231457892
        datatype: str, str, str, str
    Behaviour:
    ---------
        Create: Add a new carrier to the database.
        Retrieve: retrieve carrier informationby carrier id.
        Update: update carrier details like contact person and phone number.
        Delete: Remove a carrier information.

Entity: order
---------------
    State:
    -----
        Attributes: ord_num, ord_dt, tot_amou
        values: 5456461, 2023-09-18, 80000
        datatype: int, str, int
    Behaviour:
    ---------
        Create: create a new order .
        Retrieve: Retrieve order details by order number.
        Update: Modify order information like total amount.
        Delete: remove the order from the database.

Entity: employee
---------------
    State:
    -----
        Attributes: emp_id, emp_name, email, deptmnt
        values: 65461, gnanshi, gnanshi@gmail.com, logistics
        datatype: int, str, str, str
    Behaviour:
    ---------
        Create: Add a new employee to the database.
        Retrieve: get employee information by employee id.
        Update: Update employee details like email.
        Delete: Terminate an employee .

Entity: vehicle
---------------

    State:
    -----
        Attributes: veh_id, veh_type, lic_plate, max_load
        values: 1654564, truck, BVY76, 5tones
        datatype: int, str, str, str
    Behaviour:
    ---------
        Create: Add a new vehicle .
        Retrieve: get vehicle information by vehicle id.
        Update: Update vehicle details like maximum load.
        Delete: remove a vehicle from the database.

Entity: invoice
--------------
    State:
    -----
        Attributes: invoc_num, invoc_date, shipmnt_id, tot_amou, paymnt_status
        values: INV1564, 2023-09-20, SHP1544, 5000, unpaid
        datatype: str, str, str, int, str
    Behaviour:
    ---------
        Create: Add a new invoice .
        Retrieve: get invoice details by invoice number.
        Update: Modify invoice details like payment status.
        Delete: remove old invoices from the system.
'''
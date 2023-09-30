'''
Entity: product
---------------

    State:
    -----
        Attributes: pid, pname, price, manuf
        values: P34897, laptop, 50000, Apple
        datatype: str, str, int, str
    Behaviour:
    ---------
        Create : Add a new product to the system.
        Retrieve: Retrieve product information by product id .
        Update: Modify product information by price .
        Delete : Remove a product from the system.

Entity: customer
---------------
    State:
    -----
        Attributes: cid, fst_name, lst_name, email, ph_num, shipping_addr, bilng_addr
        values: 45131, yshu, alvali, yshu@gmail.com, 632145789, ABC-bglr, ABC-bglr
        datatype: int, str, str, str, str, str, str
    Behaviour:
    ---------
        Create : add a new customer.
        Retrieve : Retrieve customer information by customer id.
        Update : Modify customer information like phone number, email.
        Delete : Delete a customer account .

Entity: order
---------------
    State:
    -----
        Attributes: oid, cid, tot_amou, paymnt_mthd
        values: 45131, 51871, 50000, credit card
        datatype: int, int, int, str
    Behaviour:
    ---------
        Create: Place a new order from the particular site.
        Retrieve: Retrieve order details by oid.
        Update: Update order status and total amount.
        Delete: Cancel an order .

Entity: payment
---------------
    State:
    -----
        Attributes: pid, oid, pay_date, pay_amou, pay_status,
        values: 45131, 51871, 2023-9-15,500000, Successful
        datatype: int, int, str, int, str
    Behaviour:
    ---------
        Create: add a new payment for an order.
        Retrieve: Retrieve payment details by payment id or order id.
        Update: Update payment status and payment amount.
        Delete: refund a payment (if necessary).

Entity: Review
---------------
    State:
    -----
        Attributes: prid, pid, cid, rating
        values: 45131, 51871, 25654, 5
        datatype: int, int, int, int
    Behaviour:
    ---------
        Create: Allow customers to submit product reviews.
        Retrieve: Retrieve product reviews by product id.
        Update: update rating and existing reviews.
        Delete: Remove a review.

Entity: cart
-------------
    State:
    -----
        Attributes: ca_id, cid, pid, quant, cart_tot
        values: 15648, 1548, 4568, 2, 500000
        datatype: int, int, int, int, int
    Behaviour:
    ---------
        Create: Add products to a customer shopping cart.
        Retrieve: Retrieve the contents cart id.
        Update: Modify the quantity of products in the cart .
        Delete: Clear the entire shopping cart.

'''
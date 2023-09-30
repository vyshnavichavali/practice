'''
Entity: Aircraft
---------------

    State:
    -----
        Attributes: aircrft_type, reg_num, mauf, capacity
        values: Boeing, HGUI678, Airbus, 446
        datatype: str, str, str
    Behaviour:
    ---------
        Create: Add a new aircraft to the database
        Retrieve: Retrieve aircraft information based on registration number
        Update: update aircraft attributes such as passenger capacity
        Delete: Remove an aircraft from the database.

Entity: airport
-------------
    State:
    -----
        Attributes: airpt_code, loc, num_of_terminals
        values: JHGHK, Blgr, 4
        datatype: str, str, int
    Behaviour:
    ---------
        Create: Add a new airport
        Retrieve: Retrieve airport information based on airport code.
        Update: update airport data like number of terminals.
        Delete: Remove an airport record from the database.

Entity: Flight
-------------
    State:
    -----
        Attributes: Flgt_num, depat_airpt, arriv_airpt
        values: DL675, ABC, XYZ
        datatype: str, str, str, str
    Behaviour:
    ---------
        Create: Create a new flight record
        Retrieve: Retrieve flight information based on flight number, arrival airport.
        Update: update flight details, such as departure airport and arrival airport.
        Delete: remove a flight record .

Entity: Baggage
-------------
    State:
    -----
        Attributes: bag_num, weght, desti, pas_name
        values: B723489, 30, bglr, daisy
        datatype: str, int, str, str
    Behaviour:
    ---------
        Create: Record baggage details for a passenger, including weight and destination.
        Retrieve: Retrieve baggage information using baggage tag numbers.
        Update: Update baggage details like weight and destination.
        Delete: Remove baggage record.

Entity: passenger
----------------
    State:
    -----
        Attributes: pas_name, pasport_num, Natinality
        Values: daisy, ABC7655, United Status
        datatype: str, str, str
    Behaviour:
    ---------
        Create: add a new passenger .
        Read: Retrieve passenger information using their name, passport number.
        Update: Update passenger details like name and nationality.
        Delete: Remove a passengers record .

Entity: crew member
-------------------
    State:
    -----
        Attributes: name, emp_id, role, lic_num
        values: daisy, 87482, pilot, L348983
        datatype: str, int, str, str
    Behaviour:
    ---------
        Create: Add a new crew member .
        Retrieve: Retrieve crew member information based on their name or employee ID.
        Update: update crew member details, like role or license number.
        Delete: remove a crew member from the database.

Entity: arline
-------------

    State:
    -----
        Attributes: arli_name, Head_quat, fleet_size
        values: ABC airlines, Bglr, 600
        datatype: str, str, str
    Behaviour:
    ---------
        Create: Add a new airline .
        Retrieve: Retrieve airline information based on name.
        Update: update airline attributes like fleet size and headquarters location.
        Delete: Remove an airline .


'''
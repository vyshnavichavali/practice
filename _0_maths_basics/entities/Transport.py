'''
Entity: vehicle
-----------------
    State:
    -----
        Attributes: vid, veh_type, plate_num, manufacturer
        values: 101, sedan, ABC123, toyota
        datatype: int, str, str, str
    Behaviour:
    ---------
        Create: Add a new vehicle
        Retrieve: Retrieve vehicle information based on vid
        Update: change vehile plate number
        Delete: Remove a vehicle from the database

Entity: Driver
-----------------
    State:
    -----
        Attributes: Did, Name, Age, Lic_num
        values: 101, smith, 30, LM12345
        datatype: int, str, int, str
    Behaviour:
    ---------
        Create: Add a new driver.
        Retrieve: Retrieve driver information by DID
        Update: change driver information age
        Delete: Remove a driver record.


Entity: Passenger
-----------------
    State:
    -----
        Attributes:  pas_id, pas_name, age, pref_seat
        values: 101, smith, 30, Window
        datatype: int, str, int, str
    Behaviour:
    ---------
        Create: add a new passenger with their details.
        Retrieve: Retrieve passenger information using their pas_ID.
        Update: update passenger details like their pref_seat
        Delete: Delete a passenger record.


Entity: Route
-----------------
    State:
    -----
        Attributes: Rou_name, start_city, dest, dist, dur
        values: R001, Bglr, hyd, 100, 2
        datatype: str, str, str, int, int
    Behaviour:
    ---------
        Create: create a new route
        Retrieve: Retrieve route information based on its rou_name
        Update: update route details, such as the distance, duration.
        Delete: Delete a route record.

Entity: Ticket
-----------------
    State:
    -----
        Attributes: T_Num, pas_name, route,seat_num, fare
        values: T242545, smith, R101, 3A, 1500
        datatype: str, str, str, str,int
    Behaviour:
    ---------
        Create: create a new ticket for a passenger
        Retrieve: Retrieve ticket details using the T_Num
        Update: Update ticket information like seat_num
        Delete: Cancel a ticket

Entity: Schedule
-----------------
    State:
    -----
        Attributes: Route, dep_time, loc
        values: R101, 10AM, bglr
        datatype: str, str, str
    Behaviour:
    ---------
        Create: create a new schedule
        Retrieve: Retrieve the schedule with route
        Update: Modify schedule details like dep_time.
        Delete: Remove a schedule record.


Entity: Fare
-----------------
    State:
    -----
        Attributes: Far_type, Fare, discount, dis_fare
        values: adult, 1000, student, 400
        datatype: str, int, str, int
    Behaviour:
    ---------
        Create: create a new fare
        Retrieve: Retrieve fare details by far_type or discounts.
        Update: change fare information like discount
        Delete: Delete a fare type.

'''
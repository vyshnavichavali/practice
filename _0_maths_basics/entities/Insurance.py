'''
Entity: policy
-------------
    State:
    -----
        Attributes: pol_num, pol_type, pol_start_dat, pol_end_dat
        values: P34897, Auto, 2023-09-15, 2024- 09-15
        datatype: str, str, str, str
    Behaviour:
    ---------
        Create: Add a new policy
        Retrieve: Retrieve policy information based on pol_num
        Update: update policy details such as the policy dates.
        Delete: Remove a policy

 Entity: customer
-----------------

    State:
    -----
        Attributes: cid, name, addr, ph_num
        values: 389735628, helis, ST nagar, 9234578126
        datatype: str, str, str, str
    Behaviour:
    ---------
        create: Add a new customer
        Retrieve: Retrieve customer details by customer ID, name
        Update: update customer information such as their address, phone number
        Delete: Remove a customer's

 Entity: claim
---------------

    State:
    -----
        Attributes: cnum, pol_num, cname, cal_status, cal_amou
        values: CL3748, P34897, helis, open, 5000
        datatype: str, str, str, str, int
    Behaviour:
    ---------
        Create: add a new claim
        Retrieve: Retrieve claim details using the claim number, policy number
        Update: Update the status, amount
        Delete: remove a claim

 Entity: agent
------------------------
    State:
    -----
        Attributes: agnt_id, name, ph_num, lic_num
        values: A57678, helin, 9123458624, 45476
        datatype: str, str, str, str
    Behaviour:
    ---------
        Create: Add a new agent
        Retrieve: Retrieve agent information by agent ID
        Update: Update agent details such as license number.
        Delete: remove an agent

 Entity: Benificiary
------------------------
    State:
    -----
        Attributes: bnf_name, relation, ph_num, pol_num
        values: Amrutha, spouse, 9321456842
        datatype: str, str, str
    Behaviour:
    ---------
        Create: Add a new beneficiary
        Retrieve: Retrieve beneficiary information based on the policy number
        Update: Update beneficiary details or their relationship to the insured.
        Delete: Remove a beneficiary from a policy

 Entity: Insurance
------------------------

    State:
    -----
        Attributes: cmp_name, cmp_addr, ph_num, lic_num
        values: ABC insurance, 456-NRlayout,9123458624, 45476
        datatype: str, str, str, int
    Behaviour:
    ---------
        Create: Add a new insurance
        Retrieve: Retrieve information about an insurance company by its icense number.
        Update: update company information such as contact details and address.
        Delete:remove an insurance company

'''
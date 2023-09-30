'''
# Entity: patient
------------------------

    State:
    -----
        Attributes: pid, Name, DOB, Gender, Con_info
        values: Amrutha, 13-jan-2000, Female, 9766543682
        datatype: str, int, str, str
    Behaviour:
    ---------
        create: crating the patient record
        Retrieve: we can get the patient data through pid
        update: changing the con_info
        delete: remove the patient record

# Entity: Doctor
------------------------

    State:
    -----
        Attributes: Name, Speciality, con_info, Edu, certificate
        values: Shiva, cardiology, 9274638374, University of medicine, certified in cardiology
        datatype: str, str, int, str, str
    Behaviour:
    ---------
        create: crating the doctor record
        Retrieve: we can get the data by searching with the speciality
        update: changing the con_info
        delete: remove the doctor record


# Entity: Hospital
------------------------

    State:
    -----
        Attributes: Name, Address, con_info, bed_capacity
        values: city hospital, KNR avenue, 9876234578, 200
        datatype: str, str, str, int
    Behaviour:
    ---------
        create: crating the record of hospital
        Retrieve: we can get the data by searching hospital name
        update: changing the con_info, bed_capacity
        delete: remove the hospital record

# Entity: Billing/insurance
------------------------

    State:
    -----
        Attributes: Insu_prov, policy_num, billing_amount, billing_status
        values:  XYZ_insurance, 9324, 3000, done
        datatype: str, int, int, str
    Behaviour:
    ---------
        create: crating the insurance info of patient
        Retrieve: view billing status, insurance details and payment status
        update: update the billing_status
        delete: remove the insurance record

# Entity: Medical history
------------------------

    State:
    -----
        Attributes: Chronic conditions, surgical history, lifestyle_factors
        values: diabetes, knee surgery, smoking
        datatype: str, str, str
    Behaviour:
    ---------
        create: create patient medical history
        Retrieve: we can get the patient complete medical history
        update: modify the history records
        delete: remove the outdated record

# Entity: Medical image
------------------------

    State:
    -----
        Attributes: pid, image type, date_taken, Radiologist
        values: 101, X-ray, 2023/14/09, DR. Smith
        datatype: str, date, str, str
    Behaviour:
    ---------
        create: Add the new image
        Retrieve: we can get the data by searching with the pid
        update: changing the Radiologist
        delete: removing the image

# Entity: Medical Procedure
------------------------

    State:
    -----
        Attributes: Procedure Code, Date of Procedure, Performing Doctor.
        values: JGTH7, 2023-08-20, Dr.sanjay
        datatype: str, date, str
    Behaviour:
    ---------
        Create: add medical procedure of patient.
        Retrieve: get the data through procedure code
        update: modify procedure details
        delete: delete procedure

# Entity: Prescription
------------------------

    State:
    -----
        Attributes: Medication Name, Dosage, Prescribing Doctor.
        values: Amoxicillin, 500 , Dr.jhon
        datatype: str, int, str
    Behaviour:
    ---------
        Create: add prescription for a patient.
        Retrieve: Access a patient's data by medication.
        Update: modify medication dosage
        Delete: remove a prescription.

# Entity: Medical Appointment
------------------------

    State:
    -----
        Attributes: Patient, Doctor, Reason for Visit, Appointment Status.
        values: anjali, jhon, routine check-up, scheduled
        datatype: str, str, str, str
    Behaviour:
    ---------
        Create: add new appointment to a patient.
        Retrieve: Retrieve appointment details by patient.
        Update: Change reason for visit.
        Delete: remove an appointment.
'''
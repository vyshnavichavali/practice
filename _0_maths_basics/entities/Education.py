''''''
'''
Entity: Student 
===================
    1. STATE:
    ---------   
variable: Attributes: RollNo, name, addr, Gender
value   : Values    : 1, vyshu, Behind SR-Road Bangalore, Female
type    : datatypes:  int, str, str, str

    2. BEHAVIOR:
    --------------
    CRUD : CREATE / RETRIEVE / UPDATE / DELETE 
        - Create an Student      : While joining 
        - Retrieve Student  info : 
        - Update                 : Update Address /Name 
        - Delete Student         : while leaving the School

Notes: 
-------
During the joining student information will be created.
After that we can retrieve Student information. 
We can update Student details like Name, Address 
We can delete Student details while leaving the school


Entity: Teacher 
===================
    1. STATE:
    ---------   
variable: Attributes: id, name, sal, Gender, Sub_expert
value   : Values    : 10, vyshu, 40,000, Female, Maths
type    : datatypes:  int, str, int, str, str

    2. BEHAVIOR:
    --------------
    CRUD : 
        - Create an Teacher      : While joining in the education institution
        - Retrieve Teacher  info : 
        - Update                 : Update sal /Name 
        - Delete Teacher         : while leaving the educational institution

Notes: 
-------
During the joining Teacher information will be created.
After that we can retrieve Teacher information. 
We can update Teacher details like Name, Address 
We can delete Teacher details while leaving the educational institution

Entity: Remote Learning 
=======================
    1. STATE:
    ---------   
         Attributes: id, name, password
         Values    : 10, vyshu, *******
         datatypes:  int, str, str

    2. BEHAVIOR:
    --------------
    CRUD : 
        - Create an login        : While signing up
        - Retrieve student  info : while we want to login
        - Update                 : Update password 
        - Delete login           : while joining in offline/ course is completed

Notes: 
-------
During the joining in remote learning we do signup.
After that we can retrieve while we want to login. 
We can update loign details like password
We can delete loign details while joining in offline/ course is completed

Entity: School
--------------
    State:
    -----
        Attributes: Name, Address, Contact information, Priniple/Headmaster
        Values: Shreya, SR Nagar Banglore, 9865789327, Kishore
        Datatypes:str, str, str, str
    Behaviour:
    ---------
    CRUD:
        Create: School record will be created like, name, address, contact information
        Retrieve: We can get information by name and location
        Update: We can update Principal and contact information
        Delete: Removing school record from database
        
Entity: Curriculum
------------------
    State:
    -----
    
        Attributes: Grade, Subjects/courses, Textbooks, Assessment method, Standard
        Values: A, Maths, MathsTextbook,Exam, state standrad
        Datatypes: str, str, str, str
    Behaviour:
    ---------
    CRUD
        Create: creating new curriulum like grade, subjects
        Retrieve: We can get by searching associated course/subject
        Update: changing such as assessment
        Delete: remove the curriculum from system

Entity: Classroom
-----------------

    State:
    -----
        Attributes: Room number, seating arrangement, Technology, Teaching aids
        values: 101, rows of desks/circular arrangement, whiteboard/blackboard, chalk/marker
        datatype: int, str, str,str
    Behaviour:
    ---------
        create: Adding new classroom record 
        Retrieve: We can get about classroom by searching room number
        update: modifying the seating arrangement
        delete: remove the classroom recors
        

Entity: Subject/Course:
----------------------

    State:
    -----
        Attributes: course title, instructor, credits
        values: Algebra, BIOTHL, Smith, 3 
        datatype: str, str, str,int
    Behaviour:
    ---------
        create: Adding course in the record
        Retrieve: We can get subject by searching subject code
        update: changing the instructor
        delete: remove the subject

Entity: Education Technology
----------------------
LMS- Learning mangement system
    State:
    -----
        Attributes: LMS, Edu_s/w, H/w, online_resource
        values: google classroom, Microsoft office,laptops,  E-books  
        datatype: str, str, str,str
    Behaviour:
    ---------
        create: crating technology 
        Retrieve: we can get the data about particular technology
        update: changing the hardware
        delete: remove technology

# Entity: Parent/Guardian
------------------------

    State:
    -----
        Attributes: pname,sid con_info, Relation, 
        values: Amrutha,101, 9274638374, Mother
        datatype: str, int, str, str
    Behaviour:
    ---------
        create: crating the record for parent 
        Retrieve: we can get the data by searching with the sid
        update: changing the con_info
        delete: remove the parent record
'''
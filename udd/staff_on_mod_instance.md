# Staff teaching a module Instance

*  [STAFF_ID](#staff_id)
*  [MOD_INSTANCE_ID](#mod_instance_id)

##STAFF_ID
###Description
An institutions unique ID for their staff member. This could be their username.

###Purpose
To show the staff member's name within SSP, SSP Dashboards, or Student Insight.

###Derivation

###References

###Format
String(255)

###Compulsory
Yes

###Notes
This will be the unique identifier/ primary key for the member of staff who is responsible for the student (course/ year tutor) or the person responsible for managing cases or analysing dashboards which involve the student. This will typically be the staff/ HR/ payroll number for the member of academic staff, which links to their email address in the institutions identity management system.

##MOD_INSTANCE_ID 
(link from Module Instance in UDD 1.1)
###Description
Institutions unique identifier for this module instance

###Purpose
For link a module instance to a student

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes

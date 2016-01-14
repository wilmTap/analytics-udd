## Student (Additional Information)

* [STUDENT_ID](#student_id) - link to Student Instance in UDD 1.1
* [USERNAME](#username)
* [LAST_NAME](#last_name)
* [FIRST_NAME](#first_name)
* [ADDRESS_LINE_1](#address_line_1)
* [ADDRESS_LINE_2](#address_line_2)
* [ADDRESS_LINE_3](#address_line_3)
* [ADDRESS_LINE_4](#address_line_4)
* [POSTCODE](#postcode)
* [PRIMARY_EMAIL_ADDRESS](#primary_email_address)
* [HOME_PHONE](#home_phone)
* [MOBILE_PHONE](#mobile_phone)
* [PHOTO_URL](#photo_url)
* [COACH_SCHOOL_ID](#coach_school_id)

## Staff teaching a module Instance

*  [STAFF_ID](#staff_id)
*  [MOD_INSTANCE_ID](#mod_instance_id) - link to Module Instance in UDD 1.1

##STUDENT_ID
###Description
The institution's own unique identifier of the student. In the case or event of requiring to provide anonymous data for trial/ evaluation purposes with JISC, institutions should use a suitable method or algorithm (which can be reversed by that institution, for evaluation purposes thereafter) to ensure that this studentid provided is different to that actual ID held locally.

###Purpose
To identify the student across multiple records within an institution

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^OWNSTU.html

###References

###Format
String 255

###Compulsory
Yes

###Notes

##USERNAME
###Description
This is the username for systems access at the Institution

###Purpose
To be used for user login/ account lookup purposes

###Format
String (255)

###Compulsory
Yes

###Notes
This will typically be imported and updated continuously from Institution identity management systems.

##LAST_NAME
###Description
Students family or surname.

###Purpose
For display. Used by Student App, Student Success Planner, Tribal Insight

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Compulsory
Yes

###Notes

##FIRST_NAME
###Description
Students given or first name

###Purpose
For display. Used by Student App, Student Success Planner, Tribal Insight

###Derivation
Jisc

###Valid Values
Any

###Format
String

###Compulsory
Yes 

###Notes

##ADDRESS_LINE_1
###Description
Address Line 1 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

Compulsory
No 

###Notes
This is usually imported from the Institution's SRS.

##ADDRESS_LINE_2
###Description
Address Line 2 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

Compulsory
No 

###Notes
This is usually imported from the Institution's SRS.

##ADDRESS_LINE_3
###Description
Address Line 3 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

Compulsory
No 

###Notes
This is usually imported from the Institution's SRS.

##ADDRESS_LINE_4
###Description
Address Line 4 - term-time accommodation

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String

Compulsory
No 

###Notes
This is usually imported from the Institution's SRS.

##POSTCODE
###Description
This is the current (term-time) postcode corresponding to the student's accommodation address provided

###Purpose
For display. Used by Student Success Planner

###Derivation
Jisc
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^TTPCODE.html

###Valid Values
Any

###Format
String

###Compulsory
No 

###Notes
This should relate to the term-time postcode of the student's residency, and NOT the entry postcode onto the student's learning instance

##PRIMARY_EMAIL_ADDRESS
###Description
Students primary email address

###Purpose
For display and contact via student success planner. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String(255)

###Compulsory
No (TO BE CONFIRMED)

###Notes
Will be input/ batched directly from central IT or identification management systems at the institution

##HOME_PHONE
###Description
Students home telephone number. This can refer to the landline telephone number of their term-time or non term-time accomodation.

###Purpose
For display and contact purposes. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String(255)

###Compulsory
No

###Notes
This is usually imported from the Institution's SRS.

##MOBILE_PHONE
###Description
Students mobile telephone number.

###Purpose
For display and contact purposes. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
String(255)

###Compulsory
No

###Notes
This is usually imported from the Institution's SRS.

##PHOTO_URL
###Description
URL link provided to a latest/ recent photo of student

###Purpose
For display purposes. Used by Student Success Planner

###Derivation
Jisc

###Valid Values
Any

###Format
GIF or JPG (exact list of formats, and ideal (minimum) photo resolution, to be confirmed)

###Compulsory
No

###Notes
This assumes that there is a way of securing access to the photo.

##COACH_SCHOOL_ID
###Description
This is the unique identification number for the learner's academic or course year supervisor/ tutor, or alternatively the id of the contact who will be responsible for handling Learning Analytics alerts and notification regarding the student

###Purpose
For notification and alerts purposes for Learning Analytics SSP and other software tools

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14025&href=a^_^OWNSTAFFID.html

###References

###Format
String(255)

###Compulsory
Yes

###Notes
This will be the unique identifier/ primary key for the member of staff who is responsible for the student (course/ year tutor) or the person responsible for receiving alerts and notifications from the Learning Analytics software suite/ tools. This will typically be the staff/ HR/ payroll number for the member of academic staff, which links to their email address in the institutions identity management system.

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

##MOD_INSTANCE_ID (link from Module Instance in UDD 1.1)
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

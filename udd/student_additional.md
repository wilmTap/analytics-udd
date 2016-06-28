# student_additional
An additional data entity.

* [STUDENT_ID](student.md#student_id) [1]
* [USERNAME](#username) [1]
* [LAST_NAME](#last_name) [1]
* [FIRST_NAME](#first_name) [1]
* [ADDRESS_LINE_1](#address_line_1) [0..1]
* [ADDRESS_LINE_2](#address_line_2) [0..1]
* [ADDRESS_LINE_3](#address_line_3) [0..1]
* [ADDRESS_LINE_4](#address_line_4) [0..1]
* [POSTCODE](#postcode) [0..1]
* [PRIMARY_EMAIL_ADDRESS](#primary_email_address) [0..1]
* [HOME_PHONE](#home_phone) [0..1]
* [MOBILE_PHONE](#mobile_phone) [0..1]
* [PHOTO_URL](#photo_url) [0..1]
* [TUTOR_STAFF_ID](#tutor_staff_id) [0..1]
* [ENTRY_POSTCODE](#entry_postcode) [0..1]

##USERNAME
###Description
This is the username for systems access at the Institution

###Purpose
To be used for user login/ account lookup purposes

###Format
String (255)

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
See HESA definition

###Format
String (8)

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

###Notes
This assumes that there is a way of securing access to the photo.


##TUTOR_STAFF_ID
###Description
This is the unique identification number for the learner's academic or course year supervisor/ tutor, or alternatively the id of the contact who will be responsible for handling Learning Analytics alerts and notification regarding the student

###Purpose
For notification and alerts purposes for Learning Analytics SSP and other software tools

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14025&href=a^_^OWNSTAFFID.html

###References

###Format
String(255)

###Notes
This will be the unique identifier/ primary key for the member of staff who is responsible for the student (course/ year tutor) or the person responsible for receiving alerts and notifications from the Learning Analytics software suite/ tools. This will typically be the staff/ HR/ payroll number for the member of academic staff, which links to their email address in the institutions identity management system.


##ENTRY_POSTCODE
###Description.
Identifies the postcode of the student's permanent or home address prior to entry to the course. It is not necessarily the correspondence address of the student.

###Purpose
Analytics 

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=15051&href=a^_^POSTCODE.html

###Valid Values
See HESA definition

###Format
String (8)

###Notes
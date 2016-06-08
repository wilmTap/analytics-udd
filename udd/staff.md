# Staff
An additional data entity

* [STAFF_ID](#staff_id) [1]
* [FIRST_NAME](#first_name) [1]
* [LAST_NAME](#last_name) [1]
* [TITLE](#title) [0..*]
* [PRIMARY_EMAIL_ADDRESS](#primary_email_address) [1]
* [HESA_STAFF_ID](#hesa_staff_id) [0..1]
* [DASH_SHIB_ID](#dash_shib_id) [0..1]

##STAFF_ID
###Description
An institution's unique identifier for a staff member. This could be their username.

###Purpose
To show the staff member's name within SSP, SSP Dashboards, or Student Insight.

###Derivation
Jisc

###Valid values
Any

###References

###Format
String(255)

###Notes
This will be the unique identifier/ primary key for the member of staff who is responsible for the student (course/year tutor) or the person responsible for managing cases or analysing dashboards which involve the student. This will typically be the staff/ HR/ payroll number for the member of academic staff, which links to their email address in the institutions identity management system.


##FIRST_NAME
###Description
Staff given or first name.

###Purpose
Display

###Derivation
Jisc

###Valid values
Any

###References

###Format
String (255)

###Notes


##LAST_NAME
###Description
Staff family or surname.

###Purpose
Display

###Derivation
Jisc

###Valid values
Any

###References

###Format
String (255)

###Notes


##TITLE
###Description
Staff Title as stored in the student record system

###Purpose
Display

###Derivation
Jisc

###Valid values
Any

###References

###Format
String (255)

###Notes


##PRIMARY_EMAIL_ADDRESS
###Description
Staff's primary email address

###Purpose
Display, and as a user id and contact detail in analytics.

###Derivation
Jisc

###Valid values
Any

###References

###Format
String (255)

###Notes


##HESA_STAFF_ID
###Description
A unique code allocated to staff when they are first entered onto the HESA Staff record. The code remains with the member of staff for the whole of their career within higher education

###Purpose
Analytics

###Derivation
https://www.hesa.ac.uk/component/studrec/show_file/14025/a%5E_%5ESTAFFID.html

###Valid values
A 13 digit number, or an eleven digit number preceded by 'XX'

###References

###Format
String (13)

###Notes
The values have a specific generation algorithm. See https://www.hesa.ac.uk/component/studrec/show_file/14025/a%5E_%5ESTAFFID.html


##DASH_SHIB_ID
###Description.
The person identifier used by Shibboleth / The UK Access Management Federation to grant access to the Jisc analytics staff dashboard.

###Purpose
Analytics 

###Derivation
https://www.internet2.edu/media/medialibrary/2013/09/04/internet2-mace-dir-eduperson-200604.html

###Valid Values
Not specified

###Format
String (256)

###Notes
There may be a more general AIM_ID property later that can be used for any UK Federation service provider ID, not just the Jisc staff dashboard.

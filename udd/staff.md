# Staff
An additional data entity

* [STAFF_ID](staff_on_mod_instance.md#staff_id)
* [FIRST_NAME](#first_name)
* [LAST_NAME](#last_name)
* [TITLE](#title)
* [PRIMARY_EMAIL_ADDRESS](#primary_email_address)
* [HESA_STAFF_ID](#hesa_staff_id)
* [DASH_SHIB_ID](#dash_shib_id)

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

###Compulsory
Yes

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

###Compulsory
Yes

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

###Compulsory
No

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

###Compulsory
Yes

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

###Compulsory
No

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

###Compulsory
No

###Notes
There may be a more general AIM_ID property later that can be used for any UK Federation service provider ID, not just the Jisc staff dashboard.

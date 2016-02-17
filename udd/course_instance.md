#Course instance
* [COURSE_ID](#course_id)
* [COURSE_INSTANCE_ID](#course_instance_id)
* [START_DATE](#start_date)
* [END_DATE](#end_date)
* [ACADEMIC_YEAR](#academic_year)

##COURSE_ID
###Description
The providers own ID for the course

###Purpose
To link relational database tables

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^OWNCOURSEID.html
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^Course_COURSEID.html

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes

###Notes
HE guidance - this field could relate to actual HESA COURSEID field or the HR institution's OWNCOURSEID field for cross-referencing purposes.

##COURSE_INSTANCE_ID
###Description
Institution's identifier for this course instance

###Purpose
To link student to course, and course to course instance

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes

###Notes

##START_DATE
###Description
Start date for this course instance

###Purpose
For analytics

###Derivation
Jisc

###Valid Values
Date in ISO8601 format - YYYY-MM-DD

###Format
String (255)

###Compulsory
Yes

###Notes

##END_DATE
###Description
End date for this course instance

##Purpose
For analytics

###Derivation
Jisc

###Valid Values
Date in ISO8601 format - YYYY-MM-DD

###Format
String (255)

###Compulsory
Yes

###Notes

##ACADEMIC_YEAR
###Description
Academic year to which the course instance relates. 

###Purpose
For display and analysis purposes

###Derivation
Jisc

###Valid Values
Year as four digit - ie year that the academic year starts in.

###Format
Int

###Compulsory
Yes

###Notes
Could be derived, but academic year calendars may be different between institutions. This field could also be sourced directly from the SRS.

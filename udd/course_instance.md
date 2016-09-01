#Course instance
* [COURSE_ID](course.md#course_id) [1]
* [COURSE_INSTANCE_ID](#course_instance_id) [1]
* [START_DATE](#start_date) [1]
* [END_DATE](#end_date) [1]
* [ACADEMIC_YEAR](#academic_year) [1]
* [COURSE_LOCATION](#course_location) [0..1]

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
ISO 8601 Year

###Notes
Could be derived, but academic year calendars may be different between institutions. This field could also be sourced directly from the SRS.

##COURSE_LOCATION
###Description
Identifies the location with which a student on a course instance is associated, be it a building, a site or a campus.

###Purpose
For analytics (predictive model building) and for presenting analytics.

###Derivation
Loosely based on
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=15051&href=a^_^CAMPID.html

###Valid Values
Any

###Format
String (255)

###Notes
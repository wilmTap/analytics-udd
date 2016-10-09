#course_instance
* [COURSE_ID](course.md#course_id) [1]
* [COURSE_INSTANCE_ID](#course_instance_id) [1]
* [START_DATE](#start_date) [0..1]
* [END_DATE](#end_date) [0..1]
* [ACADEMIC_YEAR](#academic_year) [0..1]

Primary key: ('COURSE_INSTANCE_ID')

For more information about which properties are required for particular purposes or under particular conditions, please consult the [guide to mandatory properties in the UDD](../mandatory.md).

##COURSE_INSTANCE_ID
###Description
Institution's identifier for this course_instance

###Purpose
To link student to course, and course to course_instance

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Notes

##START_DATE
###Description
Start date for this course_instance

###Purpose
For analytics

###Derivation
Jisc

###Valid Values
Date in ISO8601 format - YYYY-MM-DD

###Format
String (255)

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.

##END_DATE
###Description
End date for this course_instance

##Purpose
For analytics

###Derivation
Jisc

###Valid Values
Date in ISO8601 format - YYYY-MM-DD

###Format
String (255)

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.

##ACADEMIC_YEAR
###Description
Academic year to which the course_instance relates. 

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

Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.


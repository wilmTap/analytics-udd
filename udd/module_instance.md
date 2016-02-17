#Module instance
* [MOD_ID](#mod_id)
* [MOD_INSTANCE_ID](#mod_instance_id)
* [MOD_START_DATE](#mod_start_date)
* [MOD_END_DATE](#mod_end_date)
* [MOD_PERIOD](#mod_period)
* [MOD_ONLINE](#mod_online)
* [MOD_ENROLLMENT](#mod_enrollment)
* [MOD_ACADEMIC_YEAR](#mod_academic_year)
* [MOD_OPTIONAL](#mod_optional)

##MOD_ID
###Description
The unique identifier standard across SRS and LMS for the course.

###Purpose
For analytics and to link Module to Module Instance

Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^Module_MODID.html

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes

##MOD_INSTANCE_ID
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

##MOD_START_DATE
###Description
Start date of this module instance

###Purpose
Analytics and display

###Derivation
Jisc

###Valid Values
ISO 8601 - YYYY-MM-DD

###Format
Date

###Compulsory
Yes (if applicable)

###Notes
The start and end date of a module instance MUST align with the start and end date of a course instance.

##MOD_END_DATE
###Description
End date of this module instance

###Purpose
Analytics and display

###Derivation
Jisc

###Valid Values
ISO 8601 - YYYY-MM-DD

###Format
Date

###Compulsory
Yes (if applicable)

###Notes
The start and end date of a module instance MUST align with the start and end date of a course instance.

##MOD_PERIOD
###Description
Period to which module instance relates (e.g. semester 1)

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Any

###Format
String (256)

###Compulsory
No (if applicable)

###Notes
It is expected that sites / organisations will have their own code lists for MOD_PERIOD values.

##MOD_ONLINE
###Description
Whether this module instance is delivered wholly online

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
<table>
<tr><td>CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>2</td><td>No</td><td>Na</td></tr>
</table>  

###Format
Int

###Compulsory
Yes (if applicable)

###Notes

##MOD_ENROLLMENT
###Description
This field will be an auto-calculated field which will provide (in real-time) the number of students/ learners enrolled onto the particular instance of this module instance

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Int

###Compulsory
Yes (if applicable) - default will be zero (0)

###Notes

##MOD_ACADEMIC_YEAR
###Description
Academic year that this module runs within - this must represent the start year of that specific academic year eg. for 2014-15 this would be 2014

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Int

###Format
4 digit year

###Compulsory
Yes (if applicable)

###Notes
This is the starting year for the academic year.

##MOD_OPTIONAL
###Description
Whether this instance relates to an optional module or not.

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values

<table>
<tr><td>CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>2</td><td>No</td><td>Na</td></tr>
</table>  

###Format
Int

###Compulsory
No (if applicable)

###Notes

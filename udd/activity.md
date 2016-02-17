#Activity
* [STUDENT_ID](#student_id)
* [MOD_ID](#mod_id)
* [EVENT](#event)
* [EVENT_DATE](#event_date)

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

##EVENT
###Description.
The activity event type associated with the learner activity record

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
To be specified as an integer indexed list by the institution

###Format
Int

###Compulsory
Yes

###Notes

##EVENT_DATE
###Description.
The date of the event type of the learner activity record taking place

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
To be specified as an integer indexed list by the institution

###Format
Date (ISO format) - YYYY-MM-DD

###Compulsory
Yes

###Notes

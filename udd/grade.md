#Grade
* [STUDENT_ID](#student_id)
* [MOD_INSTANCE_ID](#mod_instance_id)
* [GRADABLE_OBJECT](#gradable_object)
* [CATEGORY](#category)
* [MAX_POINTS](#max_points)
* [EARNED_POINTS](#earned_points)
* [WEIGHT](#weight)
* [GRADE_DATE](#grade_date)

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

##GRADABLE_OBJECT
###Description.
TO BE CONFIRMED

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Not specified

###Format
Int

###Compulsory
Yes

###Notes
Used to classify the grade activity record.

##CATEGORY
###Description.
This is a custom set of values representing the category of the grade activity record object eg. assignment, examination, coursework, test etc.

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
Used to classify the grade activity record.

##MAX_POINTS
###Description.
Maximum points available for this graded activity record

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Not specified

###Format
Int

###Compulsory
Yes

###Notes
Used to calculate grade result.

##EARNED_POINTS
###Description.
Points earned and achieved (result) for this graded activity record

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Not specified

###Format
Int

###Compulsory
Yes

###Notes
Used to calculate grade result.

##WEIGHT
##Description.
The weighting value associated with the grade activity record

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Not specified

###Format
Int

###Compulsory
Yes

###Notes
Used to calculate grade result.

##GRADE_DATE
###Description.
The date at which the grade result has been confirmed and awarded

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
Not specified

###Format
Date (ISO format) - YYYY-MM-DD

###Compulsory
No

###Notes

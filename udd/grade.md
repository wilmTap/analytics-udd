#Grade
* [STUDENT_ID](student.md#student_id)
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id)
* [GRADABLE_OBJECT](#gradable_object)
* [CATEGORY](#category)
* [MAX_POINTS](#max_points)
* [EARNED_POINTS](#earned_points)
* [WEIGHT](#weight)
* [GRADE_DATE](#grade_date)

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

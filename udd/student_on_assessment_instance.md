#Student on assessment instance
* [STUDENT_ID](student.md#student_id)
* [STUDENT_COURSE_MEMBERSHIP_ID](student_course_membership.md#student_course_membership_id)
* [STUDENT_COURSE_MEMBERSHIP_SEQ](student_course_membership.md#student_course_membership_seq)
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id)
* [ASSESS_ID](assessment_instance.md#assess_id)
* [ASSESS_SEQ_ID](#assess_seq_id)
* [ASSESS_DUE_DATE](#assess_due_date)
* [ASSESS_RETAKE](#assess_retake)
* [ASSESS_AGREED_MARK](#assess_agreed_mark)
* [ASSESS_ACTUAL_MARK](#assess_actual_mark)
* [ASSESS_AGREED_GRADE](#assess_agreed_grade)
* [ASSESS_ACTUAL_GRADE](#assess_actual_grade)
* [ASSESSMENT_CURRENT_ATTEMPT](#assessment_current_attempt)
* [ASSESSMENT_COMPLETED_ATTEMPT](#assessment_completed_attempt)

##ASSESS_SEQ_ID
###Description.
A unique ID to indicate the order of assessments taken by a student on the assessment instance.

###Purpose
To help identify the latest assessment and the order of assessments for a student, especially for those in reassessment.
This could differ from the ASSESS_CURRENT_ATTEMPT/ASSESS_COMPLETED_ATTEMPT attributes when a student has mitigating circumstances.

###Derivation
Jisc

###Valid Values
Any

###Format
Integer

###Compulsory
Yes (if applicable)

###Notes


##ASSESS_DUE_DATE
###Description.
The date an assessment instance for a student was due for submisson.

###Purpose
Analytics and display

###Derivation
Jisc

###Valid Values
YYYY-MM-DD

###Format
ISO 8601 

###Compulsory
Yes (if applicable)

###Notes


##ASSESS_RETAKE
###Description.
Whether this is a retake of the asessment for that student.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values

|code|description (English)|description (Welsh)|
|---|---|---|
|1|Yes|"welsh translation forthcoming”|
|2|No|"welsh translation forthcoming”|

###Format
Integer

###Compulsory
No

###Notes


##ASSESS_ACTUAL_MARK
###Description.
The actual mark for the assessment attempt.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
1-100

###Format
Decimal

###Compulsory
No

###Notes


##ASSESS_AGREED_MARK
###Description.
The agreed mark for the assessment attempt.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
1-100

###Format
Decimal

###Compulsory
No

###Notes


##ASSESS_ACTUAL_GRADE
###Description.
The actual grade for the assessment attempt.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
No

###Notes


##ASSESS_AGREED_GRADE
###Description.
The agreed grade for the assessment attempt.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes

###Notes


##ASSESSMENT_CURRENT_ATTEMPT
###Description.
Number of attempts taken by a student so far on an assessment instance.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
Integer

###Compulsory
Yes (if applicable)

###Notes


##ASSESSMENT_COMPLETED_ATTEMPT
###Description.
Number of attempts taken by a student to complete an assessment instance.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
Integer

###Compulsory
Yes (if applicable)

###Notes


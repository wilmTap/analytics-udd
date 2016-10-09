#student_on_assessment_instance
* [STUDENT_ID](student.md#student_id) [1]
* [STUDENT_COURSE_MEMBERSHIP_ID](student_course_membership.md#student_course_membership_id) [1]
* [STUDENT_COURSE_MEMBERSHIP_SEQ](student_course_membership.md#student_course_membership_seq) [1]
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id) [1]
* [ASSESS_INSTANCE_ID](assessment_instance.md#assess_instance_id) [1]
* [ASSESS_SEQ_ID](#assess_seq_id) [1]
* [ASSESS_DUE_DATE](#assess_due_date) [0..1]
* [ASSESS_RETAKE](#assess_retake) [0..1]
* [ASSESS_AGREED_MARK](#assess_agreed_mark) [0..1]
* [ASSESS_ACTUAL_MARK](#assess_actual_mark) [0..1]
* [ASSESS_AGREED_GRADE](#assess_agreed_grade) [0..1]
* [ASSESS_ACTUAL_GRADE](#assess_actual_grade) [0..1]
* [ASSESSMENT_CURRENT_ATTEMPT](#assessment_current_attempt) [0..1]
* [ASSESSMENT_RESULT](#assessment_result) [0..1]
* [GRADE_DATE](#grade_date) [0..1]
* [MAX_POINTS](#max_points) [0..1]
* [X_ASSESS_DETAIL](#x_assess_detail) [0..1]
* [X_MOD_NAME](student_on_a_module_instance.md#x_mod_name) [0..1]
* [X_MOD_ID](#x_mod_id) [0..1]
* [X_MOD_ACADEMIC_YEAR](#x_mod_academic_year) [0..1]

Primary key: ('STUDENT_COURSE_MEMBERSHIP_ID', 'STUDENT_COURSE_MEMBERSHIP_SEQ', 'ASSESS_INSTANCE_ID', 'ASSESS_SEQ_ID')

For more information about which properties are required for particular purposes or under particular conditions, please consult the [guide to mandatory properties in the UDD](../mandatory.md).

##ASSESS_SEQ_ID
###Description.
A unique sequence number to indicate the order of assessments taken by a student on the assessment instance.

###Purpose
To help identify the latest assessment and the order of assessments for a student, especially for those in reassessment.
This could differ from the ASSESS_CURRENT_ATTEMPT/ASSESS_COMPLETED_ATTEMPT attributes when a student has mitigating circumstances.

###Derivation
Jisc

###Valid Values
Any

###Format
Integer

###Notes
The ASSESS_SEQ_ID number needs to increment with the chronological order of assessments.

##ASSESS_DUE_DATE
###Description.
The date an assessment instance for a student was due for submission.

###Purpose
Analytics and display

###Derivation
Jisc

###Valid Values
YYYY-MM-DD

###Format
ISO 8601

###Notes


##ASSESS_RETAKE
###Description.
Whether this is a retake of the asessment for that student.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
<table>
<tr><td>ASSESS_RETAKE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>2</td><td>No</td><td>Na</td></tr>
</table>  

###Format
Integer

###Notes


##ASSESS_ACTUAL_MARK
###Description.
The initial mark given for the assessment attempt prior to moderation.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
0-100

###Format
Decimal

###Notes


##ASSESS_AGREED_MARK
###Description.
The mark agreed for the assessment attempt after moderation.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
0-100

###Format
Decimal

###Notes


##ASSESS_ACTUAL_GRADE
###Description.
The initial grade given for the assessment attempt before moderation.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Notes


##ASSESS_AGREED_GRADE
###Description.
The grade agreed for the assessment attempt after moderation.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

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

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

##ASSESSMENT_RESULT
###Description.
Indicates whether the student passed the assessment, didn't pass the assessment, deferred the assessment or whether this information is not known because the assessment hasn't been due yet.

###Purpose
Analytics

###Derivation
Jisc; student_on_a_module_instance.MOD_RESULT

<table>
<tr><td>MOD_RESULT</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Pass</td><td>  </td></tr>
<tr><td>2</td><td>Fail</td><td>  </td></tr>
<tr><td>3</td><td>Not known</td><td> </td></tr>
<tr><td>4</td><td>deprecated (was: 'deferred')</td><td> </td></tr>
</table>  

###Format
Int

###Notes
Code 3 is applied in all cases where the outcome is either not known (yet), or doesn't apply because the student hasn't been assessed yet. Code 4 is deprecated because deferral or withdrawal is indicated by WITHDRAWAL_REASON in student_course_membership. 
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.


##GRADE_DATE
###Description.
The date at which the grade result has been confirmed and awarded.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Not specified

###Format
Date (ISO format) - YYYY-MM-DD

###Notes
This is the date when a grade has been moderated and agreed, but before exam board confirmation. It is typically the date at which the grade is entered in a SRS.


##MAX_POINTS
###Description.
The maximum points that an instructor can allocate to an assessment. Used to indicate the marking scale used for an assignment.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Not specified

###Format
String (256)

###Notes
The value can be any alphanumeric used by any type of marking scale. E.g. 80%, B11 or 'excellent'. There is also the similar MAX_MARKS property on assessment_instance, which is for analytic purposes. It only accepts decimal data.


##X_ASSESS_DETAIL
###Description.
An extra implementation optimisation that isn't part of the UDD model. It's value is identical to that of the relevant assessment_instance.ASSESS_DETAIL.

###Purpose
Implementation optimisation

###Derivation
Jisc; assessment_instance.ASSESS_DETAIL

###Valid Values
Any

###Format
String (255)

###Notes
This data is generated internally from existing data, and does not need to be supplied by an institution.


##X_MOD_ID
###Description.
An extra implementation optimisation that isn't part of the UDD model. Its value is identical to that of the relevant module.MOD_ID.

###Purpose
Implementation optimisation

###Derivation
Jisc; module.MOD_ID

###Valid Values
Any

###Format
String (255)

###Notes
This data is generated internally from existing data, and does not need to be supplied by an institution.


##X_MOD_ACADEMIC_YEAR
###Description
An extra implementation optimisation that isn't part of the UDD model. Its value is identical to that of MOD_ACADEMIC_YEAR on the mod_instance identified by the relevant MOD_INSTANCE_ID.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
4 digit year

###Format
Int

###Notes
This is the starting year for the academic year.
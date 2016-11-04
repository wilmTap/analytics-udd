#student_on_a_module_instance

* [STUDENT_COURSE_MEMBERSHIP_ID](student_course_membership.md#student_course_membership_id) [1] *
* [COURSE_INSTANCE_ID](course_instance.md#course_instance_id) [1] *
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id) [1] *
* [STUDENT_COURSE_MEMBERSHIP_SEQ](student_course_membership.md#student_course_membership_seq) [1]
* [STUDENT_ID](student.md#student_id) [1]
* [MOD_GRADE](#mod_grade) [0..1] deprecated
* [MOD_RESULT](#mod_result) [0..1]
* [MOD_RETAKE](#mod_retake) [0..1]
* [MOD_START_DATE](#mod_start_date) [0..1]
* [MOD_END_DATE](#mod_end_date) [0..1]
* [MOD_FIRST_MARK](#mod_first_mark) [0..1]
* [MOD_ACTUAL_MARK](#mod_actual_mark) [0..1]
* [MOD_AGREED_MARK](#mod_agreed_mark) [0..1]
* [MOD_FIRST_GRADE](#mod_first_grade) [0..1]
* [MOD_ACTUAL_GRADE](#mod_actual_grade) [0..1]
* [MOD_AGREED_GRADE](#mod_agreed_grade) [0..1]
* [MOD_CREDITS_ACHIEVED](#mod_credits_achieved) [0..1]
* [MOD_CURRENT_ATTEMPT](#mod_current_attempt) [0..1]
* [MOD_COMPLETED_ATTEMPT](#mod_completed_attempt) [0..1]
* [X_MOD_NAME](#x_mod_name) [0..1]
* [X_MOD_ACADEMIC_YEAR](#x_mod_academic_year) [0..1]

\* indicates that the property is part of a composite primary key for this entity.

##MOD_GRADE (deprecated)
###Description.
Final grade student achieved on the module.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (256)

###Notes
Use MOD_AGREED_GRADE instead of MOD_GRADE


##MOD_RESULT
###Description.
Indicates whether the student passed the module, didn't pass the module, deferred the module or whether this information is not known because the module hasn't been completed yet.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values

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


##MOD_RETAKE
###Description.
Whether this is a retake of the module for that student.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values

<table>
<tr><td>MOD_RETAKE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>2</td><td>No</td><td>Na</td></tr>
</table>  

###Format
Int

###Notes


##MOD_START_DATE
###Description
Start date of this module_instance

###Purpose
Analytics and display

###Derivation
Jisc

###Valid Values
ISO 8601 - YYYY-MM-DD

###Format
Date

###Notes
The start and end date of a module_instance MUST align with the start and end date of a course_instance.
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.


##MOD_END_DATE
###Description
End date of this module_instance

###Purpose
Analytics and display

###Derivation
Jisc

###Valid Values
ISO 8601 - YYYY-MM-DD

###Format
Date

###Notes
The start and end date of a module_instance MUST align with the start and end date of a course_instance.
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.


##MOD_FIRST_MARK
###Description
The mark awarded by the initial marker prior to any moderation process.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
0-100

###Format
Decimal

###Notes
MOD_FIRST_MARK should only be part of a UDD compliant dataset if there is a moderation process and the input mark is available in the source data.
If a marking process involves concurrent initial marking, the reconciled result should be recorded in MOD_ACTUAL_MARK.

##MOD_ACTUAL_MARK
###Description
The mark awarded to the learner after any moderation process, but before any formal confirmation process. Moderation processes typically involve multiple markers, and confirmation processes typically involve external examiners.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
0-100

###Format
Decimal

###Notes
MOD_ACTUAL_MARK should only be part of a UDD compliant dataset if there is a moderation process and if the result of that process is available in the source data.


##MOD_AGREED_MARK
###Description
The mark recorded after any moderation or confirmation processes, or the only recorded mark if there are no moderation or confirmation processes. This mark is typically the one used to determine degree classification.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
0-100

###Format
Decimal

###Notes
MOD_AGREED_MARK is expected to be present in any UDD compliant dataset as soon as it becomes available.


##MOD_FIRST_GRADE
###Description
The grade awarded by the initial marker prior to any moderation process.

###Purpose
Analytics. The first grade a student receives on the module is used to help monitor what changes to marks are made during the re-assessment process.

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Notes
MOD_FIRST_GRADE should only be part of a UDD compliant dataset if there is a moderation process and the input grade is available in the source data.
If a marking process involves concurrent initial marking, the reconciled result should be recorded in MOD_ACTUAL_GRADE.


##MOD_ACTUAL_GRADE
###Description
The grade awarded to the learner after any moderation process, but before any formal confirmation process. Moderation processes typically involve multiple markers, and confirmation processes typically involve external examiners.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Notes
MOD_ACTUAL_GRADE should only be part of a UDD compliant dataset if there is a moderation process and if the result of that process is available in the source data.


##MOD_AGREED_GRADE
###Description
The grade recorded after any moderation or confirmation processes, or the only recorded grade if there are no moderation or confirmation processes. This grade is typically the one used to determine degree classification.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Notes
MOD_AGREED_GRADE is expected to be present in any UDD compliant dataset as soon as it becomes available.

##MOD_CREDITS_ACHIEVED
###Description
The number of credits awarded for the module.

###Purpose
Analytics

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/crdtpts/

###Valid Values
Any

###Format
Integer

###Notes


##MOD_CURRENT_ATTEMPT
###Description
Number of attempts taken by a student so far on a module_instance.

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

##MOD_COMPLETED_ATTEMPT
###Description
Number of attempts taken by a student to complete a module_instance.

###Purpose
Analytics

###Derivation
Jisc

###Valid Values
Any

###Format
Integer

###Notes


##X_MOD_NAME
###Description
An extra implementation optimisation that isn't part of the UDD model. Its value is identical to that of the relevant module.MOD_NAME.

###Purpose
Implementation optimisation

###Derivation
Jisc; module.MOD_NAME

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
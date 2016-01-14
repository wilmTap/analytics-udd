
##Institution
* TENANT_ID
* TENANT_NAME

##Student
* [STUDENT_ID](#student_id)
* [ULN](#ULN)
* [DOB](#DOB)
* ETHNICITY
* GENDER
* AGE
* LEARN_DIF
* DISABILITY1
* DISABILITY2
* DOMICILE
* TERMTIME_ACCOM
* PARENTS_ED
* SOCIO_EC
* OVERSEAS

##Course
* COURSE_ID
* SUBJECT
* TITLE
* COURSE_AIM

##Course Instance
* COURSE_ID
* COURSE_INSTANCE_ID
* START_DATE
* END_DATE
* ACADEMIC_YEAR

##Student on Course Instance
* STUDENT_ID
* COURSE_INSTANCE_ID
* WITHDRAWAL_REASON
* WITHDRAWAL_DATE
* MODE
* YEAR_COM
* YEAR_PRG
* YEAR_STU
* COURSE_AVERAGE_GRADE
* YEAR_AVERAGE_GRADE
* ENTRY_QUALS
* ENTRY_POINTS
* COURSE_OUTCOME
* COURSE_GRADE

##Module
* MOD_ID
* MOD_NAME
* MOD_SUBJECT
* MOD_CREDITS

##Module Instance
* MOD_ID
* MOD_INSTANCE_ID
* MOD_START_DATE
* MOD_END_DATE
* MOD_PERIOD
* MOD_ONLINE
* MOD_ENROLLMENT
* MOD_ACADEMIC_YEAR
* MOD_OPTIONAL
* MOD_LEVEL

##Student on a module Instance
* STUDENT_ID
* COURSE_INSTANCE_ID
* MOD_INSTANCE_ID
* MOD_OUTCOME
* MOD_GRADE
* MOD_PASS
* MOD_RETAKE

##Grade
* STUDENT_ID
* MOD_INSTANCE_ID
* GRADABLE_OBJECT
* CATEGORY
* MAX_POINTS
* EARNED_POINTS
* WEIGHT
* GRADE_DATE

##Activity
* STUDENT_ID
* MOD_ID
* EVENT
* EVENT_DATE


# Definitions
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

##ULN
###Description
Unique Learner Number. For initial trial and data model development for the predictive model, this field should be left NULL.

###Purpose
For future use, tracking student journey.

###Derivation
Skills Funding Agency: See https://www.gov.uk/government/publications/lrs-unique-learner-numbers

###References

###Format
String (10)

###Compulsory
No

###Notes
The ULN can be provided as an additional point of reference, however the STUDENT_ID will always take precedence as the unique learner/ student identifier

##DOB
###Description
Student's date of birth

###Purpose
For analytics comparisons.

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^BIRTHDTE.html

###References

###Format
ISO8601 format of YYYY-MM-DD

###Compulsory
Yes

###Notes
Cannot be NULL - a valid date of birth must be provided for all learners. A date of birth of 2099-12-31 can be provided on a temporary basis.

##ETHNICITY
###Description
This field records the ethnicity of the student, on the basis of their own self-assessment

###Purpose
To allow equal opportunities monitoring, within detailed learning analytics/ data modelling.

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^ETHNIC.html

###Format
String (10)

###Valid Values & Mappings:

CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)	HESA - ETHNIC	FE ILR - ETHNICITY
10	White	Gwyn	10	31
13	White - Scottish	Gwyn - Alban	13	N/A
51	Irish	Gwyddel	N/A	32
14	Irish Traveller		14	N/A
15	Gypsy or Traveller		15	33
19	Other White background	Gwyn Arall	19	34
21	Black or Black British - Caribbean		21	45
22	Black or Black British - African		22	44
29	Other Black background		29	46
31	Asian or Asian British - Indian		31	39
32	Asian or Asian British - Pakistani		32	40
33	Asian or Asian British - Bangladeshi		33	41
34	Chinese		34	42
39	Other Asian background		39	43
41	Mixed - White and Black Caribbean		41	35
42	Mixed - White and Black African		42	36
43	Mixed - White and Asian		43	37
49	Other mixed background		49	38
50	Arab		50	47
80	Other ethnic background	Cefndir Ethnig Arall	80	98
90	Not known	Anhysbys	90	N/A
98	Information refused		98	99
90	Not known	Anhysbys	NULL	NULL
 
Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)

###Compulsory
Yes

###Notes
Where any ethnicity details are unknown, this field must be coded with '90'

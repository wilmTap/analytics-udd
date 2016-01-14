
##Institution
* [TENANT_ID](#tenant_id)
* [TENANT_NAME](#tenant_name)

##Student
* [STUDENT_ID](#student_id)
* [ULN](#uln)
* [DOB](#dob)
* [ETHNICITY](#ethnicity)
* [GENDER](#gender)
* [AGE](#age)
* [LEARN_DIF](#learn_dif)
* [DISABILITY1](#disability1)
* [DISABILITY2](#disability2)
* [DOMICILE](#domicile)
* [TERMTIME_ACCOM](#termtime_accom)
* [PARENTS_ED](#parents_ed)
* [SOCIO_EC](#socio_ec)
* [OVERSEAS](#overseas)

##Course
* [COURSE_ID](#course_id)
* [SUBJECT](#subject)
* [TITLE](#title)
* [COURSE_AIM](#course_aim)

##Course Instance
* [COURSE_ID](#course_id)
* [COURSE_INSTANCE_ID](#course_instance_id)
* [START_DATE](#start_date)
* [END_DATE](#end_date)
* [ACADEMIC_YEAR](#academic_year)

##Student on Course Instance
* [STUDENT_ID](#student_id)
* [COURSE_INSTANCE_ID](#course_instance_id)
* [WITHDRAWAL_REASON](#withdrawal_reason)
* [WITHDRAWAL_DATE](#withdrawal_date)
* [MODE](#mode)
* [YEAR_COM](#year_com)
* [YEAR_PRG](#year_prg)
* [YEAR_STU](#year_stu)
* [COURSE_AVERAGE_GRADE](#course_average_grade)
* [YEAR_AVERAGE_GRADE](#year_average_grade)
* [ENTRY_QUALS](#entry_quals)
* [ENTRY_POINTS](#entry_points)
* [COURSE_OUTCOME](#course_outcome)
* [COURSE_GRADE](#cpurse_grade)

##Module
* [MOD_ID](#mod_id)
* [MOD_NAME](#mod_name)
* [MOD_SUBJECT](#mod_subject)
* [MOD_CREDITS](#mod_credits)

##Module Instance
* [MOD_ID](#mod_id)
* [MOD_INSTANCE_ID](#mod_instance_id)
* [MOD_START_DATE](#mod_start_date)
* [MOD_END_DATE](#mod_end_date)
* [MOD_PERIOD](#mod_period)
* [MOD_ONLINE](#mod_online)
* [MOD_ENROLLMENT](#mod_enrollment)
* [MOD_ACADEMIC_YEAR](#mod_academic_year)
* [MOD_OPTIONAL](#mod_optional)
* [MOD_LEVEL](#mod_level)

##Student on a module Instance
* [STUDENT_ID](#student_id)
* [COURSE_INSTANCE_ID](#course_instance_id)
* [MOD_INSTANCE_ID](#mod_instance_id)
* [MOD_OUTCOME](#mod_outcome)
* [MOD_GRADE](#mod_grade)
* [MOD_PASS](#mod_pass)
* [MOD_RETAKE](#mod_retake)

##Grade
* [STUDENT_ID](#student_id)
* [MOD_INSTANCE_ID](#mod_instance_id)
* [GRADABLE_OBJECT](#gradable_object)
* [CATEGORY](#category)
* [MAX_POINTS](#max_points)
* [EARNED_POINTS](#earned_points)
* [WEIGHT](#weight)
* [GRADE_DATE](#grade_date)

##Activity
* [STUDENT_ID](#student_id)
* [MOD_ID](#mod_id)
* [EVENT](#event)
* [EVENT_DATE](#event_date)

# Definitions

#INSTITUTION ENTITY
##TENANT_ID
###Description
This field records the unique identifier for the University College concerned - using the UK Provider Reference Number (UKRPN) which is the unique identifier allocated to institutions by the UK Register of Learning Providers (UKRLP).

###Purpose
To identify the organisation.

###Derivation
UK Register of Learning Providers (UKRLP).

###References

###Format
String (8)

###Compulsory
Yes

###Notes
Further information (on UKPRN) available at www.ukrlp.co.uk

##TENANT_NAME
###Description
Institution's official legal name. This should match the name indicated in the UKRLP database, as used for TENANT_ID

###Purpose
To identify the organisation.

###Derivation
Insitution

###References

###Format
String (255)

###Compulsory
Yes

###Notes

#STUDENT ENTITY
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

##GENDER
###Description
To record a Learner's current gender assignment, on the basis of their own self-assessment

###Purpose
For equal opportunities monitoring within learning analytics / data modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^SEXID.html

###Format
Int

###Valid Values & Mappings

CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(SEXID),FEILR(SEX)
1,Male,Gwryw,1,M
2,Female,Beny,2,F
3,Other,Arall,3,N/A
4,Unknown,Anhysbys,NULL,NULL

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL) 

###Compulsory
Yes

###Notes
If the gender is unknown, return code '4' in all cases


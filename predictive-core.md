
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

###CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(SEXID),FEILR(SEX)
1,Male,Gwryw,1,M
2,Female,Beny,2,F
3,Other,Arall,3,N/A
4,Unknown,Anhysbys,NULL,NULL

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL) 

###Compulsory
Yes

###Notes
If the gender is unknown, return code '4' in all cases

##AGE
###Description
The current age of the learner/ student

###Purpose
To be used purely for display purposes within the Learning Analytics software suite

###Format
Int

###Compulsory
Yes - Learning Analytics system calculated field

###Notes
This will typically auto-calculated on a daily basis, based on field DOB. The LA system will provide this field.

##LEARN_DIF
###Description
This field records whether the learner considers themselves to have a learning difficulty

###Purpose
For detailed analysis or intervention purposes within Learning Analytics eg. Data Insight Tool

###Derivation
https://www.hesa.ac.uk/component/studrec/show_file/14051/a%5E_%5ELEARNDIF.html

###Valid Values & Mappings
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)	HESA - LEARNDIF	FE ILR - LLDDCAT
1	Moderate learning difficulty		1	10
2	Severe learning difficulty		2	11
10	Dyslexia		10	12
11	Dyscalculia		11	13
19	Other specific learning difficulty		19	94
20	Autism spectrum disorder		20	14
90	Multiple learning difficulties		90	3
97	Other		97	96
98	No learning difficulty		98	N/A
99	Not known / information not provided		99	N/A
98	No learning difficulty		NULL	NULL

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)

###Format
Int

###Compulsory
Yes

###Notes
If a learner's learning difficulty is unknown, then code '99' should be used for those cases

##DISABILITY1
###Description
Whether the student is indicated as being disabled, according to their own self-assessment. This will be their primary disability.

###Purpose
For equal opportunities monitoring within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5eDISABLE.html

###Valid Values & Mappings
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)	HESA - DISABLE	HE ILR - LLDDCat
0	No known disability	Dim Anabledd	0	N/A
58	Blind or a serious visual impairment uncorrected by glasses		2	N/A
57	Deaf or a serious hearing impairment		3	N/A
56	A physical impairment or mobility issues, such as difficulty using arms or using a wheelchair or crutches		4	N/A
96	A disability, impairment or medical condition that is not listed above		5	N/A
55	A mental health condition, such as depression, schizophrenia or anxiety disorder		6	N/A
96	A disability, impairment or medical condition that is not listed above		7	N/A
8	Two or more impairments and/or disabling medical conditions		8	2
51	A specific learning difficulty such as dyslexia, dyspraxia or AD(H)D		11	12
53	A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder		53	15
53	A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder		N/A	1
54	A long standing illness or health condition such as cancer, HIV, diabetes, chronic heart disease, or epilepsy		54	95
55	A mental health condition, such as depression, schizophrenia or anxiety disorder		55	9
56	A physical impairment or mobility issues, such as difficulty using arms or using a wheelchair or crutches		56	6
56	A physical impairment or mobility issues, such as difficulty using arms or using a wheelchair or crutches		N/A	93
57	Deaf or a serious hearing impairment		57	5
58	Blind or a serious visual impairment uncorrected by glasses		58	4
96	A disability, impairment or medical condition that is not listed above		96	7
96	A disability, impairment or medical condition that is not listed above		N/A	8
96	A disability, impairment or medical condition that is not listed above		N/A	16
96	A disability, impairment or medical condition that is not listed above		N/A	97
97	Information refused		97	98
98	Information not sought		98	N/A
99	Not known	Anhysbys	99	99
0	No known disability	Dim Anabledd	NULL	NULL

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)

###Format
Int

###Compulsory
Yes

###Notes
If disability is unknown, code '0' or '99' should be provided

##DISABILITY2
###Description
Whether the student is indicated as being disabled, according to their own self-assessment. This will be their secondary disability.

###Purpose
For equal opportunities monitoring within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5eDISABLE.html

###Valid Values & Mappings
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)	HESA - DISABLE	HE ILR - LLDDCat
0	No known disability	Dim Anabledd	0	N/A
58	Blind or a serious visual impairment uncorrected by glasses		2	N/A
57	Deaf or a serious hearing impairment		3	N/A
56	A physical impairment or mobility issues, such as difficulty using arms or using a wheelchair or crutches		4	N/A
96	A disability, impairment or medical condition that is not listed above		5	N/A
55	A mental health condition, such as depression, schizophrenia or anxiety disorder		6	N/A
96	A disability, impairment or medical condition that is not listed above		7	N/A
8	Two or more impairments and/or disabling medical conditions		8	2
51	A specific learning difficulty such as dyslexia, dyspraxia or AD(H)D		11	12
53	A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder		53	15
53	A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder		N/A	1
54	A long standing illness or health condition such as cancer, HIV, diabetes, chronic heart disease, or epilepsy		54	95
55	A mental health condition, such as depression, schizophrenia or anxiety disorder		55	9
56	A physical impairment or mobility issues, such as difficulty using arms or using a wheelchair or crutches		56	6
56	A physical impairment or mobility issues, such as difficulty using arms or using a wheelchair or crutches		N/A	93
57	Deaf or a serious hearing impairment		57	5
58	Blind or a serious visual impairment uncorrected by glasses		58	4
96	A disability, impairment or medical condition that is not listed above		96	7
96	A disability, impairment or medical condition that is not listed above		N/A	8
96	A disability, impairment or medical condition that is not listed above		N/A	16
96	A disability, impairment or medical condition that is not listed above		N/A	97
97	Information refused		97	98
98	Information not sought		98	N/A
99	Not known	Anhysbys	99	99
0	No known disability	Dim Anabledd	NULL	NULL

Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)

###Format
Int

###Compulsory
Yes

###Notes
If disability is unknown, code '0' or '99' should be provided

##DOMICILE
###Description
This field holds the country code of the student's permanent home address prior to entry to the course. It is not necessarily the correspondence address of the student.

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5eDOMICILE.html

###Format
String (2)

###Valid Values (No Mappings)
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5eDOMICILE.html

###Compulsory
Yes

###Notes
If a domicile country is unknown, please use code 'ZZ'

##TERMTIME_ACCOM
###Description
The current term time accomodation type of student

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5eTTACCOM.html

###Valid Values & Mappings
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)	HESA - TTACCOM	FE ILR - ACCOM
1	Provider maintained property		1	5
2	Parental/guardian home		2	N/A
4	Other	Arall	4	NULL
5	Not known	Anhysbys	5	N/A
6	Not in attendance at the provider		6	N/A
7	Own residence		7	N/A
8	Other rented accommodation		8	N/A
9	Private-sector halls		9	N/A
5	Not known	Anhysbys	NULL	N/A
Please Note - N/A denotes that no mapping value is applicable (and should not be confused with NULL)

###Format
Int

###Compulsory
Yes

###Notes
If the type is unknown, code '5' should be used

##PARENTS_ED
###Description
Whether parents have higher education qualification

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5ePARED.html

###Valid Values
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)
1	Yes	Ie
2	No	Na
7	No response given	Dim Ateb
8	Don't know	Anhysbys
9	Information refused	Gwybodaeth wedi ei ddal yn ol

###Format
Int

###Compulsory
Yes

###Notes
Where this is unknown, the code '8' should be provided. This information may not be available for FE/ ILR institutions, and only HE.

##SOCIO_EC
###Description
This field collects the socio-economic classification of students participating in HE if 21 or over at the start of their course or parental classification if under 21

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^SEC.html

###Valid Values
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)
1	Higher managerial & professional occupations	
2	Lower managerial & professional occupations	
3	Intermediate occupations	
4	Small employers & own account workers	
5	Lower supervisory & technical occupations	
6	Semi-routine occupations	
7	Routine occupations	
8	Never worked & long-term unemployed	
9	Not classified	Dim math

###Format
Int

###Compulsory
Yes for HE

###Notes
Where this is unknown, the code '9' should be provided. This information may not be available for FE/ ILR institutions, and only HE.

##OVERSEAS
###Description
Whether the student is classified as a home student (UK), or European (EU) or as Overseas (rest of the world)

###Purpose
For detailed analysis within Learning Analytics/ Data Modelling

###Derivation
Jisc

###Valid Values
CODE	DESCRIPTION (ENGLISH)	DESCRIPTION (WELSH)
1	United Kingdom	Deyrnas Unedig
2	Europe (EU)	Ewrop (UE)
3	Rest of the World (Overseas)	Gweddill y Byd
99	Not Known	Anhysbys

###Format
Int

###Compulsory
Yes

###Notes
If this value is unknown, then code '99' should be used. The mapping for these fields could be done using the Nationality indicator, or other relevant source within the HESA/ student records system database.

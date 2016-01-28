
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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(ETHNIC),FEILR(ETHNICITY)  
10,White,Gwyn,10,31    
13,White - Scottish,Gwyn - Alban,13,N/A  
51,Irish,Gwyddel,N/A,32  
14,Irish Traveller,14,N/A  
15,Gypsy or Traveller,,15,33  
19,Other White background,Gwyn Arall,19,34  
21,Black or Black British - Caribbean,,21,45  
22,Black or Black British - African,,22,44  
29,Other Black background,,29	46  
31,Asian or Asian British - Indian,,31,39  
32,Asian or Asian British - Pakistani,,32.40  
33,Asian or Asian British - Bangladeshi,,33,41  
34,Chinese,,34,42  
39,Other Asian background,,39,43  
41,Mixed - White and Black Caribbean,,41,35  
42,Mixed - White and Black African,,42,36  
43,Mixed - White and Asian,,43,37  
49,Other mixed background,,49,38  
50,Arab,,50,47  
80,Other ethnic background,Cefndir Ethnig Arall,80,98  
90,Not known,Anhysbys,90,N/A  
98,Information refused,,98,99  
90,Not known,Anhysbys,NULL,NULL  
 
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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(LEARNDIF),FEILR(LLDDCAT)  
1,Moderate learning difficulty,,1,10  
2,Severe learning difficulty,,2,11  
10,Dyslexia,,10,12  
11,Dyscalculia,,11,13  
19,Other specific learning difficulty,,19,94  
20,Autism spectrum disorder,,20,14  
90,Multiple learning difficulties,,90,3  
97,Other,,97,96  
98,No learning difficulty,,98,N/A  
99,Not known / information not provided,,99,N/A  
98,No learning difficulty,,NULL,NULL  

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(DISABLE),FEILR(LLDDCat)  
0,No known disability,Dim Anabledd,0,N/A  
58,Blind or a serious visual impairment uncorrected by glasses,,2,N/A  
57,Deaf or a serious hearing impairment,,3,N/A  
56,A physical impairment or mobility issues such as difficulty using arms or using a wheelchair or crutches,,4,N/A  
96,A disability impairment or medical condition that is not listed above,,5,N/A  
55,A mental health condition such as depression schizophrenia or anxiety disorder,,6,N/A  
96,A disability impairment or medical condition that is not listed above,,7,N/A  
8,Two or more impairments and/or disabling medical conditions,,8,2  
51,A specific learning difficulty such as dyslexia dyspraxia or AD(H)D,,11,12  
53,A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder,,53,15  
53,A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder,,N/A,1  
54,A long standing illness or health condition such as cancer HIV diabetes chronic heart disease or epilepsy,,54,95  
55,A mental health condition such as depression schizophrenia or anxiety disorder,,55,9  
56,A physical impairment or mobility issues such as difficulty using arms or using a wheelchair or crutches,,56,6  
56,A physical impairment or mobility issues such as difficulty using arms or using a wheelchair or crutches,,N/A,93  
57,Deaf or a serious hearing impairment,,57,5  
58,Blind or a serious visual impairment uncorrected by glasses,,58,4  
96,A disability impairment or medical condition that is not listed above,,96,7  
96,A disability impairment or medical condition that is not listed above,,N/A,8  
96,A disability impairment or medical condition that is not listed above,,N/A,16  
96,A disability impairment or medical condition that is not listed above,,N/A,97  
97,Information refused,,97,98  
98,Information not sought,,98,N/A  
99,Not known,Anhysbys,99,99  
0,No known disability,Dim Anabledd,NULL,NULL  

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(DISABLE),FEILR(LLDDCat)  
0,No known disability,Dim Anabledd,0,N/A  
58,Blind or a serious visual impairment uncorrected by glasses,,2,N/A  
57,Deaf or a serious hearing impairment,,3,N/A  
56,A physical impairment or mobility issues such as difficulty using arms or using a wheelchair or crutches,,4,N/A  
96,A disability impairment or medical condition that is not listed above,,5,N/A  
55,A mental health condition such as depression schizophrenia or anxiety disorder,,6,N/A  
96,A disability impairment or medical condition that is not listed above,,7,N/A  
8,Two or more impairments and/or disabling medical conditions,,8,2  
51,A specific learning difficulty such as dyslexia dyspraxia or AD(H)D,,11,12  
53,A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder,,53,15  
53,A social/communication impairment such as Asperger's syndrome/other autistic spectrum disorder,,N/A,1  
54,A long standing illness or health condition such as cancer HIV diabetes chronic heart disease or epilepsy,,54,95  
55,A mental health condition such as depression schizophrenia or anxiety disorder,,55,9  
56,A physical impairment or mobility issues such as difficulty using arms or using a wheelchair or crutches,,56,6  
56,A physical impairment or mobility issues such as difficulty using arms or using a wheelchair or crutches,,N/A,93  
57,Deaf or a serious hearing impairment,,57,5  
58,Blind or a serious visual impairment uncorrected by glasses,,58,4  
96,A disability impairment or medical condition that is not listed above,,96,7  
96,A disability impairment or medical condition that is not listed above,,N/A,8  
96,A disability impairment or medical condition that is not listed above,,N/A,16  
96,A disability impairment or medical condition that is not listed above,,N/A,97  
97,Information refused,,97,98  
98,Information not sought,,98,N/A  
99,Not known,Anhysbys,99,99  
0,No known disability,Dim Anabledd,NULL,NULL  

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(TTACCOM),FEILR(ACCOM)  
1,Provider maintained property,,1,5  
2,Parental/guardian home,,2,N/A  
4,Other,Arall,4,NULL  
5,Not known,Anhysbys,5,N/A  
6,Not in attendance at the provider,,6,N/A  
7,Own residence,,7,N/A  
8,Other rented accommodation,,8,N/A  
9,Private-sector halls,,9,N/A  
5,Not known,Anhysbys,NULL,N/A    

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Yes,Ie  
2,No,Na  
7,No response given,Dim Ateb  
8,Don't know,Anhysbys  
9,Information refused,Gwybodaeth wedi ei ddal yn ol  

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Higher managerial & professional occupations,  
2,Lower managerial & professional occupations,   
3,Intermediate occupations,  
4,Small employers & own account workers,  
5,Lower supervisory & technical occupations,  	
6,Semi-routine occupations,  	
7,Routine occupations,  	
8,Never worked & long-term unemployed,  	
9,Not classified,Dim math  

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)
1,United Kingdom,Deyrnas Unedig  
2,Europe (EU),Ewrop (UE)  
3,Rest of the World (Overseas),Gweddill y Byd  
99,Not Known,Anhysbys  

###Format
Int

###Compulsory
Yes

###Notes
If this value is unknown, then code '99' should be used. The mapping for these fields could be done using the Nationality indicator, or other relevant source within the HESA/ student records system database.

##COURSE_ID
###Description
The providers own ID for the course

###Purpose
To link relational database tables

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^OWNCOURSEID.html
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^Course_COURSEID.html

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes

###Notes
HE guidance - this field could relate to actual HESA COURSEID field or the HR institution's OWNCOURSEID field for cross-referencing purposes.

##SUBJECT
###Description
Subject coding - using JACS3

###Purpose
For display purposes

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^SBJCA.html

###Valid Values
Valid JACS3 Code. See:
https://www.hesa.ac.uk/jacs3

###Format
String (10) - Usually 4 characters, number followed by three digits

###Compulsory
Yes

###Notes
The JACS3 coding will be used here initially, from the HE (HESA) model. Further discussion will be required around this, to discuss subject classifications for FE/ ILR.y

##TITLE
###Description
Course Name or Title

###Purpose
For display purposes

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^CTITLE.html

###Valid Value
Any

###Format
String (255)

###Compulsory
Yes

###Notes

##COURSE_AIM
###Description
The qualification which the learner/ student is aiming for at the provider

###Purpose
For display purposes and further analysis

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^COURSEAIM.html

###Valid Values
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^COURSEAIM.html
  
- plus additional codes X98 & X99 (see notes below)  

###References

###Format
String(255)

###Compulsory
Yes

###Notes
This field uses the HESA "COURSEAIM" codeset initially - with the addition of new code 'X98' to denote 'No formal qualification aim, below FE level' for FE equivalent denotation to HE code 'X99'. All course levels are denoted here (TBC with FE college, for final implementation). Specific use of the LARS codeset for FE (from ILR) may need to be considered, or a mapping/ amalgamation with the HESA codeset. This is to be discussed in consultation with the FE sector.

##COURSE_INSTANCE_ID
###Description
Institution's identifier for this course instance

###Purpose
To link student to course, and course to course instance

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes

###Notes

##START_DATE
###Description
Start date for this course instance

###Purpose
For analytics

###Derivation
Jisc

###Valid Values
Date in ISO8601 format - YYYY-MM-DD

###Format
String (255)

###Compulsory
Yes

###Notes

##END_DATE
###Description
End date for this course instance

##Purpose
For analytics

###Derivation
Jisc

###Valid Values
Date in ISO8601 format - YYYY-MM-DD

###Format
String (255)

###Compulsory
Yes

###Notes

##ACADEMIC_YEAR
###Description
Academic year to which the course instance relates. 

###Purpose
For display and analysis purposes

###Derivation
Jisc

###Valid Values
Year as four digit - ie year that the academic year starts in.

###Format
Int

###Compulsory
Yes

###Notes
Could be derived, but academic year calendars may be different between institutions. This field could also be sourced directly from the SRS.

##WITHDRAWAL_REASON
###Description
The reason a student has withdrawn from a course (if they have)

###Purpose
For analytics

###Derivation
Based on the ILR codeset used for 'WithdrawReason' - with HESA code '05' utilised. For further information visit:

https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^WITHDRAWREASON.html
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^RSNEND.html

###Valid Values & Mappings 
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(WITHDRAWREASON),HESA(RSNEND),FEILR(WITHDRAWREASON)  
2,Learner has transferred to another provider,,02,03,2  
3,Learner injury / illness,,03,04,3   
5,Death,,N/A,05,N/A  
7,Learner has transferred between providers due to intervention by the Skills Funding Agency,,07,N/A,7  
10,Gone into employment,,N/A,10,N/A  
28,OLASS learner withdrawn due to circumstances outside the providers’ control,,N/A,N/A,28  
29,Learner has been made redundant,,29,N/A,29  
40,Learner has transferred to a new learning aim with the same provider,,40,N/A,40  
41,Learner has transferred to another provider to undertake learning that meets a specific government strategy,,41,N/A,41  
42,Academic failure/left in bad standing/not permitted to progress – HE learning aims only,,N/A,02,42  
43,Financial reasons,,N/A,06,43  
44,Other personal reasons,,N/A,07,44  
45,Written off after lapse of time (HE learning aims only),,N/A,08,45  
46,Exclusion,,N/A,09,46  
97,Other,,97,11,97  
98,Reason not known,,98,99,98  
98,Reason not known,,NULL,N/A,NULL  
99,Completion of course - result unknown,,N/A,98,N/A  

###Format
Int

###Compulsory
Yes (if applicable)

###Notes

##WITHDRAWAL_DATE
###Description
The date a student has withdrawn from a course (if they have)

###Purpose
For analytics

###Derivation
https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^ENDDATE.html

###Valid Values
ISO Date - YYYY-MM-DD

###Format
Int

###Compulsory
Yes (if applicable)

###Notes
Would normally utilise ENDDATE (HE/ HESA) or potentially LearnActEndDate (FE/ ILR - to be confirmed) when relevant fields denote that the learner/ student has withdrawn from the learning aim/ course.

###MODE
###Description
Mode of study (eg part-time or full time)

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MODE.html

###Valid Values & Mappings
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(MODE),FEILR(PlanLearnHours)  
1,Full-time according to funding council definitions,,1,PlanLearnHours >= 540  
2,Other full-time,,2,N/A  
12,FE students full-time 30 weeks or more,,12,N/A  
13,FE students full-time 4-29 weeks,,13,N/A  
14,FE students full-time less than 4 weeks,,14,N/A  
23,Sandwich (thick) according to funding council definitions,,23,N/A  
24,Sandwich (thin) according to funding council definitions,,24,N/A  
25,Other sandwich course/programme,,25,N/A  
31,Part-time,,31,PlanLearnHours < 540  
33,FE students part-time released from employment,,33,N/A  
34,FE students part-time not released from employment,,34,N/A  
35,FE students evening only,,35,N/A  
36,FE students open or distance learning,,36,N/A  
38,Structured part-time (providers in Scotland),,38,N/A  
39,Other part-time (providers in Scotland),,39,N/A  
43,Writing-up - previously full-time,,43,N/A  
44,Writing-up - previously part-time,,44,N/A  
51,Sabbatical,,51,N/A  
63,Dormant - previously full-time,,63,N/A  
64,Dormant - previously part-time,,64,N/A  
6,FE students continuous delivery day/daytime,,65,N/A  
73,Change to dormant status - previously full-time,,73,N/A  
74,Change to dormant status - previously part-time,,74,N/A  
99,FE students in England,,99,N/A  
98,Not Known/ Not in Early Statistics/HEIFES population,,NULL,NULL  

###Format
Int

###Compulsory
Yes (if applicable)

###Notes
Mapping based on HESA codeset, and ILE (FE) initial mapping suggested above on ILR field 'PlanLearnHours'.

##YEAR_COM
###Description
This field indicates the year number that the learning aim/ course started

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^COMDATE.html

###Valid Values
Any

###Format
Int

###Compulsory
Yes (if applicable)

###Notes
This can be extracted from the actual commencement date of the learning aim/ student (on course) instance.

##YEAR_PRG
###Description
This field indicates the year number of the course that the student is currently studying. This could be different from the year of student if the student has changed course or re-taken a year.

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^YEARPRG.html

###Valid Values
Any

###Format
Int

###Compulsory
Yes (if applicable)

###Notes

##YEAR_STU
###Description
Year number that the student is in since enrolling for a course

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a%5e_%5eYEARSTU.html

###Valid Values
Any

###Format
Int

###Compulsory
Yes (if applicable)

###Notes

##COURSE_AVERAGE_GRADE
###Description
The current (LIVE) course grade of the learner

###Purpose
For display & analytics

###Derivation
Jisc

###Valid Values
Codeset to be confirmed - specific per institution

###Format
Int

###Compulsory
Yes (if applicable)

###Notes
This can either be implemented on the LA sides (via a suitable algorithm provided by the institution) or derived on the instituion's side, and provided in real time (push operation) to the Learning Analytics data warehouse.

##YEAR_AVERAGE_GRADE
###Description
The current (LIVE) annual (current year) grade of the learner

###Purpose
For display & analytics

###Derivation
Jisc

###Valid Values
Codeset to be confirmed - specific per institution

###Format
Int

###Compulsory
Yes (if applicable)

###Notes
This can either be implemented on the LA sides (via a suitable algorithm provided by the institution) or derived on the instituion's side, and provided in real time (push operation) to the Learning Analytics data warehouse.

##ENTRY_QUALS
###Description
The classification of entry qualifications, prior to entry to the institution

###Purpose
For display & analytics

###Derivation
Based on HESA codings for QUALENT3, but merged with specific element of the FE ILR field 'PriorAttain'
https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^QUALENT3.html

###Valid Values & Mappings
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH),HESA(QUALENT3),FEILR(PRIORATTAIN)   
DUK,UK doctorate degree,,DUK, 	
DZZ,Non-UK doctorate degree,,DZZ,  	
D80,Other qualification at level D,,D80,  	
MUK,UK masters degree,,MUK,  	
MZZ,Non-UK masters degree,,MZZ,  	
M2X,Integrated undergraduate/postgraduate taught masters degree on the enhanced/extended pattern,,M2X,  	
M41,Diploma at level M,,M41,  	
M44,Certificate at level M,,M44,  	
M71,Postgraduate Certificate in Education or Professional Graduate Diploma in Education,,M71,  	
M80,Other taught qualification at level M,,M80,  	
M90,Taught work at level M for provider credit,,M90,  	
M91,(Other) Qualification at level 7 or above,,N/A,13  
HUK,UK first degree with honours,,HUK,  	
HZZ,Non-UK first degree,,HZZ,  	
H11,First degree with honours leading to Qualified Teacher Status (QTS)/registration with a General Teaching Council (GTC),,H11,  	
H71,Professional Graduate Certificate in Education,,H71,  	
H80,(Other) Qualification at level H or level 6,,H80,12  
JUK,UK ordinary (non-honours) first degree,,JUK,  	
J10,Foundation degree,,J10,  
J20,Diploma of Higher Education (DipHE),,J20,  	
J30,Higher National Diploma (HND),,J30,  	
J31,(Other) Qualification at level 5,,,  		
J31,(Other) Qualification at level 5 or above (DEPRECATED SINCE 01/08/2013),,J32,5  
J49,Foundation course at level J,,J49,  	
J48,Certificate in Education (CertEd) or Diploma in Education (DipEd) (i.e. non-graduate initial teacher training qualification),,J48,  	
J80,Other qualification at level J,,J80,  	
C20,Certificate of Higher Education (CertHE),,C20,  	
C30,Higher National Certificate (HNC),,C30, 	
C44,Higher Apprenticeship (level 4),,C44,  	
C80,(Other) Qualification at level C or level 4,,C80,4  
C80,(Other) Qualification at level C or level 4,,N/A,10  
C90,Undergraduate credits,,C90,  	
P41,Diploma at level 3,,P41,  	
P42,Certificate at level 3,,P42,  	
P46,Award at level 3,,P46,  	
P47,AQA Baccalaureate (Bacc),,P47,  	
P50,A/AS level,,P50,  	
P51,14-19 Advanced Diploma (level 3),,P51,  	
P53,Scottish Baccalaureate,,P53,  	
P54,Scottish Highers/Advanced Highers,,P54,  	
P62,International Baccalaureate (IB) Diploma,,P62,  	
P63,International Baccalaureate (IB) Certificate,,P63,  	
P64,Cambridge Pre-U Diploma,,P64,  	
P65,Cambridge Pre-U Certificate,,P65,  	
P68,Welsh Baccalaureate Advanced Diploma (level 3),,P68,  	
P80,(Other) Qualification at level 3,,P80,3  
P91,Level 3 qualifications of which some or all are subject to UCAS Tariff,,P91,  	
P92,Level 3 qualifications of which none are subject to UCAS Tariff,,P92,  	
P93,Level 3 qualifications of which all are subject to UCAS Tariff,,P93,  	
P94,Level 3 qualifications of which some are subject to UCAS Tariff,,P94,  	
Q51,14-19 Higher Diploma (level 2),,Q51,  	
Q52,Welsh Baccalaureate Intermediate Diploma (level 2),,Q52,  	
Q80,(Other) Qualification at level 2,,Q80,2  
R51,14-19 Foundation Diploma (level 1),,R51,  	
R52,Welsh Baccalaureate Foundation Diploma (level 1),,R52,  	
R80,Other qualification at level 1,,R80,1  
X07,(Other) Qualification below level 1,,NULL,7  
X00,Higher education (HE) access course Quality Assurance Agency (QAA) recognised,,X00,  	
X01,Higher education (HE) access course not Quality Assurance Agency (QAA) recognised,,X01,  	
X02,Mature student admitted on basis of previous experience and/or admissions test,,X02,  	
X04,Other qualification level not known,,X04,97  
X05,Student has no formal qualification,,X05,99  
X06,Not known,,X06,98  
X06,Not known,,NULL,NULL  

###Format
Alphanumeric

###Compulsory
Yes (if applicable)

###Notes

##ENTRY_POINTS
###Description
This field indicates the entry points gained by the student/ learner prior to entry to the institution. This is currently based on the UCAS entry points system. This field must be adapted or used to represent those points for entry into FE eg. using a formula to combine & calculate points to represent Maths and English qualifications upon entry for example

###Purpose
For analytics

###Derivation
Jisc

###Valid Values
Any

###Format
Int

###Compulsory
No

###Notes

##COURSE_OUTCOME
###Description
This field indicates the outcome/ status of the learner's current course or learning aim. This is based on the information provided by HESA via the RSNEND field, however this has been adapted with the addition of fields to cater for FE (via the ILR CompStatus field), and can be used to fully cater for the outcomes in granular detail

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^RSNEND.html
https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf

###Valid Values
Any integer

###Format
Int

###Compulsory
Yes (if applicable)

###Notes

##COURSE_GRADE
###Description
Class of award achieved by the student on this course instance. Based on HESA codeset for CLASS (HE conformity to be confirmed)

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^CLASS.html

###Valid Values
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,First class honours,  	
2,Upper second class honours,  	
3,Lower second class honours, 	
4,Undivided second class honours, 	
5,Third class honours, 	
6,Fourth class honours, 	
7,Unclassified honours, 	
8,Aegrotat (whether to honours or pass), 	
9,Pass - degree awarded without honours following an honours course, 	
10,Ordinary (to include divisions of ordinary, if any) - degree awarded after following a non-honours course, 	
11,General degree - degree awarded after following a non-honours course/degree that was not available to be classified, 	
12,Distinction, 	
13,Merit, 	
14,Pass, 	
51,A FE, 	
52,B FE, 	
53,C FE, 	
54,D FE, 	
55,E FE, 	
56,F FE, 	
57,G FE, 	
61,N FE, 	
62,U FE, 	
63,X FE, 	
64,A* FE, 	
65,Y FE, 	
71,Pass FE, 	
72,Merit FE, 	
73,Distinction FE, 	
74,Fail FE, 	
81,1 FE, 	
82,2 FE, 	
83,3 FE, 	
84,4 FE, 	
85,5 FE, 	
86,6 FE, 	
87,7 FE, 	
88,8 FE, 	
89,9 FE,  
90,10 FE,  
91,Not yet awarded,  

###Format
Int

###Compulsory
Yes (if applicable)

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

##MOD_NAME
###Description
The actual name of the module

###Purpose
For display purposes.

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MTITLE.html

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes

##MOD_SUBJECT
###Description
Module subject - coded using JACS3 subject codes (initially, for HE purposes)

###Purpose
For display purposes and analytics.

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MODSBJ.html

###Valid Values
Valid JACS3 subject code. See link above.

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes
For FE purposes, it will need be adapted to work with institutions specific codeset for Learning Activities. Details to be confirmed.

##MOD_CREDITS
###Description
Number of credits award for the module

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^CRDTPTS.html

###Valid Values
Any

###Format
Int

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Semester 1,  
2,Semester 2,  
3,All Year,  
4,Term 1,  
5,Term 2,  
6,Term 3,  
7,Other,  

###Format
Int

###Compulsory
No (if applicable)

###Notes

##MOD_ONLINE
###Description
Whether this module instance is delivered wholly online

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Yes,Ie  
2,No,Na  

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
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Yes,Ie  
2,No,Na  

###Format
Int

###Compulsory
No (if applicable)

###Notes

##MOD_LEVEL
###Description
Level of credit points - indicates the level of module the student is studying. This has been initially based on the HESA field LEVELPTS, however may be utilised and adapted to also cater for FE

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
0,Entry level,  
1,HE Certificate/NVQ Level 4 or equivalent, 	
2,HE Intermediate, 	
3,HE Honours, 	
5,Undergraduate unspecified, 	
6,HE Masters, 	
7,HE Doctorate, 	
9,Not applicable, 	
A,NVQ level 1 or equivalent, 	
B,NVQ level 2 or equivalent, 	
C,NVQ level 3 or equivalent, 	
D,HND/Diploma HE, 	
E,Ordinary degrees, 	
 
###Format
String(1)

###Compulsory
No (if applicable)

###Notes

##MOD_OUTCOME
###Description
This field records if the student completed the module and if so whether they gained credit or not. There should be a Module Outcome field for each module taken by the student.

###Purpose
Analytics 

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MODOUT.html

###Valid Values
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Completion - gained full credit, 	
2,Completion - did not gain credit, 	
3,Partial completion (HEFCW HESES Rules), 	
4,Student did not complete module, 	
5,Module taken on a not-for-credit basis, 	
6,Module outcome not yet known, 	
7,Not coded, 	
9,Module previously returned in error, 	
A,Student did not complete module - gained credit, 	
B,Student did not complete module - deferral, 	
C,Completion - award of credit not known, 	

###Format
String(1)

###Compulsory
Yes

###Notes

##MOD_GRADE
###Description.
Final grade student achieved on the module.

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
1-100

###Format
Int

###Compulsory
Yes

###Notes
Where the module is grades as percentage then the an integer value (0-100) should be used.  Where a non-percentage marking scheme is used (eg A,B,C) this should be encoded numerically, with 1 being the lowest mark.

##MOD_PASS
###Description.
Whether the student passed or not.

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Yes,Ie  
2,No,Na  
3,Not completed yet,Dim wedi cwblhau  

###Format
Int

###Compulsory
Yes

###Notes
This can be calculated and derived from MOD_OUTCOME if required.

##MOD_RETAKE
###Description.
Whether this is a retake of the module for that student.

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values
CODE,DESCRIPTION(ENGLISH),DESCRIPTION(WELSH)  
1,Yes,Ie  
2,No,Na  
3,Not completed yet,Dim wedi cwblhau  

###Format
Int

###Compulsory
No

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


#Student on Course Instance
* [STUDENT_ID](student.md#student_id)
* [STUDENT_COURSE_MEMBERSHIP_ID](student_course_membership.md#student_course_membership_id)
* [STUDENT_COURSE_MEMBERSHIP_SEQ](student_course_membership.md#student_course_membership_seq)
* [MODE](#mode)
* [YEAR_COM](#year_com)
* [YEAR_PRG](#year_prg)
* [YEAR_STU](#year_stu)
* [COURSE_LOCATION](#course_location)
* [X_COURSE_AVERAGE_MARK](#course_average_mark)
* [X_YEAR_AVERAGE_MARK](#year_average_mark)

##MODE
###Description
Mode of study (eg part-time or full time)

###Purpose
For analytics

###Derivation
Jisc

###Valid Values & Mappings

<table>
            <tr><td>CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td><td>HESA (MODE)</td><td>FEILR (PlanLearnHours)  </td></tr>
            <tr><td>100</td><td>Full time</td><td></td><td>1, 2, 12, 13, 14, 23, 24, 25</td><td>PlanLearnHours > 540h</td></tr>
            <tr><td>200</td><td>Part-time</td><td></td><td>31, 33, 34, 35, 36, 38, 39, 43, 44, 65</td><td>PlanLearnHours &le; 540</td></tr>
            <tr><td>300</td><td>FE students in England</td><td></td><td>99</td><td>N/A</td></tr>
            <tr><td>400</td><td>On hiatus</td><td></td><td>51, 63, 64, 73, 74</td><td>N/A</td></tr>
            <tr><td>98</td><td>Not Known/ Not in Early Statistics/HEIFES population</td><td></td><td>N/A</td><td>N/A</td></tr>
            <tr><td>NULL</td><td>No data</td><td></td><td>NULL</td><td>NULL</td></tr>
        </table>

###Format
Int

###Compulsory
Yes (if applicable)

###Notes
Mapping based on HESA codeset, and ILE (FE) initial mapping suggested above on ILR field 'PlanLearnHours'. See https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MODE.html


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


##X_COURSE_AVERAGE_MARK
###Description
The current (LIVE) average of all module marks from across a learner's whole course.

###Purpose
For analytics

###Derivation
Jisc

###Valid Values
0-1

###Format
Float

###Compulsory
Yes (if applicable)

###Notes
This data is generated internally to the learning record warehouse from existing data, and does not need to be supplied by an institution.

##YEAR_AVERAGE_GRADE
###Description
The current (LIVE) average of all of this academic year's module marks from across a learner's whole course.

###Purpose
For analytics

###Derivation
Jisc

###Valid Values
0-1

###Format
Float

###Compulsory
Yes (if applicable)

###Notes
This data is generated internally to the learning record warehouse from existing data, and does not need to be supplied by an institution.

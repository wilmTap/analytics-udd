#Course
* [COURSE_ID](#course_id)
* [SUBJECT](#subject)
* [TITLE](#title)
* [COURSE_AIM](#course_aim)

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

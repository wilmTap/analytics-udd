#Student on Course Instance
* [STUDENT_ID](student.md#student_id)
* [STUDENT_COURSE_MEMBERSHIP_ID](student_course_membership.md#student_course_membership_id)
* [STUDENT_COURSE_MEMBERSHIP_SEQ](student_course_membership.md#student_course_membership_seq)
* [MODE](#mode)
* [YEAR_COM](#year_com)
* [YEAR_PRG](#year_prg)
* [YEAR_STU](#year_stu)
* [COURSE_AVERAGE_GRADE](#course_average_grade)
* [YEAR_AVERAGE_GRADE](#year_average_grade)
* [COURSE_LOCATION](#course_location)

###MODE
###Description
Mode of study (eg part-time or full time)

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MODE.html

###Valid Values & Mappings

<table>
<tr><td>CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)</td><td>HESA(MODE)</td><td>FEILR(PlanLearnHours)  </td></tr>
<tr><td>1</td><td>Full-time according to funding council definitions</td><td></td><td>1</td><td>PlanLearnHours >= 540  </td></tr>
<tr><td>2</td><td>Other full-time</td><td></td><td>2</td><td>N/A  </td></tr>
<tr><td>12</td><td>FE students full-time 30 weeks or more</td><td></td><td>12</td><td>N/A  </td></tr>
<tr><td>13</td><td>FE students full-time 4-29 weeks</td><td></td><td>13</td><td>N/A  </td></tr>
<tr><td>14</td><td>FE students full-time less than 4 weeks</td><td></td><td>14</td><td>N/A  </td></tr>
<tr><td>23</td><td>Sandwich (thick) according to funding council definitions</td><td></td><td>23</td><td>N/A  </td></tr>
<tr><td>24</td><td>Sandwich (thin) according to funding council definitions</td><td></td><td>24</td><td>N/A  </td></tr>
<tr><td>25</td><td>Other sandwich course/programme</td><td></td><td>25</td><td>N/A  </td></tr>
<tr><td>31</td><td>Part-time</td><td></td><td>31</td><td>PlanLearnHours &le; 540  </td></tr>
<tr><td>33</td><td>FE students part-time released from employment</td><td></td><td>33</td><td>N/A  </td></tr>
<tr><td>34</td><td>FE students part-time not released from employment</td><td></td><td>34</td><td>N/A  </td></tr>
<tr><td>35</td><td>FE students evening only</td><td></td><td>35</td><td>N/A  </td></tr>
<tr><td>36</td><td>FE students open or distance learning</td><td></td><td>36</td><td>N/A  </td></tr>
<tr><td>38</td><td>Structured part-time (providers in Scotland)</td><td></td><td>38</td><td>N/A  </td></tr>
<tr><td>39</td><td>Other part-time (providers in Scotland)</td><td></td><td>39</td><td>N/A  </td></tr>
<tr><td>43</td><td>Writing-up - previously full-time</td><td></td><td>43</td><td>N/A  </td></tr>
<tr><td>44</td><td>Writing-up - previously part-time</td><td></td><td>44</td><td>N/A  </td></tr>
<tr><td>51</td><td>Sabbatical</td><td></td><td>51</td><td>N/A  </td></tr>
<tr><td>63</td><td>Dormant - previously full-time</td><td></td><td>63</td><td>N/A  </td></tr>
<tr><td>64</td><td>Dormant - previously part-time</td><td></td><td>64</td><td>N/A  </td></tr>
<tr><td>6</td><td>FE students continuous delivery day/daytime</td><td></td><td>65</td><td>N/A  </td></tr>
<tr><td>73</td><td>Change to dormant status - previously full-time</td><td></td><td>73</td><td>N/A  </td></tr>
<tr><td>74</td><td>Change to dormant status - previously part-time</td><td></td><td>74</td><td>N/A  </td></tr>
<tr><td>99</td><td>FE students in England</td><td></td><td>99</td><td>N/A  </td></tr>
<tr><td>98</td><td>Not Known/ Not in Early Statistics/HEIFES population</td><td></td><td>N/A</td><td>N/A</td></tr>
<tr><td>NULL</td><td>No data</td><td></td><td>NULL</td><td>NULL</td></tr>
</table>  

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
The current (LIVE) average grade of the learner's whole course.

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
This can either be implemented on the Learning Analytics data warehouse (via a suitable algorithm provided by the institution) or derived on the institution's side, and provided in real time (push operation) to the Learning Analytics data warehouse.

##YEAR_AVERAGE_GRADE
###Description
The current (LIVE) average grade of the learner's whole course this academic year.

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
This can either be implemented on the Learning Analytics data warehouse (via a suitable algorithm provided by the institution) or derived on the institution's side, and provided in real time (push operation) to the Learning Analytics data warehouse.

##COURSE_LOCATION
###Description
Identifies the location with which a student on a course instance is associated, be it a building, a site or a campus.

###Purpose
For analytics (predictive model building) and for presenting analytics.

###Derivation
Loosely based on
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=15051&href=a^_^CAMPID.html

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes

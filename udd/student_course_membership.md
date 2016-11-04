#student_course_membership

* [STUDENT_COURSE_MEMBERSHIP_ID](#student_course_membership_id) [1] *
* [STUDENT_COURSE_MEMBERSHIP_SEQ](#student_course_membership_seq) [1]
* [STUDENT_ID](student.md#student_id) [1]
* [COURSE_ID](course.md#course_id) [1]
* [WITHDRAWAL_REASON](#withdrawal_reason) [0..1]
* [WITHDRAWAL_DATE](#withdrawal_date) [0..1] deprecated
* [ENTRY_QUALS](#entry_quals) [0..1]
* [ENTRY_POINTS](#entry_points) [0..1]
* [COURSE_OUTCOME](#course_outcome) [0..1]
* [COURSE_GRADE](#course_grade) [0..1]
* [COURSE_AIM_ATTAINED](#course_aim_attained) [0..1]
* [COURSE_MARK](#course_mark) [0..1]
* [COURSE_EXPECTED_END_DATE](#course_expected_end_date) [0..1]
* [COURSE_END_DATE](#course_end_date) [0..1]
* [COURSE_JOIN_DATE](#course_join_date) [0..1]
* [COURSE_JOIN_AGE](#course_join_age) [0..1]
* [COHORT_ID](#cohort_id) [0..1]
* [ACTIVE_MEMBERSHIP](#active_membership) [0..1]

\* indicates that the property is part of a composite primary key for this entity.

##STUDENT_COURSE_MEMBERSHIP_ID
###Description
The institution's own unique identifier for the combination of one student and one course they are enrolled on.

###Purpose
To provide a unique course code for a student, for use in correctly mapping to module and assessment records.

###Derivation
As defined by the Student Record System.

###References

###Format
String (255)

###Notes
The student_course_membership is designed to deal with the fact that some students are enrolled on more than one course in their time at a provider. Drawing together data on their student ID alone could therefore be misleading, or at least be significantly different from students who have only ever been registered on one course. STUDENT_COURSE_MEMBERSHIP_ID partitions the study careers of those who are on multiple courses, and makes them comparable to those who have only ever been enrolled on one course.

##STUDENT_COURSE_MEMBERSHIP_SEQ
###Description
A sequence indicator that uniquely identifies the combination of the student and the course_instance they are assigned to.

###Purpose
To provide a unique course_instance code for a student, for use in joining a student to course_instance/enrolment records

###Derivation
As defined by the Student Record System.

###Valid Values
Either a letter or digit that increments for each student - course_instance pair.

###References

###Format
String (255)

###Notes
The student_course_membership sequence ID is designed to deal with the fact that some students drop out off or enroll on more than one instance of the same course. Note that the ACTIVE_MEMBERSHIP property indicates whether this student_course_membership record is the current one.


##WITHDRAWAL_REASON
###Description
The reason a student has withdrawn from a course (if they have)

###Purpose
For analytics

###Derivation
Based on the ILR codeset used for 'WithdrawReason' - with HESA code '05' utilised. For further information visit:

https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf

https://www.hesa.ac.uk/collection/c16051/a/WITHDRAWREASON

https://www.hesa.ac.uk/collection/c16051/a/RSNEND

###Valid Values & Mappings
<table>
<tr><td>WITHDRAWAL_REASON</td><td>DESCRIPTION (ENGLISH)</td><td>DESCRIPTION (WELSH)</td><td>HESA (WITHDRAWREASON)</td><td>HESA (RSNEND)</td><td>FEILR (WITHDRAWREASON)  </td></tr>
<tr><td>2</td><td>Learner has transferred to another provider</td><td></td><td>02</td><td>03</td><td>2  </td></tr>
<tr><td>3</td><td>Learner injury / illness</td><td></td><td>03</td><td>04</td><td>3   </td></tr>
<tr><td>5</td><td>Death</td><td></td><td>N/A</td><td>05</td><td>N/A  </td></tr>
<tr><td>7</td><td>Learner has transferred between providers due to intervention by the Skills Funding Agency</td><td></td><td>07</td><td>N/A</td><td>7  </td></tr>
<tr><td>10</td><td>Gone into employment</td><td></td><td>N/A</td><td>10</td><td>N/A  </td></tr>
<tr><td>28</td><td>OLASS learner withdrawn due to circumstances outside the providers’ control</td><td></td><td>N/A</td><td>N/A</td><td>28  </td></tr>
<tr><td>29</td><td>Learner has been made redundant</td><td></td><td>29</td><td>N/A</td><td>29  </td></tr>
<tr><td>40</td><td>Learner has transferred to a new learning aim with the same provider</td><td></td><td>40</td><td>N/A</td><td>40  </td></tr>
<tr><td>41</td><td>Learner has transferred to another provider to undertake learning that meets a specific government strategy</td><td></td><td>41</td><td>N/A</td><td>41  </td></tr>
<tr><td>42</td><td>Academic failure/left in bad standing/not permitted to progress – HE learning aims only</td><td></td><td>N/A</td><td>02</td><td>42  </td></tr>
<tr><td>43</td><td>Financial reasons</td><td></td><td>N/A</td><td>06</td><td>43  </td></tr>
<tr><td>44</td><td>Other personal reasons</td><td></td><td>N/A</td><td>07</td><td>44  </td></tr>
<tr><td>45</td><td>Written off after lapse of time (HE learning aims only)</td><td></td><td>N/A</td><td>08</td><td>45  </td></tr>
<tr><td>46</td><td>Exclusion</td><td></td><td>N/A</td><td>09</td><td>46  </td></tr>
<tr><td>97</td><td>Other</td><td></td><td>97</td><td>11</td><td>97  </td></tr>
<tr><td>98</td><td>Reason not known</td><td></td><td>98</td><td>99</td><td>98  </td></tr>
<tr><td>99</td><td>Completion of course - result unknown</td><td></td><td>N/A</td><td>98</td><td>N/A</td></tr>
</table>  

###Format
Int

###Notes

##WITHDRAWAL_DATE
###Description
The date a student has withdrawn from a course (if they have)

###Purpose
For analytics

###Derivation
https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf
https://www.hesa.ac.uk/collection/c16051/a/ENDDATE

###Valid Values
YYYY-MM-DD

###Format
ISO 8601 Date

###Notes
Would normally utilise ENDDATE (HE/ HESA) or potentially LearnActEndDate (FE/ ILR - to be confirmed) when relevant fields denote that the learner/ student has withdrawn from the learning aim/ course.

This property is deprecated, use student_course_membership.COURSE_END_DATE and student_course_membership.COURSE_OUTCOME instead.

##ENTRY_QUALS
###Description
The classification of entry qualifications, prior to entry to the institution

###Purpose
For display & analytics

###Derivation
Based on HESA codings for QUALENT3, but merged with specific element of the FE ILR field 'PriorAttain'

https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/518675/ILRSpecification2016_17_v2_April2016.pdf

https://www.hesa.ac.uk/collection/c16051/a/QUALENT3

###Valid Values & Mappings
<table>
<tr><td>ENTRY_QUALS</td><td>DESCRIPTION (ENGLISH)</td><td>DESCRIPTION (WELSH)</td><td>HESA(QUALENT3)</td><td>FEILR (PRIORATTAIN)</td></tr>
<tr><td>DUK</td><td>UK doctorate degree</td><td></td><td>DUK</td><td> 	</td></tr>
<tr><td>DZZ</td><td>Non-UK doctorate degree</td><td></td><td>DZZ</td><td>  	</td></tr>
<tr><td>D80</td><td>Other qualification at level D</td><td></td><td>D80</td><td>  	</td></tr>
<tr><td>MUK</td><td>UK masters degree</td><td></td><td>MUK</td><td>  	</td></tr>
<tr><td>MZZ</td><td>Non-UK masters degree</td><td></td><td>MZZ</td><td>  	</td></tr>
<tr><td>M2X</td><td>Integrated undergraduate/postgraduate taught masters degree on the enhanced/extended pattern</td><td></td><td>M2X</td><td>  	</td></tr>
<tr><td>M41</td><td>Diploma at level M</td><td></td><td>M41</td><td>  	</td></tr>
<tr><td>M44</td><td>Certificate at level M</td><td></td><td>M44</td><td>  	</td></tr>
<tr><td>M71</td><td>Postgraduate Certificate in Education or Professional Graduate Diploma in Education</td><td></td><td>M71</td><td>  	</td></tr>
<tr><td>M80</td><td>Other taught qualification at level M</td><td></td><td>M80</td><td>  	</td></tr>
<tr><td>M90</td><td>Taught work at level M for provider credit</td><td></td><td>M90</td><td>  	</td></tr>
<tr><td>M91</td><td>(Other) Qualification at level 7 or above</td><td></td><td>N/A</td><td>13  </td></tr>
<tr><td>HUK</td><td>UK first degree with honours</td><td></td><td>HUK</td><td>  	</td></tr>
<tr><td>HZZ</td><td>Non-UK first degree</td><td></td><td>HZZ</td><td>  	</td></tr>
<tr><td>H11</td><td>First degree with honours leading to Qualified Teacher Status (QTS)/registration with a General Teaching Council (GTC)</td><td></td><td>H11</td><td>  	</td></tr>
<tr><td>H71</td><td>Professional Graduate Certificate in Education</td><td></td><td>H71</td><td>  	</td></tr>
<tr><td>H80</td><td>(Other) Qualification at level H or level 6</td><td></td><td>H80</td><td>12  </td></tr>
<tr><td>JUK</td><td>UK ordinary (non-honours) first degree</td><td></td><td>JUK</td><td>  	</td></tr>
<tr><td>J10</td><td>Foundation degree</td><td></td><td>J10</td><td>  </td></tr>
<tr><td>J20</td><td>Diploma of Higher Education (DipHE)</td><td></td><td>J20</td><td>  	</td></tr>
<tr><td>J30</td><td>Higher National Diploma (HND)</td><td></td><td>J30</td><td>  	</td></tr>
<tr><td>J31</td><td>(Other) Qualification at level 5 or above (DEPRECATED SINCE 01/08/2013)</td><td></td><td>J32</td><td>5  </td></tr>
<tr><td>J49</td><td>Foundation course at level J</td><td></td><td>J49</td><td>  	</td></tr>
<tr><td>J48</td><td>Certificate in Education (CertEd) or Diploma in Education (DipEd) (i.e. non-graduate initial teacher training qualification)</td><td></td><td>J48</td><td>  	</td></tr>
<tr><td>J80</td><td>Other qualification at level J</td><td></td><td>J80</td><td>  	</td></tr>
<tr><td>C20</td><td>Certificate of Higher Education (CertHE)</td><td></td><td>C20</td><td>  	</td></tr>
<tr><td>C30</td><td>Higher National Certificate (HNC)</td><td></td><td>C30</td><td> 	</td></tr>
<tr><td>C44</td><td>Higher Apprenticeship (level 4)</td><td></td><td>C44</td><td>  	</td></tr>
<tr><td>C80</td><td>(Other) Qualification at level C or level 4</td><td></td><td>C80</td><td>4, 10  </td></tr>
<tr><td>C90</td><td>Undergraduate credits</td><td></td><td>C90</td><td>  	</td></tr>
<tr><td>P41</td><td>Diploma at level 3</td><td></td><td>P41</td><td>  	</td></tr>
<tr><td>P42</td><td>Certificate at level 3</td><td></td><td>P42</td><td>  	</td></tr>
<tr><td>P46</td><td>Award at level 3</td><td></td><td>P46</td><td>  	</td></tr>
<tr><td>P47</td><td>AQA Baccalaureate (Bacc)</td><td></td><td>P47</td><td>  	</td></tr>
<tr><td>P50</td><td>A/AS level</td><td></td><td>P50</td><td>  	</td></tr>
<tr><td>P51</td><td>14-19 Advanced Diploma (level 3)</td><td></td><td>P51</td><td>  	</td></tr>
<tr><td>P53</td><td>Scottish Baccalaureate</td><td></td><td>P53</td><td>  	</td></tr>
<tr><td>P54</td><td>Scottish Highers/Advanced Highers</td><td></td><td>P54</td><td>  	</td></tr>
<tr><td>P62</td><td>International Baccalaureate (IB) Diploma</td><td></td><td>P62</td><td>  	</td></tr>
<tr><td>P63</td><td>International Baccalaureate (IB) Certificate</td><td></td><td>P63</td><td>  	</td></tr>
<tr><td>P64</td><td>Cambridge Pre-U Diploma</td><td></td><td>P64</td><td>  	</td></tr>
<tr><td>P65</td><td>Cambridge Pre-U Certificate</td><td></td><td>P65</td><td>  	</td></tr>
<tr><td>P68</td><td>Welsh Baccalaureate Advanced Diploma (level 3)</td><td></td><td>P68</td><td>  	</td></tr>
<tr><td>P80</td><td>(Other) Qualification at level 3</td><td></td><td>P80</td><td>3  </td></tr>
<tr><td>P91</td><td>Level 3 qualifications of which some or all are subject to UCAS Tariff</td><td></td><td>P91</td><td>  	</td></tr>
<tr><td>P92</td><td>Level 3 qualifications of which none are subject to UCAS Tariff</td><td></td><td>P92</td><td>  	</td></tr>
<tr><td>P93</td><td>Level 3 qualifications of which all are subject to UCAS Tariff</td><td></td><td>P93</td><td>  	</td></tr>
<tr><td>P94</td><td>Level 3 qualifications of which some are subject to UCAS Tariff</td><td></td><td>P94</td><td>  	</td></tr>
<tr><td>Q51</td><td>14-19 Higher Diploma (level 2)</td><td></td><td>Q51</td><td>  	</td></tr>
<tr><td>Q52</td><td>Welsh Baccalaureate Intermediate Diploma (level 2)</td><td></td><td>Q52</td><td>  	</td></tr>
<tr><td>Q80</td><td>(Other) Qualification at level 2</td><td></td><td>Q80</td><td>2  </td></tr>
<tr><td>R51</td><td>14-19 Foundation Diploma (level 1)</td><td></td><td>R51</td><td>  	</td></tr>
<tr><td>R52</td><td>Welsh Baccalaureate Foundation Diploma (level 1)</td><td></td><td>R52</td><td>  	</td></tr>
<tr><td>R80</td><td>Other qualification at level 1</td><td></td><td>R80</td><td>1  </td></tr>
<tr><td>X07</td><td>(Other) Qualification below level 1</td><td></td><td>N/A</td><td>7  </td></tr>
<tr><td>X00</td><td>Higher education (HE) access course Quality Assurance Agency (QAA) recognised</td><td></td><td>X00</td><td>  	</td></tr>
<tr><td>X01</td><td>Higher education (HE) access course not Quality Assurance Agency (QAA) recognised</td><td></td><td>X01</td><td>  	</td></tr>
<tr><td>X02</td><td>Mature student admitted on basis of previous experience and/or admissions test</td><td></td><td>X02</td><td>  	</td></tr>
<tr><td>X04</td><td>Other qualification level not known</td><td></td><td>X04</td><td>97  </td></tr>
<tr><td>X05</td><td>Student has no formal qualification</td><td></td><td>X05</td><td>99  </td></tr>
<tr><td>X06</td><td>Not known</td><td></td><td>X06</td><td>98</td></tr>
</table>

###Format
Alphanumeric

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

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

###Notes


##COURSE_OUTCOME
###Description
This field indicates the outcome/ status of the learner's current course or learning aim. This is based on the information provided by HESA via the RSNEND field, however this has been adapted with the addition of fields to cater for FE (via the ILR CompStatus field), and can be used to fully cater for the outcomes in granular detail

###Purpose
For analytics

###Derivation

https://www.hesa.ac.uk/collection/c16051/a/rsnend/

https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/449779/ILRSpecification2015_16_v3_July2015.pdf

###Valid Values
 <table>
            <tr>
                <td>COURSE_OUTCOME</td>
                <td>DESCRIPTION (ENGLISH)</td>
                <td>DESCRIPTION (WELSH)</td>
                <td>HESA RSNEND code</td>
                <td>FEILR CompStatus code</td>
            </tr>
            <tr>
                <td>01</td>
                <td>Successful completion of course</td>
                <td> </td>
                <td>01</td>
                <td>2</td>
            </tr>
            <tr>
                <td>02</td>
                <td>Academic failure/left in bad standing/not permitted to
                    progress</td>
                <td> </td>
                <td>02</td>
                <td>3</td>
            </tr>
            <tr>
                <td>03</td>
                <td>Transferred to another provider</td>
                <td> </td>
                <td>03</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>04</td>
                <td>Health reasons</td>
                <td> </td>
                <td>04</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>05</td>
                <td>Death</td>
                <td> </td>
                <td>05</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>06</td>
                <td>Financial reasons</td>
                <td> </td>
                <td>06</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>07</td>
                <td>Other personal reasons &amp; dropped out</td>
                <td> </td>
                <td>07</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>08</td>
                <td>Written off after lapse of time</td>
                <td> </td>
                <td>08</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>09</td>
                <td>Exclusion</td>
                <td> </td>
                <td>09</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>10</td>
                <td>Gone into employment</td>
                <td> </td>
                <td>10</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>11</td>
                <td>Other</td>
                <td> </td>
                <td>11</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>12</td>
                <td>Transferred out as part of collaborative supervision arrangements</td>
                <td> </td>
                <td>12</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>13</td>
                <td>The learner is continuing or intending to continue the learning activities leading to the learning aim</td>
                <td> </td>
                <td>N/A</td>
                <td>1</td>
            </tr>
            <tr>
                <td>14</td>
                <td>Learner has temporarily withdrawn from the aim due to an agreed break in learning</td>
               <td> </td>
                <td>N/A</td>
                <td>6</td>
            </tr>
            <tr>
                <td>98</td>
                <td>Completion of course - result unknown</td>
                <td> </td>
                <td>98</td>
                <td>N/A</td>
            </tr>
            <tr>
                <td>99</td>
                <td>Unknown</td>
                <td> </td>
                <td>99</td>
                <td>N/A</td>
            </tr>
        </table>

###Format
Int

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

##COURSE_GRADE
###Description
Class of award achieved by the student on this course_instance. Based on HESA codeset for CLASS (HE conformity to be confirmed)

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/CLASS

###Valid Values

<table>
<tr><td>COURSE_GRADE</td><td>DESCRIPTION (ENGLISH)</td><td>DESCRIPTION (WELSH)  </td></tr>
<tr><td>1</td><td>First class honours</td><td>  	</td></tr>
<tr><td>2</td><td>Upper second class honours</td><td>  	</td></tr>
<tr><td>3</td><td>Lower second class honours</td><td> 	</td></tr>
<tr><td>4</td><td>Undivided second class honours</td><td> 	</td></tr>
<tr><td>5</td><td>Third class honours</td><td> 	</td></tr>
<tr><td>6</td><td>Fourth class honours</td><td> 	</td></tr>
<tr><td>7</td><td>Unclassified honours</td><td> 	</td></tr>
<tr><td>8</td><td>Aegrotat (whether to honours or pass)</td><td> 	</td></tr>
<tr><td>9</td><td>Pass - degree awarded without honours following an honours course</td><td> 	</td></tr>
<tr><td>10</td><td>Ordinary (to include divisions of ordinary if any) - degree awarded after following a non-honours course</td><td> 	</td></tr>
<tr><td>11</td><td>General degree - degree awarded after following a non-honours course/degree that was not available to be classified</td><td> 	</td></tr>
<tr><td>12</td><td>Distinction</td><td> 	</td></tr>
<tr><td>13</td><td>Merit</td><td> 	</td></tr>
<tr><td>14</td><td>Pass</td><td> 	</td></tr>
<tr><td>51</td><td>A FE</td><td> 	</td></tr>
<tr><td>52</td><td>B FE</td><td> 	</td></tr>
<tr><td>53</td><td>C FE</td><td> 	</td></tr>
<tr><td>54</td><td>D FE</td><td> 	</td></tr>
<tr><td>55</td><td>E FE</td><td> 	</td></tr>
<tr><td>56</td><td>F FE</td><td> 	</td></tr>
<tr><td>57</td><td>G FE</td><td> 	</td></tr>
<tr><td>61</td><td>N FE</td><td> 	</td></tr>
<tr><td>62</td><td>U FE</td><td> 	</td></tr>
<tr><td>63</td><td>X FE</td><td> 	</td></tr>
<tr><td>64</td><td>A* FE</td><td> 	</td></tr>
<tr><td>65</td><td>Y FE</td><td> 	</td></tr>
<tr><td>71</td><td>Pass FE</td><td> 	</td></tr>
<tr><td>72</td><td>Merit FE</td><td> 	</td></tr>
<tr><td>73</td><td>Distinction FE</td><td> 	</td></tr>
<tr><td>74</td><td>Fail FE</td><td> 	</td></tr>
<tr><td>81</td><td>1 FE</td><td> 	</td></tr>
<tr><td>82</td><td>2 FE</td><td> 	</td></tr>
<tr><td>83</td><td>3 FE</td><td> 	</td></tr>
<tr><td>84</td><td>4 FE</td><td> 	</td></tr>
<tr><td>85</td><td>5 FE</td><td> 	</td></tr>
<tr><td>86</td><td>6 FE</td><td> 	</td></tr>
<tr><td>87</td><td>7 FE</td><td> 	</td></tr>
<tr><td>88</td><td>8 FE</td><td> 	</td></tr>
<tr><td>89</td><td>9 FE</td><td>  </td></tr>
<tr><td>90</td><td>10 FE</td><td>  </td></tr>
<tr><td>91</td><td>Not yet awarded</td><td>  </td></tr>
</table>

###Format
Int

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.

##COURSE_AIM_ATTAINED
###Description
The Course Aim the student attained on the course of which they are a member.

###Purpose
Allowing the analysis of whether a student achieved the award/aim associated with the course of which they are a member.

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/courseaim/

###Valid Values
<table>
 <tr>
  <td>COURSE_AIM</td>
  <td>DESCRIPTION (ENGLISH)</td>
  <td>DESCRIPTION (WELSH)</td>
  <td>HESA</td>
  <td>FEILR</td>
 </tr>
 <tr>
  <td>D00</td>
  <td>Doctorate degree that meets the criteria for a research-based higher degree</td>
  <td></td>
  <td>D00</td>
  <td></td>
 </tr>
 <tr>
  <td>D01</td>
  <td>New Route PhD that meets the criteria for a research-based higher degree</td>
  <td></td>
  <td>D01</td>
  <td></td>
 </tr>
 <tr>
  <td>D90</td>
  <td>Provider credit at level D that can count towards a research-based higher degree</td>
  <td></td>
  <td>D90</td>
  <td></td>
 </tr>
 <tr>
  <td>E00</td>
  <td>Doctorate degree that does not meet the criteria for a research-based higher degree</td>
  <td></td>
  <td>E00</td>
  <td></td>
 </tr>
 <tr>
  <td>E40</td>
  <td>National Vocational Qualification (NVQ) at level E</td>
  <td></td>
  <td>E40</td>
  <td></td>
 </tr>
 <tr>
  <td>E43</td>
  <td>Highly specialist diploma from a professional body</td>
  <td></td>
  <td>E43</td>
  <td></td>
 </tr>
 <tr>
  <td>E90</td>
  <td>Advanced taught study at level E for provider credit</td>
  <td></td>
  <td>E90</td>
  <td></td>
 </tr>
 <tr>
  <td>L00</td>
  <td>Masters degree that meets the criteria for a research-based higher degree</td>
  <td></td>
  <td>L00</td>
  <td></td>
 </tr>
 <tr>
  <td>L80</td>
  <td>Other postgraduate qualification at level L that meets the criteria for a research-based higher degree</td>
  <td></td>
  <td>L80</td>
  <td></td>
 </tr>
 <tr>
  <td>L90</td>
  <td>Provider credit at level L that can count towards a research-based higher degree</td>
  <td></td>
  <td>L90</td>
  <td></td>
 </tr>
 <tr>
  <td>L91</td>
  <td>Visiting research students at levels D or L, with formal or informal credit</td>
  <td></td>
  <td>L91</td>
  <td></td>
 </tr>
 <tr>
  <td>L99</td>
  <td>Research-based higher degree where the student may ultimately study at levels D or L</td>
  <td></td>
  <td>L99</td>
  <td></td>
 </tr>
 <tr>
  <td>M00</td>
  <td>Masters degree obtained typically by a combination of coursework and thesis/dissertation, that does not meet the criteria for a research-based higher degree</td>
  <td></td>
  <td>M00</td>
  <td></td>
 </tr>
 <tr>
  <td>M01</td>
  <td>Taught masters degree designed specifically as a training in research methods and intended as a preparation for a research-based higher degree</td>
  <td></td>
  <td>M01</td>
  <td></td>
 </tr>
 <tr>
  <td>M02</td>
  <td>Masters in Teaching and Learning</td>
  <td></td>
  <td>M02</td>
  <td></td>
 </tr>
 <tr>
  <td>M10</td>
  <td>Post-experience taught masters degree</td>
  <td></td>
  <td>M10</td>
  <td></td>
 </tr>
 <tr>
  <td>M11</td>
  <td>Master of Business Administration (MBA)</td>
  <td></td>
  <td>M11</td>
  <td></td>
 </tr>
 <tr>
  <td>M16</td>
  <td>Pre-registration masters degree leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory body</td>
  <td></td>
  <td>M16</td>
  <td></td>
 </tr>
 <tr>
  <td>M22</td>
  <td>Integrated undergraduate/postgraduate taught masters degree on the enhanced/extended pattern</td>
  <td></td>
  <td>M22</td>
  <td></td>
 </tr>
 <tr>
  <td>M26</td>
  <td>Integrated undergraduate/postgraduate taught masters degree on the enhanced/extended pattern leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory body</td>
  <td></td>
  <td>M26</td>
  <td></td>
 </tr>
 <tr>
  <td>M28</td>
  <td>Integrated undergraduate/postgraduate taught masters degree on the enhanced/extended pattern leading towards registration with the Architects Registration Board (Part 1 and Part 2 qualification)</td>
  <td></td>
  <td>M28</td>
  <td></td>
 </tr>
 <tr>
  <td>M40</td>
  <td>Fellowship at level M</td>
  <td></td>
  <td>M40</td>
  <td></td>
 </tr>
 <tr>
  <td>M41</td>
  <td>Diploma at level M</td>
  <td></td>
  <td>M41</td>
  <td></td>
 </tr>
 <tr>
  <td>M42</td>
  <td>Advanced professional certificate at level M</td>
  <td></td>
  <td>M42</td>
  <td></td>
 </tr>
 <tr>
  <td>M43</td>
  <td>National Vocational Qualification (NVQ) at level M</td>
  <td></td>
  <td>M43</td>
  <td></td>
 </tr>
 <tr>
  <td>M44</td>
  <td>Certificate at level M</td>
  <td></td>
  <td>M44</td>
  <td></td>
 </tr>
 <tr>
  <td>M45</td>
  <td>Scottish Vocational Qualification (SVQ) 5</td>
  <td></td>
  <td>M45</td>
  <td></td>
 </tr>
 <tr>
  <td>M50</td>
  <td>Postgraduate bachelors degree at level M obtained typically by a combination of coursework and thesis/dissertation, that does not meet the criteria for a research-based higher degree</td>
  <td></td>
  <td>M50</td>
  <td></td>
 </tr>
 <tr>
  <td>M70</td>
  <td>Professional taught qualification at level M other than a masters degree</td>
  <td></td>
  <td>M70</td>
  <td></td>
 </tr>
 <tr>
  <td>M71</td>
  <td>Postgraduate Certificate in Education or Professional Graduate Diploma in Education</td>
  <td></td>
  <td>M71</td>
  <td></td>
 </tr>
 <tr>
  <td>M72</td>
  <td>Post-registration education qualification at level M other than a masters degree for serving schoolteachers</td>
  <td></td>
  <td>M72</td>
  <td></td>
 </tr>
 <tr>
  <td>M73</td>
  <td>Postgraduate Diploma in Education
  <td></td>
  <td>M73</td>
  <td></td>
 </tr>
 <tr>
  <td>M76</td>
  <td>Post-registration health and social care qualification at level M</td>
  <td></td>
  <td>M76</td>
  <td></td>
 </tr>
 <tr>
  <td>M78</td>
  <td>Taught qualification at level M (where qualification at level H and/or level M is a pre-requisite for course entry) leading towards registration with the Architects Registration Board (Part 3 qualification)</td>
  <td></td>
  <td>M78</td>
  <td></td>
 </tr>
 <tr>
  <td>M79</td>
  <td>Level 7 Diploma in Teaching in the Lifelong Learning Sector</td>
  <td></td>
  <td>M79</td>
  <td></td>
 </tr>
 <tr>
  <td>M80</td>
  <td>Other taught qualification at level M</td>
  <td></td>
  <td>M80</td>
  <td></td>
 </tr>
 <tr>
  <td>M86</td>
  <td>Taught qualification at level M leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory body</td>
  <td></td>
  <td>M86</td>
  <td></td>
 </tr>
 <tr>
  <td>M88</td>
  <td>Taught qualification at level M (where a qualification at level H is a pre-requisite for course entry) leading towards registration with the Architects Registration Board (Part 2 qualification)</td>
  <td></td>
  <td>M88</td>
  <td></td>
 </tr>
 <tr>
  <td>M90</td>
  <td>Taught work at level M for provider credit</td>
  <td></td>
  <td>M90</td>
  <td></td>
 </tr>
 <tr>
  <td>M91</td>
  <td>Visiting taught students at levels E or M, with formal or informal credit</td>
  <td></td>
  <td>M91</td>
  <td></td>
 </tr>
 <tr>
  <td>M99</td>
  <td>Taught work at levels E or M with an unspecified qualification aim</td>
  <td></td>
  <td>M99</td>
  <td></td>
 </tr>
 <tr>
  <td>H00</td>
  <td>First degree with honours</td>
  <td></td>
  <td>H00</td>
  <td></td>
 </tr>
 <tr>
  <td>H11</td>
  <td>First degree with honours leading to Qualified Teacher Status (QTS)/registration with a General Teaching Council (GTC)</td>
  <td></td>
  <td>H11</td>
  <td></td>
 </tr>
 <tr>
  <td>H12</td>
  <td>First degree with honours leading to Early Years Teacher Status (EYTS)</td>
  <td></td>
  <td>H12</td>
  <td></td>
 </tr>
 <tr>
  <td>H16</td>
  <td>Pre-registration first degree with honours leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory body</td>
  <td></td>
  <td>H16</td>
  <td></td>
 </tr>
 <tr>
  <td>H18</td>
  <td>First degree with honours leading towards registration with the Architects Registration Board (Part 1 qualification)</td>
  <td></td>
  <td>H18</td>
  <td></td>
 </tr>
 <tr>
  <td>H22</td>
  <td>First degree with honours on the enhanced/extended pattern but at level H</td>
  <td></td>
  <td>H22</td>
  <td></td>
 </tr>
 <tr>
  <td>H23</td>
  <td>First degree with honours and diploma</td>
  <td></td>
  <td>H23</td>
  <td></td>
 </tr>
 <tr>
  <td>H41</td>
  <td>Diploma at level H</td>
  <td></td>
  <td>H41</td>
  <td></td>
 </tr>
 <tr>
  <td>H42</td>
  <td>Certificate at level H</td>
  <td></td>
  <td>H42</td>
  <td></td>
 </tr>
 <tr>
  <td>H43</td>
  <td>National Vocational Qualification (NVQ) at level H</td>
  <td></td>
  <td>H43</td>
  <td></td>
 </tr>
 <tr>
  <td>H50</td>
  <td>Postgraduate bachelors degree at level H</td>
  <td></td>
  <td>H50</td>
  <td></td>
 </tr>
 <tr>
  <td>H60</td>
  <td>Graduate diploma/certificate at level H</td>
  <td></td>
  <td>H60</td>
  <td></td>
 </tr>
 <tr>
  <td>H61</td>
  <td>Graduate diploma/certificate at level H but where a previous qualification at level H is a pre-requisite for course entry</td>
  <td></td>
  <td>H61</td>
  <td></td>
 </tr>
 <tr>
  <td>H62</td>
  <td>Pre-registration graduate diploma/certificate leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory
body</td>
  <td></td>
  <td>H62</td>
  <td></td>
 </tr>
 <tr>
  <td>H70</td>
  <td>Professional qualification at level H other than a first degree with honours</td>
  <td></td>
  <td>H70</td>
  <td></td>
 </tr>
 <tr>
  <td>H71</td>
  <td>Professional Graduate Certificate in Education</td>
  <td></td>
  <td>H71</td>
  <td></td>
 </tr>
 <tr>
  <td>H72</td>
  <td>Professional qualification at level H for serving schoolteachers other than a first degree with honours</td>
  <td></td>
  <td>H72</td>
  <td></td>
 </tr>
 <tr>
  <td>H76</td>
  <td>Post-registration health and social care qualification at level H other than a first degree with honours</td>
  <td></td>
  <td>H76</td>
  <td></td>
 </tr>
 <tr>
  <td>H78</td>
  <td>Other qualification at level H (where other qualifications at level H are a pre-requisite for course entry) leading towards registration with the Architects Registration Board (Part 3 qualification)</td>
  <td></td>
  <td>H78</td>
  <td></td>
 </tr>
 <tr>
  <td>H79</td>
  <td>Level 6 Diploma in Teaching in the Lifelong Learning Sector</td>
  <td></td>
  <td>H79</td>
  <td></td>
 </tr>
 <tr>
  <td>H80</td>
  <td>Other qualification at level H</td>
  <td></td>
  <td>H80</td>
  <td></td>
 </tr>
 <tr>
  <td>H81</td>
  <td>Other qualification at level H but where a previous qualification at level H is a pre-requisite for course entry</td>
  <td></td>
  <td>H81</td>
  <td></td>
 </tr>
 <tr>
  <td>H88</td>
  <td>Qualification at level H (where another qualification at level H is a pre-requisite for course entry) leading towards registration with the Architects Registration Board (Part 2 qualification)</td>
  <td></td>
  <td>H88</td>
  <td></td>
 </tr>
 <tr>
  <td>H90</td>
  <td>Credits at level H</td>
  <td></td>
  <td>H90</td>
  <td></td>
 </tr>
 <tr>
  <td>H91</td>
  <td>Visiting students at level H, with formal or informal credit</td>
  <td></td>
  <td>H91</td>
  <td></td>
 </tr>
 <tr>
  <td>H99</td>
  <td>Taught work at level H with an unspecified qualification aim</td>
  <td></td>
  <td>H99</td>
  <td></td>
 </tr>
 <tr>
  <td>I00</td>
  <td>Ordinary (non-honours) first degree</td>
  <td></td>
  <td>I00</td>
  <td></td>
 </tr>
 <tr>
  <td>I11</td>
  <td>Ordinary (non-honours) first degree leading to Qualified Teacher Status (QTS)/registration with a General Teaching Council (GTC)</td>
  <td></td>
  <td>I11</td>
  <td></td>
 </tr>
 <tr>
  <td>I12</td>
  <td>Ordinary (non-honours) first degree leading to Early Years Teacher Status (EYTS)</td>
  <td></td>
  <td>I12</td>
  <td></td>
 </tr>
 <tr>
  <td>I16</td>
  <td>Pre-registration ordinary (non-honours) first degree leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory body</td>
  <td></td>
  <td>I16</td>
  <td></td>
 </tr>
 <tr>
  <td>I60</td>
  <td>Graduate diploma/certificate at level I</td>
  <td></td>
  <td>I60</td>
  <td></td>
 </tr>
 <tr>
  <td>I61</td>
  <td>Graduate diploma/certificate at level I but where a previous qualification at level I or H is a pre-requisite for course entry</td>
  <td></td>
  <td>I61</td>
  <td></td>
 </tr>
 <tr>
  <td>I70</td>
  <td>Professional qualification at level I other than an ordinary (non-honours) first degree</td>
  <td></td>
  <td>I70</td>
  <td></td>
 </tr>
 <tr>
  <td>I71</td>
  <td>Qualified Teacher Status (QTS)/registration with a General Teaching Council (GTC) only</td>
  <td></td>
  <td>I71</td>
  <td></td>
 </tr>
 <tr>
  <td>I72</td>
  <td>Professional qualification at level I for serving schoolteachers</td>
  <td></td>
  <td>I72</td>
  <td></td>
 </tr>
 <tr>
  <td>I73</td>
  <td>Early Years Teacher Status (EYTS) only</td>
  <td></td>
  <td>I73</td>
  <td></td>
 </tr>
 <tr>
  <td>I74</td>
  <td>Teaching certificate (trained through the medium of Welsh)</td>
  <td></td>
  <td>I74</td>
  <td></td>
 </tr>
 <tr>
  <td>I76</td>
  <td>Post-registration health and social care qualification at level I other than an ordinary (non-honours) first degree</td>
  <td></td>
  <td>I76</td>
  <td></td>
 </tr>
 <tr>
  <td>I79</td>
  <td>Level 5 Diploma in Teaching in the Lifelong Learning Sector</td>
  <td></td>
  <td>I79</td>
  <td></td>
 </tr>
 <tr>
  <td>I80</td>
  <td>Other qualification at level I</td>
  <td></td>
  <td>I80</td>
  <td></td>
 </tr>
 <tr>
  <td>I81</td>
  <td>Other qualification at level I but where a previous qualification at level I or H is a pre-requisite for course entry</td>
  <td></td>
  <td>I81</td>
  <td></td>
 </tr>
 <tr>
  <td>I90</td>
  <td>Credits at level I</td>
  <td></td>
  <td>I90</td>
  <td></td>
 </tr>
 <tr>
  <td>I91</td>
  <td>Visiting students at level I, with formal or informal credit</td>
  <td></td>
  <td>I91</td>
  <td></td>
 </tr>
 <tr>
  <td>I99</td>
  <td>Taught work at level I with an unspecified qualification  aim</td>
  <td></td>
  <td>I99</td>
  <td></td>
 </tr>
 <tr>
  <td>J10</td>
  <td>Foundation degree</td>
  <td></td>
  <td>J10</td>
  <td></td>
 </tr>
 <tr>
  <td>J16</td>
  <td>Foundation degree which on completion meets entry  requirement for pre-registration health and social care qualification</td>
  <td></td>
  <td>J16</td>
  <td></td>
 </tr>
 <tr>
  <td>J20</td>
  <td>Diploma of Higher Education (DipHE)</td>
  <td></td>
  <td>J20</td>
  <td></td>
 </tr>
 <tr>
  <td>J26</td>
  <td>Diploma of Higher Education (DipHE) leading towards obtaining eligibility to register to practice with a health or social care or veterinary statutory regulatory body</td>
  <td></td>
  <td>J26</td>
  <td></td>
 </tr>
 <tr>
  <td>J30</td>
  <td>Higher National Diploma (HND)</td>
  <td></td>
  <td>J30</td>
  <td></td>
 </tr>
 <tr>
  <td>J41</td>
  <td>Diploma at level J</td>
  <td></td>
  <td>J41</td>
  <td></td>
 </tr>
 <tr>
  <td>J42</td>
  <td>Certificate at level J</td>
  <td></td>
  <td>J42</td>
  <td></td>
 </tr>
 <tr>
  <td>J43</td>
  <td>National Vocational Qualification (NVQ) at level J</td>
  <td></td>
  <td>J43</td>
  <td></td>
 </tr>
 <tr>
  <td>J45</td>
  <td>Scottish Vocational Qualification (SVQ) 4</td>
  <td></td>
  <td>J45</td>
  <td></td>
 </tr>
 <tr>
  <td>J76</td>
  <td>Post-registration health and social care qualification at level J</td>
  <td></td>
  <td>J76</td>
  <td></td>
 </tr>
 <tr>
  <td>J80</td>
  <td>Other qualification at level J</td>
  <td></td>
  <td>J80</td>
  <td></td>
 </tr>
 <tr>
  <td>J90</td>
  <td>Credits at level J</td>
  <td></td>
  <td>J90</td>
  <td></td>
 </tr>
 <tr>
  <td>J99</td>
  <td>Taught work at level J with an unspecified qualification aim</td>
  <td></td>
  <td>J99</td>
  <td></td>
 </tr>
 <tr>
  <td>C20</td>
  <td>Certificate of Higher Education (CertHE)</td>
  <td></td>
  <td>C20</td>
  <td></td>
 </tr>
 <tr>
  <td>C30</td>
  <td>Higher National Certificate (HNC)</td>
  <td></td>
  <td>C30</td>
  <td></td>
 </tr>
 <tr>
  <td>C41</td>
  <td>Diploma at level C</td>
  <td></td>
  <td>C41</td>
  <td></td>
 </tr>
 <tr>
  <td>C42</td>
  <td>Certificate at level C</td>
  <td></td>
  <td>C42</td>
  <td></td>
 </tr>
 <tr>
  <td>C43</td>
  <td>National Vocational Qualification (NVQ) at level C</td>
  <td></td>
  <td>C43</td>
  <td></td>
 </tr>
 <tr>
  <td>C77</td>
  <td>Level 4 Preparing to Teach in the Lifelong Learning Sector</td>
  <td></td>
  <td>C77</td>
  <td></td>
 </tr>
 <tr>
  <td>C78</td>
  <td>Level 4 Certificate in Teaching in the Lifelong Learning Sector</td>
  <td></td>
  <td>C78</td>
  <td></td>
 </tr>
 <tr>
  <td>C80</td>
  <td>Other qualification at level C</td>
  <td></td>
  <td>C80</td>
  <td></td>
 </tr>
 <tr>
  <td>C90</td>
  <td>Credits at level C</td>
  <td></td>
  <td>C90</td>
  <td></td>
 </tr>
 <tr>
  <td>C99</td>
  <td>Taught work at level C with an unspecified qualification aim</td>
  <td></td>
  <td>C99</td>
  <td></td>
 </tr>
 <tr>
  <td>P41</td>
  <td>Diploma at level P</td>
  <td></td>
  <td>P41</td>
  <td></td>
 </tr>
 <tr>
  <td>P42</td>
  <td>Certificate at level P</td>
  <td></td>
  <td>P42</td>
  <td></td>
 </tr>
 <tr>
  <td>P43</td>
  <td>National Vocational Qualification (NVQ) 3</td>
  <td></td>
  <td>P43</td>
  <td></td>
 </tr>
 <tr>
  <td>P45</td>
  <td>Scottish Vocational Qualification (SVQ) 3</td>
  <td></td>
  <td>P45</td>
  <td></td>
 </tr>
 <tr>
  <td>P50</td>
  <td>A/AS level</td>
  <td></td>
  <td>P50</td>
  <td></td>
 </tr>
 <tr>
  <td>P55</td>
  <td>Advanced Higher (Scotland)</td>
  <td></td>
  <td>P55</td>
  <td></td>
 </tr>
 <tr>
  <td>P56</td>
  <td>Higher (Scotland)</td>
  <td></td>
  <td>P56</td>
  <td></td>
 </tr>
 <tr>
  <td>P70</td>
  <td>Professional qualification at level 3</td>
  <td></td>
  <td>P70</td>
  <td></td>
 </tr>
 <tr>
  <td>P77</td>
  <td>Level 3 Preparing to Teach in the Lifelong Learning Sector</td>
  <td></td>
  <td>P77</td>
  <td></td>
 </tr>
 <tr>
  <td>P78</td>
  <td>Level 3 Certificate in Teaching in the Lifelong Learning Sector</td>
  <td></td>
  <td>P78</td>
  <td></td>
 </tr>
 <tr>
  <td>P80</td>
  <td>Other qualification at level 3</td>
  <td></td>
  <td>P80</td>
  <td></td>
 </tr>
 <tr>
  <td>P85</td>
  <td>Diploma in Foundation Studies (Art and Design) at level 3</td>
  <td></td>
  <td>P85</td>
  <td></td>
 </tr>
 <tr>
  <td>P90</td>
  <td>Credits at level 3</td>
  <td></td>
  <td>P90</td>
  <td></td>
 </tr>
 <tr>
  <td>Q41</td>
  <td>Diploma at level Q</td>
  <td></td>
  <td>Q41</td>
  <td></td>
 </tr>
 <tr>
  <td>Q42</td>
  <td>Certificate at level Q</td>
  <td></td>
  <td>Q42</td>
  <td></td>
 </tr>
 <tr>
  <td>Q43</td>
  <td>National Vocational Qualification (NVQ) 2</td>
  <td></td>
  <td>Q43</td>
  <td></td>
 </tr>
 <tr>
  <td>Q45</td>
  <td>Scottish Vocational Qualification (SVQ) 2</td>
  <td></td>
  <td>Q45</td>
  <td></td>
 </tr>
 <tr>
  <td>Q50</td>
  <td>GCSE at grade A*-C</td>
  <td></td>
  <td>Q50</td>
  <td></td>
 </tr>
 <tr>
  <td>Q56</td>
  <td>Intermediate 2 (Scotland)</td>
  <td></td>
  <td>Q56</td>
  <td></td>
 </tr>
 <tr>
  <td>Q57</td>
  <td>Standard Grade Credit (Scotland)</td>
  <td></td>
  <td>Q57</td>
  <td></td>
 </tr>
 <tr>
  <td>Q70</td>
  <td>Professional qualification at level 2</td>
  <td></td>
  <td>Q70</td>
  <td></td>
 </tr>
 <tr>
  <td>Q80</td>
  <td>Other qualification at level 2</td>
  <td></td>
  <td>Q80</td>
  <td></td>
 </tr>
 <tr>
  <td>Q90</td>
  <td>Credits at level 2</td>
  <td></td>
  <td>Q90</td>
  <td></td>
 </tr>
 <tr>
  <td>R42</td>
  <td>Certificate at level R</td>
  <td></td>
  <td>R42</td>
  <td></td>
 </tr>
 <tr>
  <td>R43</td>
  <td>National Vocational Qualification (NVQ) 1</td>
  <td></td>
  <td>R43</td>
  <td></td>
 </tr>
 <tr>
  <td>R45</td>
  <td>Scottish Vocational Qualification (SVQ) 1</td>
  <td></td>
  <td>R45</td>
  <td></td>
 </tr>
 <tr>
  <td>R50</td>
  <td>GCSE at grade D-G</td>
  <td></td>
  <td>R50</td>
  <td></td>
 </tr>
 <tr>
  <td>R56</td>
  <td>Intermediate 1 (Scotland)</td>
  <td></td>
  <td>R56</td>
  <td></td>
 </tr>
 <tr>
  <td>R57</td>
  <td>Standard Grade General (Scotland)</td>
  <td></td>
  <td>R57</td>
  <td></td>
 </tr>
 <tr>
  <td>R70</td>
  <td>Professional qualification at level 1</td>
  <td></td>
  <td>R70</td>
  <td></td>
 </tr>
 <tr>
  <td>R80</td>
  <td>Other qualification at level 1</td>
  <td></td>
  <td>R80</td>
  <td></td>
 </tr>
 <tr>
  <td>R90</td>
  <td>Credits at level 1</td>
  <td></td>
  <td>R90</td>
  <td></td>
 </tr>
 <tr>
  <td>S42</td>
  <td>National Vocational Qualification (NVQ) Entry level certificate</td>
  <td></td>
  <td>S42</td>
  <td></td>
 </tr>
 <tr>
  <td>S57</td>
  <td>Standard Grade Foundation (Scotland)</td>
  <td></td>
  <td>S57</td>
  <td></td>
 </tr>
 <tr>
  <td>S80</td>
  <td>Other qualification at further education (FE) access level</td>
  <td></td>
  <td>S80</td>
  <td></td>
 </tr>
 <tr>
  <td>S90</td>
  <td>Credits at further education (FE) access level</td>
  <td></td>
  <td>S90</td>
  <td></td>
 </tr>
 <tr>
  <td>X00</td>
  <td>Higher education (HE) access course, Quality Assurance Agency (QAA) recognised</td>
  <td></td>
  <td>X00</td>
  <td></td>
 </tr>
 <tr>
  <td>X01</td>
  <td>Higher education (HE) access course, not Quality Assurance Agency (QAA) recognised</td>
  <td></td>
  <td>X01</td>
  <td></td>
 </tr>
 <tr>
  <td>X41</td>
  <td>Welsh for Adults Entry level</td>
  <td></td>
  <td>X41</td>
  <td></td>
 </tr>
 <tr>
  <td>X42</td>
  <td>Welsh for Adults level 1</td>
  <td></td>
  <td>X42</td>
  <td></td>
 </tr>
 <tr>
  <td>X43</td>
  <td>Welsh for Adults level 2</td>
  <td></td>
  <td>X43</td>
  <td></td>
 </tr>
 <tr>
  <td>X44</td>
  <td>Welsh for Adults level 3</td>
  <td></td>
  <td>X44</td>
  <td></td>
 </tr>
 <tr>
  <td>X45</td>
  <td>Welsh for Adults level 4</td>
  <td></td>
  <td>X45</td>
  <td></td>
 </tr>
 <tr>
  <td>X46</td>
  <td>Welsh for Adults specialist/arbennig</td>
  <td></td>
  <td>X46</td>
  <td></td>
 </tr>
 <tr>
  <td>X98</td>
  <td>No formal qualification aim, below FE level</td>
  <td></td>
  <td>N/A</td>
  <td></td>
 </tr>
 <tr>
  <td>X99</td>
  <td>No formal qualification aim, below HE level</td>
  <td></td>
  <td>X99</td>
  <td></td>
 </tr>
  <tr>
  <td>Z99</td>
  <td>Course aim does not apply</td>
  <td></td>
  <td>Z99</td>
  <td></td>
 </tr>
</table>

###References

###Format
String(255)

###Notes
All course levels are denoted here (TBC with FE college, for final implementation). Specific use of the LARS codeset for FE (from ILR) may need to be considered, or a mapping/ amalgamation with the HESA codeset. This is to be discussed in consultation with the FE sector.


##COURSE_MARK
###Description
The overall mark a student attained on their course.

###Purpose
For display purposes and further analysis

###Derivation
SRS Systems

###Valid values
0-100

###References

###Format
Decimal (IEEE 754)

###Notes


##COURSE_EXPECTED_END_DATE
###Description
The end date the student was expected to complete a course when they enrolled. This will be used to identify students who extend beyond this date.

###Purpose
Analytics and display

###Derivation
Jisc

###Valid values
YYYY-MM-DD

###References

###Format
ISO 8601

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

##COURSE_END_DATE
###Description
The date on which the student left their course.

###Purpose
Analytics and display

###Derivation
Jisc

###Valid values
YYYY-MM-DD

###References

###Format
ISO 8601

###Notes
Note that there may be many reasons why a student leaves a course. This is recorded in WITHDRAWAL_REASON.

##COURSE_JOIN_DATE
###Description
This field indicates the date of the student's initial commencement of studies for this student_course_membership and may relate to a date prior to the current academic/financial year. Exchange-in students should have the date they commenced their studies at the reporting provider.

###Purpose
Analytics

###Derivation
HESA COMDATE
https://www.hesa.ac.uk/collection/c16051/a/COMDATE

###Valid values
YYYY-MM-DD

###References

###Format
ISO 8601

###Notes


##COURSE_JOIN_AGE
###Description
The age of the student when they initially commenced their studies for this student_course_membership. Exchange-in students should have the age they commenced their studies at the reporting provider.

###Purpose
Analytics

###Derivation
Jisc

###Valid values
0-200

###References

###Format
Int

###Notes
This value is designed to be a secondary source to check COURSE_JOIN_DATE minus DOB. In cases where COURSE_JOIN_AGE is not stored separately, it should be calculated at the ETL stage.


##COHORT_ID
###Description
An identifier for a group of students in a year cohort.

###Purpose
Display and grouping purposes, and but analysis.

###Derivation
Jisc

###Valid values
Any

###References

###Format
String (255)

###Notes


##COHORT_ID
###Description
An identifier for a group of students in a year cohort.

###Purpose
Display and grouping purposes, and but analysis.

###Derivation
Jisc

###Valid values
Any

###References

###Format
String (255)

###Notes


##ACTIVE_MEMBERSHIP
###Description
Indicates whether the student_course_membership record of which this property is a part is the current student course membership.

###Purpose
Display purposes.

###Derivation
Jisc

###Valid values
 <table>
            <tr>
                <td>ACTIVE_MEMBERSHIP</td>
                <td>DESCRIPTION (ENGLISH)</td>
                <td>DESCRIPTION (WELSH)</td>
            </tr>
            <tr>
                <td>1</td>
                <td>current</td>
                <td> </td>
            </tr>
            <tr>
                <td>2</td>
                <td>not current</td>
                <td> </td>
            </tr>
            <tr>
                <td>3</td>
                <td>unknown</td>
                <td> </td>
            </tr>
        </table>

###References

###Format
String (1)

###Notes
The student_course_membership record with ACTIVE_MEMBERSHIP=1 also needs to have a STUDENT_COURSE_MEMBERSHIP_SEQ of the highest sequential value of all student_course_membership records with the same STUDENT_ID + STUDENT_COURSE_MEMBERSHIP_ID combination. This record will generally also be the record with the most recent COURSE_JOIN_DATE. This attribute will be compulsory in UDD v1.3.
#Student on a module Instance
* [STUDENT_ID](student.md#student_id)
* [COURSE_INSTANCE_ID](course_instance.md#course_instance_id)
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id)
* [MOD_OUTCOME](#mod_outcome)
* [MOD_GRADE](#mod_grade)
* [MOD_PASS](#mod_pass)
* [MOD_RETAKE](#mod_retake)

##MOD_OUTCOME
###Description
This field records if the student completed the module and if so whether they gained credit or not. There should be a Module Outcome field for each module taken by the student.

###Purpose
Analytics 

###Derivation
https://www.hesa.ac.uk/index.php?option=com_studrec&task=show_file&mnl=14051&href=a^_^MODOUT.html

###Valid Values

<table>
<tr><td>CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Completion - gained full credit</td><td> 	</td></tr>
<tr><td>2</td><td>Completion - did not gain credit</td><td> 	</td></tr>
<tr><td>3</td><td>Partial completion (HEFCW HESES Rules)</td><td> 	</td></tr>
<tr><td>4</td><td>Student did not complete module</td><td> 	</td></tr>
<tr><td>5</td><td>Module taken on a not-for-credit basis</td><td> 	</td></tr>
<tr><td>6</td><td>Module outcome not yet known</td><td> 	</td></tr>
<tr><td>7</td><td>Not coded</td><td> 	</td></tr>
<tr><td>9</td><td>Module previously returned in error</td><td> 	</td></tr>
<tr><td>A</td><td>Student did not complete module - gained credit</td><td> 	</td></tr>
<tr><td>B</td><td>Student did not complete module - deferral</td><td> 	</td></tr>
<tr><td>C</td><td>Completion - award of credit not known</td><td></td></tr>
</table> 	

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
Indicates whether the student passed the module, didn't pass the module, or whether this information is not known because the module hasn't been completed yet.

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values

<table>
<tr><td>CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>2</td><td>No</td><td>Na  </td></tr>
<tr><td>3</td><td>Not completed yet</td><td>Dim wedi cwblhau</td></tr>
</table>  

###Format
Int

###Compulsory
Yes

###Notes
Code 3 is applied in all cases where the outcome is either not known (yet), or doesn't apply; because a student withdrew or deferred, for example. The value can be calculated and derived from MOD_OUTCOME if required. Note that MOD_OUTCOME has a richer vocabulary for indicating the completion statuses of modules.

##MOD_RETAKE
###Description.
Whether this is a retake of the module for that student.

###Purpose
Analytics 

###Derivation
Jisc

###Valid Values

<table>
<tr><td>    CODE</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>    1</td><td>Yes</td><td>Ie  </td></tr>
<tr><td>    2</td><td>No</td><td>Na</td></tr>
</table>  

###Format
Int

###Compulsory
No

###Notes

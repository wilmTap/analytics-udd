#Module
* [MOD_ID](#mod_id) [1] *
* [MOD_NAME](#mod_name) [0..1]
* [MOD_SUBJECT](#mod_subject) [0..1]
* [MOD_CREDITS](#mod_credits) [0..1]
* [MOD_LEVEL](#mod_level) [0..1]

\* indicates that the property is the primary key for this entity.

##MOD_ID
###Description
The unique identifier standard across SRS and LMS for the course.

###Purpose
For analytics and to link module to module_instance

Derivation
https://www.hesa.ac.uk/collection/c16051/a/module_modid/

###Valid Values
Any

###Format
String (255)

###Notes


##MOD_NAME
###Description
The actual name of the module

###Purpose
For display purposes.

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/MTITLE

###Valid Values
Any

###Format
String (255)

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.

##MOD_SUBJECT
###Description
Module subject - coded using JACS3 subject codes

###Purpose
For display purposes and analytics.

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/modsbj/

https://www.hesa.ac.uk/support/documentation/jacs

###Valid Values
[JACS3 CSV](../media/jacs3-valid-entries.csv)

###Format
String (255)

###Notes
For FE purposes, it will need be adapted to work with institutions specific codeset for Learning Activities. Details to be confirmed.
Omitting this property may hinder the development or use of an effective analytics model.


##MOD_CREDITS
###Description
Number of credits award for the module

###Purpose
For analytics

###Derivation
https://www.hesa.ac.uk/collection/c16051/a/CRDTPTS

###Valid Values
Any

###Format
Int

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

##MOD_LEVEL
###Description
Level of credit points - indicates the level of module the student is studying. This has been initially based on the HESA field LEVELPTS, however may be utilised and adapted to also cater for FE

###Purpose
Analytics

###Derivation
Jisc

###Valid Values

<table>
<tr><td>MOD_LEVEL</td><td>DESCRIPTION(ENGLISH)</td><td>DESCRIPTION(WELSH)  </td></tr>
<tr><td>0</td><td>Entry level</td><td>  </td></tr>
<tr><td>1</td><td>HE Certificate/NVQ Level 4 or equivalent</td><td> 	</td></tr>
<tr><td>2</td><td>HE Intermediate</td><td> 	</td></tr>
<tr><td>3</td><td>HE Honours</td><td> 	</td></tr>
<tr><td>5</td><td>Undergraduate unspecified</td><td> 	</td></tr>
<tr><td>6</td><td>HE Masters</td><td> 	</td></tr>
<tr><td>7</td><td>HE Doctorate</td><td> 	</td></tr>
<tr><td>9</td><td>Not applicable</td><td> 	</td></tr>
<tr><td>A</td><td>NVQ level 1 or equivalent</td><td> 	</td></tr>
<tr><td>B</td><td>NVQ level 2 or equivalent</td><td> 	</td></tr>
<tr><td>C</td><td>NVQ level 3 or equivalent</td><td> 	</td></tr>
<tr><td>D</td><td>HND/Diploma HE</td><td> 	</td></tr>
<tr><td>E</td><td>Ordinary degrees</td><td></td></tr>
</table> 	

###Format
String(1)

###Notes

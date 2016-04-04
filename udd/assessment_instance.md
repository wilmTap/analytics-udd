#Assessment instance
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id)
* [ASSESS_INSTANCE_ID](#assess_instance_id)
* [ASSESS_TYPE_ID](#assess_type_id)
* [ASSESS_TYPE_NAME](#assess_type_name)
* [ASSESS_DETAIL](#assess_detail)
* [ASSESS_WEIGHT](#assess_weight)
###Description
An assessment instance is any assessed learning activity that is part of a wider module or course that gets a grade and/or mark. The assumption is that an assessment instance is summative.

##ASSESS_INSTANCE_ID
###Description.
An institution's unique identifier for an assessment instance

###Purpose
To uniquely identify an assessment instance, and to link it to other entities such as module instances.

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes


##ASSESS_TYPE_ID
###Description.
An institution's unique identifier for the type of assessment as defined in their student record system (e.g. CW for Coursework)

###Purpose
To provide information about the type of assessment.

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes


##ASSESS_TYPE_NAME
###Description.
An institution's description for the type of assessment as defined in their student record system (e.g. Coursework).

###Purpose
To provide information about the type of assessment.

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes


##ASSESS_DETAIL
###Description.
A textual description of the assessment component and type. For example "Lab Report (1000 words)"

###Purpose
To provide information about the type of assessment.

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

###Compulsory
Yes (if applicable)

###Notes

##ASSESS_WEIGHT
###Description.
The weighting percentage that the assessment component counts towards the module mark.

###Purpose
To provide information about the type of assessment.

###Derivation
Jisc

###Valid Values
0-100

###Format
Decimal

###Compulsory
Yes (if applicable)

###Notes
#assessment_instance
* [MOD_INSTANCE_ID](module_instance.md#mod_instance_id) [1]
* [ASSESS_INSTANCE_ID](#assess_instance_id) [1]
* [ASSESS_TYPE_ID](#assess_type_id) [0..1]
* [ASSESS_TYPE_NAME](#assess_type_name) [0..1]
* [ASSESS_DETAIL](#assess_detail) [0..1]
* [ASSESS_WEIGHT](#assess_weight) [0..1]
* [MAX_MARKS](#max_marks) [0..1]

###Description
An assessment_instance is any assessed learning activity that is part of a wider module or course that gets a grade and/or mark. The assumption is that an assessment_instance is summative.

##ASSESS_INSTANCE_ID
###Description.
An institution's unique identifier for an assessment_instance

###Purpose
To uniquely identify an assessment_instance, and to link it to other entities such as module instances.

###Derivation
Jisc

###Valid Values
Any

###Format
String (255)

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

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

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

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.

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

###Notes
Omitting this property could impair the functionality of analytics applications such as student apps or dashboards.

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

###Notes
Omitting this property may hinder the development or use of an effective analytics model.

##MAX_MARKS
###Description.
The maximum numeric marks that an instructor can allocate to an assessment. Used to indicate the marking scale used for an assignment.

###Purpose
To enable student performance calculations.

###Derivation
Jisc

###Valid Values
Any

###Format
Decimal

###Notes
There is also the similar MAX_POINTS property on student_on_assessment_instance, which is for informational purposes. It has more a permissive format and value space.
# module_VLE_map
This entity connects a course area in a VLE or LMS with a module.

*  [MOD_INSTANCE_ID](module_instance.md#mod_instance_id) [1]
*  [VLE_MOD_ID](#vle_mod_id) [1]

Foreign key: ('MOD_INSTANCE_ID', 'VLE_MOD_ID')

##VLE_MOD_ID
###Description
An unique identifier for a course area in the VLE. 

###Purpose
Display in student app and staff dashboard

###Derivation
Jisc

###Valid values
Any

###References

###Format
String(255)

###Notes
The VLE course area may or may not correspond to one module.

#A guide to mandatory properties in the UDD

Because many different organisations use UDD data for many different purposes, it is not possible to be categorical about which properties have to be present in UDD compliant data that is submitted to the Jisc learning analytics Learning Record Warehouse (LRW). For example, there are some properties that are required for the LRW and other applications to function because they link different data entities, just as there are properties such as course titles that are needed just to provide labels in applications. Other properties such as marks are vitally important for practically all learning analysis, but may only be available at certain points in time.

For that reason, the UDD includes five categories of property, each of which need consideration when deciding which data to include when submitting to the LRW.

##Category 1 
These properties are required for the data in the learning record warehouse to function. They are mostly identifiers that allow different entities to be linked to each other. Each data record will have to have these properties.

- [course.COURSE_ID](udd/course.md#COURSE_ID)
- [course_instance.COURSE_ID](udd/course_instance.md#COURSE_ID)
- [course_instance.COURSE_INSTANCE_ID](udd/course_instance.md#COURSE_INSTANCE_ID)
- [institution.TENANT_ID](udd/institution.md#TENANT_ID)
- [module.MOD_ID](udd/module.md#MOD_ID)
- [module_instance.MOD_INSTANCE_ID](udd/module_instance.md#MOD_INSTANCE_ID)
- [module_instance.MOD_ID](udd/module_instance.md#MOD_ID)
- [student.STUDENT_ID](udd/student.md#STUDENT_ID)
- [student_course_membership.STUDENT_ID](udd/student_course_membership.md#STUDENT_ID)
- [student_course_membership.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_course_membership.md#STUDENT_COURSE_MEMBERSHIP_ID)
- [student_course_membership.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_course_membership.md#STUDENT_COURSE_MEMBERSHIP_SEQ)
- [student_course_membership.COURSE_ID](udd/student_course_membership.md#COURSE_ID)
- [student_on_a_module_instance.STUDENT_ID](udd/student_on_a_module_instance.md#STUDENT_ID)
- [student_on_a_module_instance.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_on_a_module_instance.md#STUDENT_COURSE_MEMBERSHIP_ID)
- [student_on_a_module_instance.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_on_a_module_instance.md#STUDENT_COURSE_MEMBERSHIP_SEQ)
- [student_on_a_module_instance.COURSE_INSTANCE_ID](udd/student_on_a_module_instance.md#COURSE_INSTANCE_ID)
- [student_on_a_module_instance.MOD_INSTANCE_ID](udd/student_on_a_module_instance.md#MOD_INSTANCE_ID)
- [student_on_a_module_instance.COURSE_INSTANCE_ID](udd/student_on_a_module_instance.md#COURSE_INSTANCE_ID)
- [student_on_course_instance.STUDENT_ID](udd/student_on_course_instance.md#STUDENT_ID)
- [student_on_course_instance.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_on_course_instance.md#STUDENT_COURSE_MEMBERSHIP_ID)
- [student_on_course_instance.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_on_course_instance.md#STUDENT_COURSE_MEMBERSHIP_SEQ)
- [student_on_course_instance.COURSE_INSTANCE_ID](udd/student_on_course_instance.md#COURSE_INSTANCE_ID)


##Category 2;
These properties are needed drive application to function well for all students. They are mostly labels for things, or basic facts about courses. If they are missing from records, the user experience for the relevant learners and the staff that support them could be significantly impaired.
- [staff.STAFF_ID](udd/staff.md#STAFF_ID)
- [staff_on_course_instance.STAFF_ID](udd/staff_on_course_instance.md#STAFF_ID)
- [staff_on_course_instance.COURSE_INSTANCE_ID](udd/staff_on_course_instance.md#COURSE_INSTANCE_ID)
- [staff_on_mod_instance.STAFF_ID](udd/staff_on_mod_instance.md#STAFF_ID)
- [staff_on_mod_instance.MOD_INSTANCE_ID](udd/staff_on_mod_instance.md#MOD_INSTANCE_ID)
- [assessment_instance.ASSESS_TYPE_ID](udd/assessment_instance.md#ASSESS_TYPE_ID)
- [assessment_instance.ASSESS_TYPE_NAME](udd/assessment_instance.md#ASSESS_TYPE_NAME)
- [assessment_instance.ASSESS_DETAIL](udd/assessment_instance.md#ASSESS_DETAIL)
- [assessment_instance.ASSESS_WEIGHT](udd/assessment_instance.md#ASSESS_WEIGHT)
- [course.TITLE](udd/course.md#TITLE)
- [institution.TENANT_NAME](udd/institution.md#TENANT_NAME)
- [course.INST_TIER_1](udd/course.md#INST_TIER_1)
- [course.INST_TIER_2](udd/course.md#INST_TIER_2)
- [course.INST_TIER_3](udd/course.md#INST_TIER_3)
- [module.MOD_NAME](udd/module.md#MOD_NAME)
- [student.AGE](udd/student.md#AGE)
- [student.LAST_NAME](udd/student.md#LAST_NAME)
- [student.FIRST_NAME](udd/student.md#FIRST_NAME)
- [student.APPSHIB_ID](udd/student.md#APPSHIB_ID)
- [student.VLE_ID](udd/student.md#VLE_ID)
- [student.USERNAME](udd/student.md#USERNAME)
- [student_course_membership.COURSE_JOIN_DATE](udd/student_course_membership.md#COURSE_JOIN_DATE)
- [student_course_membership.COURSE_END_DATE](udd/student_course_membership.md#COURSE_END_DATE)
- [student_on_assessment_instance.ASSESS_AGREED_MARK](udd/student_on_assessment_instance.md#ASSESS_AGREED_MARK)
- [student_on_assessment_instance.ASSESS_ACTUAL_MARK](udd/student_on_assessment_instance.md#ASSESS_ACTUAL_MARK)
- [student_on_assessment_instance.ASSESS_AGREED_GRADE](udd/student_on_assessment_instance.md#ASSESS_AGREED_GRADE)
- [student_on_assessment_instance.ASSESS_ACTUAL_GRADE](udd/student_on_assessment_instance.md#ASSESS_ACTUAL_GRADE)



Category 3
These properties are needed for the analytics models to function well for all students. They are mostly basic facts about courses. If they are missing from records, the user experience for the relevant learners and the staff that support them could be significantly impaired.
- [student_on_assessment_instance.STUDENT_ID](udd/student_on_assessment_instance.md#STUDENT_ID)
- [student_on_assessment_instance.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_on_assessment_instance.md#STUDENT_COURSE_MEMBERSHIP_ID)
- [student_on_assessment_instance.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_on_assessment_instance.md#STUDENT_COURSE_MEMBERSHIP_SEQ)
- [student_on_assessment_instance.MOD_INSTANCE_ID](udd/student_on_assessment_instance.md#MOD_INSTANCE_ID)
- [student_on_assessment_instance.ASSESS_INSTANCE_ID](udd/student_on_assessment_instance.md#ASSESS_INSTANCE_ID)
- [student_on_assessment_instance.ASSESS_SEQ_ID](udd/student_on_assessment_instance.md#ASSESS_SEQ_ID)
- [assessment_instance.MOD_INSTANCE_ID](udd/assessment_instance.md#MOD_INSTANCE_ID)
- [assessment_instance.ASSESS_INSTANCE_ID](udd/assessment_instance.md#ASSESS_INSTANCE_ID)
- [module_VLE_map.VLE_MOD_ID](udd/module_VLE_map.md#VLE_MOD_ID)
- [module_VLE_map.MOD_INSTANCE_ID](udd/module_VLE_map.md#MOD_INSTANCE_ID)
- [course_instance.ACADEMIC_YEAR](udd/course_instance.md#ACADEMIC_YEAR)
- [course_instance.START_DATE](udd/course_instance.md#START_DATE)
- [course_instance.END_DATE](udd/course_instance.md#END_DATE)
- [student_on_a_module_instance.MOD_START_DATE](udd/student_on_a_module_instance.md#MOD_START_DATE)
- [student_on_a_module_instance.MOD_END_DATE](udd/student_on_a_module_instance.md#MOD_END_DATE)
- [student_on_a_module_instance.MOD_FIRST_MARK](udd/student_on_a_module_instance.md#MOD_FIRST_MARK)
- [student_on_a_module_instance.MOD_ACTUAL_MARK](udd/student_on_a_module_instance.md#MOD_ACTUAL_MARK)
- [student_on_a_module_instance.MOD_AGREED_MARK](udd/student_on_a_module_instance.md#MOD_AGREED_MARK)
- [module_instance.MOD_ACADEMIC_YEAR](udd/module_instance.md#MOD_ACADEMIC_YEAR)
- [student_course_membership.WITHDRAWAL_REASON](udd/student_course_membership.md#WITHDRAWAL_REASON)
- [student_course_membership.COURSE_MARK](udd/student_course_membership.md#COURSE_MARK)

 
Category 4.
These properties are used to build a learning analytics model and personalise the outputs. The properties include several facts about learners. Whether these properties should be included in an learning record warehouse upload depends on striking the right balance between the precision and power of the particular analyses that an institution is interested in, and the data protection policies they have. This balance is best determined in discussion.

- [assessment_instance.ASSESS_TYPE_ID](udd/assessment_instance.md#ASSESS_TYPE_ID)
- [course.COURSE_AIM](udd/course.md#COURSE_AIM)
- [module.MOD_SUBJECT](udd/module.md#MOD_SUBJECT)
- [module.MOD_CREDITS](udd/module.md#MOD_CREDITS)
- [module.MOD_LEVEL](udd/module.md#MOD_LEVEL)
- [module_instance.MOD_ONLINE](udd/module_instance.md#MOD_ONLINE)
- [student.DOB](udd/student.md#DOB)
- [student.ETHNICITY](udd/student.md#ETHNICITY)
- [student.SEXID](udd/student.md#SEXID)
- [student.LEARN_DIF](udd/student.md#LEARN_DIF)
- [student.DISABILITY1](udd/student.md#DISABILITY1)
- [student.DISABILITY2](udd/student.md#DISABILITY2)
- [student.DOMICILE](udd/student.md#DOMICILE)
- [student.TERMTIME_ACCOM](udd/student.md#TERMTIME_ACCOM)
- [student.PARENTS_ED](udd/student.md#PARENTS_ED)
- [student.SOCIO_EC](udd/student.md#SOCIO_EC)
- [student.OVERSEAS](udd/student.md#OVERSEAS)
- [student_course_membership.ENTRY_QUALS](udd/student_course_membership.md#ENTRY_QUALS)
- [student_course_membership.COURSE_OUTCOME](udd/student_course_membership.md#COURSE_OUTCOME)
- [student_course_membership.COURSE_EXPECTED_END_DATE](udd/student_course_membership.md#COURSE_EXPECTED_END_DATE)
- [student_course_membership.COURSE_GRADE](udd/student_course_membership.md#COURSE_GRADE)
- [student_on_assessment_instance.ASSESSMENT_RESULT](udd/student_on_assessment_instance.md#ASSESSMENT_RESULT)
- [student_on_assessment_instance.ASSESSMENT_CURRENT_ATTEMPT](udd/student_on_assessment_instance.md#ASSESSMENT_CURRENT_ATTEMPT)
- [student_on_a_module_instance.MOD_CURRENT_ATTEMPT](udd/student_on_a_module_instance.md#MOD_CURRENT_ATTEMPT)
- [student_on_a_module_instance.MOD_RESULT](udd/student_on_a_module_instance.md#MOD_RESULT)
- [student_on_course_instance.MODE](udd/student_on_course_instance.md#MODE)
- [student_on_course_instance.YEAR_PRG](udd/student_on_course_instance.md#YEAR_PRG)
- [student_on_course_instance.YEAR_STU](udd/student_on_course_instance.md#YEAR_STU)
- [course.SUBJECT](udd/course.md#SUBJECT)

##Category 5
These properties are optional, but can be useful in building more fine 
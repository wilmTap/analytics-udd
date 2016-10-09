#A guide to mandatory properties in the UDD

Because many different organisations use UDD data for many different purposes, it is not possible to be categorical about which properties have to be present in UDD compliant data that is submitted to the Jisc learning analytics Learning Record Warehouse (LRW). For example, there are some properties that are required for the LRW and other applications to function because they link different data entities, just as there are properties such as course titles that are needed just to provide labels in applications. Other properties such as marks are vitally important for practically all learning analysis, but may only be available at certain points in time.

For that reason, the UDD includes five categories of property, each of which need consideration when deciding which data to include when submitting to the LRW.

##Category 1 
These properties are required for the data in the learning record warehouse to function. They are mostly identifiers that allow different entities to be linked to each other. Each data record will have to have these properties.

- [course.COURSE_ID](udd/course.md#course_id)
- [course_instance.COURSE_ID](udd/course_instance.md#course_id)
- [course_instance.COURSE_INSTANCE_ID](udd/course_instance.md#course_instance_id)
- [institution.TENANT_ID](udd/institution.md#tenant_id)
- [module.MOD_ID](udd/module.md#mod_id)
- [module_instance.MOD_INSTANCE_ID](udd/module_instance.md#mod_instance_id)
- [module_instance.MOD_ID](udd/module_instance.md#mod_id)
- [student.STUDENT_ID](udd/student.md#student_id)
- [student_course_membership.STUDENT_ID](udd/student_course_membership.md#student_id)
- [student_course_membership.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_course_membership.md#student_course_membership_id)
- [student_course_membership.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_course_membership.md#student_course_membership_seq)
- [student_course_membership.COURSE_ID](udd/student_course_membership.md#course_id)
- [student_on_a_module_instance.STUDENT_ID](udd/student_on_a_module_instance.md#student_id)
- [student_on_a_module_instance.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_on_a_module_instance.md#student_course_membership_id)
- [student_on_a_module_instance.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_on_a_module_instance.md#student_course_membership_seq)
- [student_on_a_module_instance.COURSE_INSTANCE_ID](udd/student_on_a_module_instance.md#course_instance_id)
- [student_on_a_module_instance.MOD_INSTANCE_ID](udd/student_on_a_module_instance.md#mod_instance_id)
- [student_on_a_module_instance.COURSE_INSTANCE_ID](udd/student_on_a_module_instance.md#course_instance_id)
- [student_on_course_instance.STUDENT_ID](udd/student_on_course_instance.md#student_id)
- [student_on_course_instance.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_on_course_instance.md#student_course_membership_id)
- [student_on_course_instance.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_on_course_instance.md#student_course_membership_seq)
- [student_on_course_instance.COURSE_INSTANCE_ID](udd/student_on_course_instance.md#course_instance_id)


##Category 2
These properties are needed drive application to function well for all students. They are mostly labels for things, or basic facts about courses. If they are missing from records, the user experience for the relevant learners and the staff that support them could be significantly impaired.
- [staff.STAFF_ID](udd/staff.md#staff_id)
- [staff_on_course_instance.STAFF_ID](udd/staff_on_course_instance.md#staff_id)
- [staff_on_course_instance.COURSE_INSTANCE_ID](udd/staff_on_course_instance.md#course_instance_id)
- [staff_on_mod_instance.STAFF_ID](udd/staff_on_mod_instance.md#staff_id)
- [staff_on_mod_instance.MOD_INSTANCE_ID](udd/staff_on_mod_instance.md#mod_instance_id)
- [assessment_instance.ASSESS_TYPE_ID](udd/assessment_instance.md#assess_type_id)
- [assessment_instance.ASSESS_TYPE_NAME](udd/assessment_instance.md#assess_type_name)
- [assessment_instance.ASSESS_DETAIL](udd/assessment_instance.md#assess_detail)
- [assessment_instance.ASSESS_WEIGHT](udd/assessment_instance.md#assess_weight)
- [course.TITLE](udd/course.md#title)
- [institution.TENANT_NAME](udd/institution.md#tenant_name)
- [course.INST_TIER_1](udd/course.md#inst_tier_1)
- [course.INST_TIER_2](udd/course.md#inst_tier_2)
- [course.INST_TIER_3](udd/course.md#inst_tier_3)
- [module.MOD_NAME](udd/module.md#mod_name)
- [student.AGE](udd/student.md#age)
- [student.LAST_NAME](udd/student.md#last_name)
- [student.FIRST_NAME](udd/student.md#first_name)
- [student.APPSHIB_ID](udd/student.md#appshib_id)
- [student.VLE_ID](udd/student.md#vle_id)
- [student.USERNAME](udd/student.md#username)
- [student_course_membership.COURSE_JOIN_DATE](udd/student_course_membership.md#course_join_date)
- [student_course_membership.COURSE_END_DATE](udd/student_course_membership.md#course_end_date)
- [student_on_assessment_instance.ASSESS_AGREED_MARK](udd/student_on_assessment_instance.md#assess_agreed_mark)
- [student_on_assessment_instance.ASSESS_ACTUAL_MARK](udd/student_on_assessment_instance.md#assess_actual_mark)
- [student_on_assessment_instance.ASSESS_AGREED_GRADE](udd/student_on_assessment_instance.md#assess_agreed_grade)
- [student_on_assessment_instance.ASSESS_ACTUAL_GRADE](udd/student_on_assessment_instance.md#assess_actual_grade)



##Category 3
These properties are needed for the analytics models to function well for all students. They are mostly basic facts about courses. If they are missing from records, the user experience for the relevant learners and the staff that support them could be significantly impaired.
- [student_on_assessment_instance.STUDENT_ID](udd/student_on_assessment_instance.md#student_id)
- [student_on_assessment_instance.STUDENT_COURSE_MEMBERSHIP_ID](udd/student_on_assessment_instance.md#student_course_membership_id)
- [student_on_assessment_instance.STUDENT_COURSE_MEMBERSHIP_SEQ](udd/student_on_assessment_instance.md#student_course_membership_seq)
- [student_on_assessment_instance.MOD_INSTANCE_ID](udd/student_on_assessment_instance.md#mod_instance_id)
- [student_on_assessment_instance.ASSESS_INSTANCE_ID](udd/student_on_assessment_instance.md#assess_instance_id)
- [student_on_assessment_instance.ASSESS_SEQ_ID](udd/student_on_assessment_instance.md#assess_seq_id)
- [assessment_instance.MOD_INSTANCE_ID](udd/assessment_instance.md#mod_instance_id)
- [assessment_instance.ASSESS_INSTANCE_ID](udd/assessment_instance.md#assess_instance_id)
- [module_VLE_map.VLE_MOD_ID](udd/module_VLE_map.md#vle_mod_id)
- [module_VLE_map.MOD_INSTANCE_ID](udd/module_VLE_map.md#mod_instance_id)
- [course_instance.ACADEMIC_YEAR](udd/course_instance.md#academic_year)
- [course_instance.START_DATE](udd/course_instance.md#start_date)
- [course_instance.END_DATE](udd/course_instance.md#end_date)
- [student_on_a_module_instance.MOD_START_DATE](udd/student_on_a_module_instance.md#mod_start_date)
- [student_on_a_module_instance.MOD_END_DATE](udd/student_on_a_module_instance.md#mod_end_date)
- [student_on_a_module_instance.MOD_FIRST_MARK](udd/student_on_a_module_instance.md#mod_first_mark)
- [student_on_a_module_instance.MOD_ACTUAL_MARK](udd/student_on_a_module_instance.md#mod_actual_mark)
- [student_on_a_module_instance.MOD_AGREED_MARK](udd/student_on_a_module_instance.md#mod_agreed_mark)
- [module_instance.MOD_ACADEMIC_YEAR](udd/module_instance.md#mod_academic_year)
- [student_course_membership.WITHDRAWAL_REASON](udd/student_course_membership.md#withdrawal_reason)
- [student_course_membership.COURSE_MARK](udd/student_course_membership.md#course_mark)

 
##Category 4.
These properties are used to build a learning analytics model and personalise the outputs. The properties include several facts about learners. Whether these properties should be included in an learning record warehouse upload depends on striking the right balance between the precision and power of the particular analyses that an institution is interested in, and the data protection policies they have. This balance is best determined in discussion.

- [assessment_instance.ASSESS_TYPE_ID](udd/assessment_instance.md#assess_type_id)
- [course.COURSE_AIM](udd/course.md#course_aim)
- [module.MOD_SUBJECT](udd/module.md#mod_subject)
- [module.MOD_CREDITS](udd/module.md#mod_credits)
- [module.MOD_LEVEL](udd/module.md#mod_level)
- [module_instance.MOD_ONLINE](udd/module_instance.md#mod_online)
- [student.DOB](udd/student.md#dob)
- [student.ETHNICITY](udd/student.md#ethnicity)
- [student.SEXID](udd/student.md#sexid)
- [student.LEARN_DIF](udd/student.md#learn_dif)
- [student.DISABILITY1](udd/student.md#disability1)
- [student.DISABILITY2](udd/student.md#disability2)
- [student.DOMICILE](udd/student.md#domicile)
- [student.TERMTIME_ACCOM](udd/student.md#termtime_accom)
- [student.PARENTS_ED](udd/student.md#parents_ed)
- [student.SOCIO_EC](udd/student.md#socio_ec)
- [student.OVERSEAS](udd/student.md#overseas)
- [student_course_membership.ENTRY_QUALS](udd/student_course_membership.md#entry_quals)
- [student_course_membership.COURSE_OUTCOME](udd/student_course_membership.md#course_outcome)
- [student_course_membership.COURSE_EXPECTED_END_DATE](udd/student_course_membership.md#course_expected_end_date)
- [student_course_membership.COURSE_GRADE](udd/student_course_membership.md#course_grade)
- [student_on_assessment_instance.ASSESSMENT_RESULT](udd/student_on_assessment_instance.md#assessment_result)
- [student_on_assessment_instance.ASSESSMENT_CURRENT_ATTEMPT](udd/student_on_assessment_instance.md#assessment_current_attempt)
- [student_on_a_module_instance.MOD_CURRENT_ATTEMPT](udd/student_on_a_module_instance.md#mod_current_attempt)
- [student_on_a_module_instance.MOD_RESULT](udd/student_on_a_module_instance.md#mod_result)
- [student_on_course_instance.MODE](udd/student_on_course_instance.md#mode)
- [student_on_course_instance.YEAR_PRG](udd/student_on_course_instance.md#year_prg)
- [student_on_course_instance.YEAR_STU](udd/student_on_course_instance.md#year_stu)
- [course.SUBJECT](udd/course.md#subject)

##Category 5
These properties are optional, but can be useful in building more fine grained analysis models. At the moment, the value of these properties as predictors are usually unknown, but their inclusion can help establish their utility. This category comprises the remainder of the UDD properties.
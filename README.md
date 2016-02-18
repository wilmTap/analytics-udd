# Analytics Universal Data Definitions

##Introduction
The Unified Data Definitions (UDD) of the Jisc analytics project is a vocabulary of the chief data entities of interest to learning analytics: students, courses, modules, etc. as well as their characteristics. The data coded with this vocabulary is typically extracted from the student record system of a particular college or university.

Along with xAPI recipes, the UDD makes up the core data specification of the Jisc learning analytics architecture.

##Workflow
The simplest way of contributing to the UDD works as follows:

1. add an issue to the issue tracker to alert everyone to what you are working on and why
2. tag the issue with the version milestone you'd like the patch to be a part of
3. make an edit or add a file in this repository, and save it to your own branch. If you prefer, you can fork the whole repository and work in your own repository
4. send a pull request once you're done
5. the pull request will be discussed at our weekly meeting and either merged, or kept in the queue, depending on whether more work is required

You can do all this through the Github GUI, but you're welcome to use any other git tool you prefer.

If the need arises, particular versions will get their own branches, but until that time, everything is merged into the main branche. Releases will be made after the group has come to an agreement.

## Core sections
###[Institution](udd/institution.md)
* [TENANT_ID](udd/institution.md#tenant_id)
* [TENANT_NAME](udd/institution.md#tenant_name)

###[Student](udd/student.md)
* [STUDENT_ID](udd/student.md#student_id)
* [ULN](udd/student.md#uln)
* [DOB](udd/student.md#dob)
* [ETHNICITY](udd/student.md#ethnicity)
* [SEXID](udd/student.md#gender)
* [AGE](udd/student.md#age)
* [LEARN_DIF](udd/student.md#learn_dif)
* [DISABILITY1](udd/student.md#disability1)
* [DISABILITY2](udd/student.md#disability2)
* [DOMICILE](udd/student.md#domicile)
* [TERMTIME_ACCOM](udd/student.md#termtime_accom)
* [PARENTS_ED](udd/student.md#parents_ed)
* [SOCIO_EC](udd/student.md#socio_ec)
* [OVERSEAS](udd/student.md#overseas)
* [APPSHIB_ID](udd/student.md#APPSHIB_id)
* [VLE_ID](udd/student.md#vle_id)

###[Course](udd/course.md)
* [COURSE_ID](udd/course.md#course_id)
* [SUBJECT](udd/course.md#subject)
* [TITLE](udd/course.md#title)
* [COURSE_AIM](udd/course.md#course_aim)

###[Course Instance](udd/course_instance.md)
* [COURSE_ID](udd/course_instance.md#course_id)
* [COURSE_INSTANCE_ID](udd/course_instance.md#course_instance_id)
* [START_DATE](udd/course_instance.md#start_date)
* [END_DATE](udd/course_instance.md#end_date)
* [ACADEMIC_YEAR](udd/course_instance.md#academic_year)

###[Student on Course Instance](udd/student_on_course_instance.md)
* [STUDENT_ID](udd/student_on_course_instance.md#student_id)
* [COURSE_INSTANCE_ID](udd/student_on_course_instance.md#course_instance_id)
* [WITHDRAWAL_REASON](udd/student_on_course_instance.md#withdrawal_reason)
* [WITHDRAWAL_DATE](udd/student_on_course_instance.md#withdrawal_date)
* [MODE](udd/student_on_course_instance.md#mode)
* [YEAR_COM](udd/student_on_course_instance.md#year_com)
* [YEAR_PRG](udd/student_on_course_instance.md#year_prg)
* [YEAR_STU](udd/student_on_course_instance.md#year_stu)
* [COURSE_AVERAGE_GRADE](udd/student_on_course_instance.md#course_average_grade)
* [YEAR_AVERAGE_GRADE](udd/student_on_course_instance.md#year_average_grade)
* [ENTRY_QUALS](udd/student_on_course_instance.md#entry_quals)
* [ENTRY_POINTS](udd/student_on_course_instance.md#entry_points)
* [COURSE_OUTCOME](udd/student_on_course_instance.md#course_outcome)
* [COURSE_GRADE](udd/student_on_course_instance.md#course_grade)
* [CAMPUS](udd/student_on_course_instance.md#campus)

###[Module](udd/module.md)
* [MOD_ID](udd/module.md#mod_id)
* [MOD_NAME](udd/module.md#mod_name)
* [MOD_SUBJECT](udd/module.md#mod_subject)
* [MOD_CREDITS](udd/module.md#mod_credits)
* [MOD_LEVEL](udd/module.md#mod_level)

###[Module Instance](udd/module_instance.md)
* [MOD_ID](udd/module_instance.md#mod_id)
* [MOD_INSTANCE_ID](udd/module_instance.md#mod_instance_id)
* [MOD_START_DATE](udd/module_instance.md#mod_start_date)
* [MOD_END_DATE](udd/module_instance.md#mod_end_date)
* [MOD_PERIOD](udd/module_instance.md#mod_period)
* [MOD_ONLINE](udd/module_instance.md#mod_online)
* [MOD_ENROLLMENT](udd/module_instance.md#mod_enrollment)
* [MOD_ACADEMIC_YEAR](udd/module_instance.md#mod_academic_year)
* [MOD_OPTIONAL](udd/module_instance.md#mod_optional)

###[Student on a module Instance](udd/student_on_module_instance.md)
* [STUDENT_ID](udd/student_on_module_instance.md#student_id)
* [COURSE_INSTANCE_ID](udd/student_on_module_instance.md#course_instance_id)
* [MOD_INSTANCE_ID](udd/student_on_module_instance.md#mod_instance_id)
* [MOD_OUTCOME](udd/student_on_module_instance.md#mod_outcome)
* [MOD_GRADE](udd/student_on_module_instance.md#mod_grade)
* [MOD_PASS](udd/student_on_module_instance.md#mod_pass)
* [MOD_RETAKE](udd/student_on_module_instance.md#mod_retake)

###[Grade](udd/grade.md)
* [STUDENT_ID](udd/grade.md#student_id)
* [MOD_INSTANCE_ID](udd/grade.md#mod_instance_id)
* [GRADABLE_OBJECT](udd/grade.md#gradable_object)
* [CATEGORY](udd/grade.md#category)
* [MAX_POINTS](udd/grade.md#max_points)
* [EARNED_POINTS](udd/grade.md#earned_points)
* [WEIGHT](udd/grade.md#weight)
* [GRADE_DATE](udd/grade.md#grade_date)

###[Activity](udd/activity.md)
* [STUDENT_ID](udd/activity.md#student_id)
* [MOD_ID](udd/activity.md#mod_id)
* [EVENT](udd/activity.md#event)
* [EVENT_DATE](udd/activity.md#event_date)

##Additional sections 
###[Student (Additional Information)](udd/student_additional.md)
* [STUDENT_ID](udd/student_additional.md#student_id) - link to Student Instance in UDD 1.1
* [USERNAME](udd/student_additional.md#username)
* [LAST_NAME](udd/student_additional.md#last_name)
* [FIRST_NAME](udd/student_additional.md#first_name)
* [ADDRESS_LINE_1](udd/student_additional.md#address_line_1)
* [ADDRESS_LINE_2](udd/student_additional.md#address_line_2)
* [ADDRESS_LINE_3](udd/student_additional.md#address_line_3)
* [ADDRESS_LINE_4](udd/student_additional.md#address_line_4)
* [POSTCODE](udd/student_additional.md#postcode)
* [PRIMARY_EMAIL_ADDRESS](udd/student_additional.md#primary_email_address)
* [HOME_PHONE](udd/student_additional.md#home_phone)
* [MOBILE_PHONE](udd/student_additional.md#mobile_phone)
* [PHOTO_URL](udd/student_additional.md#photo_url)
* [COACH_SCHOOL_ID](udd/student_additional.md#coach_school_id)

###[Staff teaching a module Instance](staff_on_mod_instance.md)
*  [STAFF_ID](udd/staff_on_mod_instance.md#staff_id)
*  [MOD_INSTANCE_ID](udd/staff_on_mod_instance.md#mod_instance_id) - link to Module Instance in UDD 1.1

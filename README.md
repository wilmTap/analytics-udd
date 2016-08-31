# Jisc Learning Analytics Unified Data Definitions v1.3

##Introduction
The Unified Data Definitions (UDD) of the Jisc analytics project is a vocabulary of the chief data entities of interest to learning analytics: students, courses, modules, etc. as well as their characteristics. The data coded with this vocabulary is typically extracted from the student record system of a particular college or university.

Along with xAPI recipes, the UDD makes up the core data specification of the Jisc learning analytics architecture.

##Differences between 1.2 and 1.3
The development of 1.3 involved a number of additions and changes. [This overview page](differences.md) provides a mapped listing of each change, with links through to the relevant pages in the UDD 1.2 and 1.3 documentation.

##Data format
No particular data format is prescribed yet for UDD data sets, but both JSON and CSV are popular have been used. Regardless of the fileformat, any UDD dataset needs to be UTF8 encoded.

##Diagram
An [entity relation diagram of the whole UDD 1.3](diagram.md) provides a one page overview of the specification.

## Core sections
###[Assessment instance](udd/assessment_instance.md)

###[Course](udd/course.md)

###[Course instance](udd/course_instance.md)

###[Institution](udd/institution.md)

###[Module](udd/module.md)

###[Module instance](udd/module_instance.md)

###[Module to VLE map](udd/module_vle_map.md)

###[Student](udd/student.md)

###[Student course membership](udd/student_course_membership.md)

###[Student on assessment instance](udd/student_on_assessment_instance.md)

###[Student on module instance](udd/student_on_a_module_instance.md)

###[Student on course instance](udd/student_on_course_instance.md)

##Additional sections 
###[Staff](udd/staff.md)

###[Staff on course instance](udd/staff_on_course_instance.md)

###[Staff on module Instance](udd/staff_on_mod_instance.md)

###[Student (Additional Information)](udd/student_additional.md)

##Specification development workflow
The simplest way of contributing to the UDD works as follows:

1. add an issue to the issue tracker to alert everyone to what you are working on and why
2. tag the issue with the version milestone you'd like the patch to be a part of
3. make an edit or add a file in this repository, and save it to your own branch. If you prefer, you can fork the whole repository and work in your own repository
4. send a pull request once you're done
5. the pull request will be discussed at our weekly meeting and either merged, or kept in the queue, depending on whether more work is required

You can do all this through the Github GUI, but you're welcome to use any other git tool you prefer.

Particular release versions will get their own branches, but the main branch will always contain the latest agreed release. Releases will be made after the group has come to an agreement.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

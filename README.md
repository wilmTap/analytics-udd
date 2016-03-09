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

###[Student](udd/student.md)

###[Course](udd/course.md)

###[Course Instance](udd/course_instance.md)

###[Student on Course Instance](udd/student_on_course_instance.md)

###[Student Course Membership](udd/student_course_membership.md)

###[Module](udd/module.md)

###[Module Instance](udd/module_instance.md)

###[Student on a module Instance](udd/student_on_a_module_instance.md)

###[Grade](udd/grade.md)

###[Activity](udd/activity.md)

##Additional sections 
###[Student (Additional Information)](udd/student_additional.md)

###[Staff teaching a module Instance](staff_on_mod_instance.md)

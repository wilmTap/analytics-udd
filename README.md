# Jisc Learning Analytics Unified Data Definitions v1.2.7

##Introduction
The Unified Data Definitions (UDD) of the Jisc analytics project is a vocabulary of the chief data entities of interest to learning analytics: students, courses, modules, etc. as well as their characteristics. The data coded with this vocabulary is typically extracted from the student record system of a particular college or university.

Along with xAPI recipes, the UDD makes up the core data specification of the Jisc learning analytics architecture.

##Differences between 1.1 and 1.2
The development of 1.2 involved a number of additions and changes. [This overview page](differences.md) provides a mapped listing of each change, with links through to the relevant pages in the UDD 1.1 and 1.2 documentation.

##Data format
No particular data format is prescribed yet for UDD data sets, but both JSON and CSV are popular have been used. Regardless of the fileformat, any UDD dataset needs to be UTF8 encoded.

##Diagram
An [entity relation diagram of the whole UDD 1.2](diagram.md) provides a one page overview of the specification.

## Core sections
###[assessment_instance](udd/assessment_instance.md)

###[course](udd/course.md)

###[course_instance](udd/course_instance.md)

###[institution](udd/institution.md)

###[module](udd/module.md)

###[module_instance](udd/module_instance.md)

###[module_vle_map](udd/module_vle_map.md)

###[student](udd/student.md)

###[student_course_membership](udd/student_course_membership.md)

###[student_on_assessment_instance](udd/student_on_assessment_instance.md)

###[student_on_a_module_instance](udd/student_on_a_module_instance.md)

###[student_on_course_instance](udd/student_on_course_instance.md)

##Additional sections 
###[staff](udd/staff.md)

###[staff_on_course_instance](udd/staff_on_course_instance.md)

###[staff_on_mod_instance](udd/staff_on_mod_instance.md)

##Mandatory and optional properties
The properties of the UDD are required in compliant datasets to different degrees. The [guide to mandatory properties in the UDD](mandatory.md) outlines the different categories of UDD property.

##Specification development workflow
The simplest way of contributing to the UDD works as follows:

1. add an issue to the issue tracker to alert everyone to what you are working on and why
2. tag the issue with the version milestone you'd like the patch to be a part of
3. make an edit or add a file in this repository, and save it to your own branch. If you prefer, you can fork the whole repository and work in your own repository
4. send a pull request once you're done
5. the pull request will be discussed at our weekly meeting and either merged, or kept in the queue, depending on whether more work is required

You can do all this through the Github GUI, but you're welcome to use any other git tool you prefer.

Particular release versions will get their own branches, but the main branch will always contain the latest agreed release. Releases will be made after the group has come to an agreement.

##Acknowledgements

Many thanks to all contributors who have raised issues, sent pull requests, commented and made suggestions. The UDD specification is the achievement of all of you.

@andrewhickey
@arc12
@christoffballard
@ds10
@gryglbrt
@ht2 
@huwrobertsjisc
@jfmullaney
@michaelwebjisc
@MiroslavKratchounov
@robwynj
@ryansmith94
@sandeepmjay
@wilmTap

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

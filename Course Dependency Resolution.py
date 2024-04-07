#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:49:23 2024

@author: soumyajeet
"""
class Course:
    def __init__(self, name, prerequisites=None):
        self.name = name
        self.prerequisites = set(prerequisites) if prerequisites else set()
        self.completed = False

class CourseResolver:
    def __init__(self, courses):
        self.courses = {course.name: course for course in courses}

    def is_ready(self, course_name, completed_courses):
        course = self.courses[course_name]
        ready = all(prereq in completed_courses for prereq in course.prerequisites)
        print(f"{course_name} is ready: {ready}")
        return ready

    def find_ready_courses(self, completed_courses):
        ready_courses = []
        for course_name, course in self.courses.items():
            if course_name not in completed_courses and self.is_ready(course_name, completed_courses):
                ready_courses.append(course_name)
        print("Ready courses:", ready_courses)
        return ready_courses

    def resolve_dependencies(self):
        completed_courses = set()
        completion_order = []

        while len(completion_order) != len(self.courses):
            ready_courses = self.find_ready_courses(completed_courses)

            if not ready_courses:
                print("Circular dependency detected between courses:", completed_courses)
                return None

            for course_name in ready_courses:
                completed_courses.add(course_name)
                completion_order.append(course_name)

        return completion_order

# Example usage
courses_data = {
    "Calculus": ["Linear Algebra"],
    "Linear Algebra": [],
    "Statistics": [],
    "Machine Learning": ["Statistics"],
    "Deep Learning": ["Machine Learning"]
}


courses = [Course(name, prerequisites) for name, prerequisites in courses_data.items()]

resolver = CourseResolver(courses)
completion_order = resolver.resolve_dependencies()

if completion_order:
    print("Recommended Course Completion Order:")
    print(completion_order)



       ############################### READ ME #########################################
       
#The above Program is Class based , we can write in Function based also ,here is what exactly happeing 


# First Iteration:

# The algorithm finds that 'Linear Algebra' and 'Statistics' are ready to be taken, as they have no prerequisites.
# It adds 'Linear Algebra' and 'Statistics' to the completion_order.
# Second Iteration:

# 'Calculus' becomes ready because 'Linear Algebra' has been completed.
# 'Machine Learning' becomes ready because 'Statistics' has been completed.
# 'Calculus' and 'Machine Learning' are added to the completion_order.
# Third Iteration:

# 'Deep Learning' becomes ready because 'Machine Learning' has been completed.
# 'Deep Learning' is added to the completion_order.
# Fourth Iteration:

# No courses are ready to be taken as all prerequisites for remaining courses are not completed yet.
# The algorithm detects a circular dependency between 'Machine Learning', 'Deep Learning', and 'Statistics', as all are interdependent in a loop.
# The algorithm halts and reports the circular dependency.
# Completion Order:

# The completion order provided is ['Linear Algebra', 'Statistics', 'Calculus', 'Machine Learning', 'Deep Learning'], which represents the order in which the courses are resolved before the circular dependency is detected.
# This sequence demonstrates how the algorithm progresses through each course, adding them to the completion order as their prerequisites are fulfilled, until a circular dependency is encountered.



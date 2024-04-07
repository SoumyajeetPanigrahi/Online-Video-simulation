#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:30:45 2024

@author: soumyajeet
"""

class PersonalizedLearningPathGenerator:
    def __init__(self, user_data, courses_data):
        self.user_data = user_data
        self.courses_data = courses_data

    def generate_learning_path(self):
        # Step 1: Extract user's interests from user data
        interests = self.user_data['interests']
        
        # Step 2: Retrieve past course engagements and performance data
        past_courses = self.user_data['past_courses']
        performance_data = self.user_data['performance']

        print("Interests:", interests)  # Debug statement
        print("Past courses:", past_courses)  # Debug statement

        # Step 3: Calculate relevance scores for uncompleted courses based on interests
        course_scores = {}
        for course_id, course_info in self.courses_data.items():
            if course_id not in past_courses and self.are_prerequisites_completed(course_info['prerequisites']):
                relevance_score = self.calculate_relevance_score(course_info['topics'], interests)
                course_scores[course_id] = relevance_score

        print("Course scores:", course_scores)  # Debug statement

        # Step 4: Sort uncompleted and prerequisite-fulfilled courses by relevance score
        sorted_courses = sorted(course_scores.items(), key=lambda x: x[1], reverse=True)

        print("Sorted courses:", sorted_courses)  # Debug statement

        # Step 5: Generate learning path based on sorted uncompleted and prerequisite-fulfilled courses
        learning_path = [course_id for course_id, _ in sorted_courses[:3]]  # Considering top 3 relevant courses

        return learning_path

    def calculate_relevance_score(self, course_topics, interests):
        # Simple relevance score calculation based on topic overlap
        intersection = set(course_topics) & set(interests)
        return len(intersection) / len(interests) if interests else 0

    def are_prerequisites_completed(self, prerequisites):
        # Check if all prerequisites are completed by the user
        return all(prerequisite in self.user_data['past_courses'] for prerequisite in prerequisites)

# Example usage:
user_data = {
    'interests': ['machine learning', 'data science'],
    'past_courses': ['course1', 'course2'],
    'performance': {'course1': 0.8, 'course2': 0.6}
}

courses_data = {
    'course1': {'topics': ['Python'], 'prerequisites': []},
    'course2': {'topics': ['machine learning'], 'prerequisites': ['course1']},
    'course3': {'topics': ['data science'], 'prerequisites': ['course1']},
    'course4': {'topics': ['deep learning'], 'prerequisites': ['course2']}
}

plp_generator = PersonalizedLearningPathGenerator(user_data, courses_data)
learning_path = plp_generator.generate_learning_path()
print("Personalized Learning Path:", learning_path)




####################`READ ME ########################################


# The user's interests are 'machine learning' and 'data science'.
# The past courses completed by the user are 'course1' and 'course2'.
# Based on the available courses and the user's interests, 'course3' has a relevance score of 0.5, indicating it aligns well with the user's interests. However, 'course4' has a relevance score of 0.0, suggesting it may not be as relevant.
# Since both 'course3' and 'course4' have been identified as uncompleted courses and 'course3' has a higher relevance score, it is prioritized over 'course4' in the learning path.













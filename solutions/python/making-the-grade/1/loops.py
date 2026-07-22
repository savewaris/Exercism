"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    for i in range(len(student_scores)):
        student_scores[i] = round(student_scores[i])
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    count = 0
    for i in range(len(student_scores)):
        if student_scores[i] <= 40:
            count+=1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    
    new_list = []
    for i in range(len(student_scores)):
        if student_scores[i] >= threshold:
            new_list.append(student_scores[i])
    return new_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    fail_score = 40
    remain_peroid_score = (highest - fail_score)/4
    return [41, 41+round(remain_peroid_score), 41+(round(remain_peroid_score)*2), 41+(round(remain_peroid_score)*3)]
    # return remain_peroid_score
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    new_list = []
    for i in range(len(student_names)):
        new_list.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return new_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    if student_info == [] or student_info == None:
        return []
    for i in range(len(student_info)):
        if 100 in student_info[i]:
            return student_info[i]
            break;
    return []
            
    
            
    
    

'''
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
Notes:

The score of the students is between 1 and 100.
'''

def csAverageOfTopFive(scores):
    
    studentID = set([s[0] for s in scores])
    
    dict_score = []
    
    for id in studentID:
        score_lst = [s[1] for s in scores if s[0] == id]
        top5_lst = sorted(score_lst, reverse=True)[:5]
        # Need floor division (//) to remove decimals and attain desired output
        average = sum(top5_lst) // len(top5_lst)
        dict_score.append([id, average])
    return dict_score

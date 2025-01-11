import turtle
from random import randint

import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states] #list comprehension
        # missing_states = []
        # for state in all_states:
        #     if state not in  guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())



screen.exitonclick()




# Dictionary Comprehension
# import random
# names  =['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# #students_scores = {new_key:new_value for item in list}
# students_scores = {student:random.randint(1,100) for student in names}
# # print(students_scores)
# passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}

#
#
#
# student_dict = {
#     "student":["Angela","James","Lily"],
#     "score": [56,76,98]
# }
#
# #Looping through dictionaries
# for (key,value) in student_dict.items():
#     print(value)
#     # print(key)
#
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# #Looping through a dataframe
# for (key,value) in student_data_frame.items():
#     print(value)
#
# #Loop through rows of a data frame
#
# for (index,row) in student_data_frame.iterrows():
#     print(index)
#     print(row) #Pandas series object
#     print(row.student)
#     print(row.score)
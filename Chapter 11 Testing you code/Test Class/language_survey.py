import survey as s 

# Define a question and make a survey

question = "What language did you first learn to speak, except motherlanguage"
language_survey = s.AnonimousSurvey(question)

#Show the question, store the responses

language_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)
    
#Show the result of the survey
print("Thank you for partecipating in the survey\n")
language_survey.show_results()

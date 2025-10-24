class AnonimousSurvey:
    
    """Collects anonymous answer to a survey"""
    
    def __init__(self, question):
        
        """Store a question and prepare to store responses
        """
        
        self.question = question
        self.responses = []
        
    def show_question(self):
        
        """Show the question survey
        """
        
        print(self.question)
        
    def store_response(self, new_response):
        
        
        """Store a single response to the survey
        """
        
        self.responses.append(new_response)
        
    def show_results(self):
        
        """Show all the responses that have been given
        """
        
        print("Survey Results: ")
        for response in self.responses:
            print(f"-{response}")
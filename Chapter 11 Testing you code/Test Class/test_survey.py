from survey import AnonimousSurvey
import pytest


@pytest.fixture
def language_survey():
    
    """A survey that will be available to all test functons
    """
    question = "What language did you first learn to speak, except motherlanguage"
    language_survey = AnonimousSurvey(question)
    return language_survey
    
def test_store_single_response(language_survey):
    
    """Test that a single response is stored correctly
    """
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    
def test_store_three_responses(language_survey):
    
    """Test that three individual responses are stored properly
    """
    
    responses = ['English','Italian','French']
    
    for response in responses:
        
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses
#The setup() method
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setup(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Igbo']

    def test_store_single_response(self):
        """Test that a single response is stored."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0])

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.reponses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
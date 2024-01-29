import random

class CollegeAdmissionChatbot:
    def __init__(self):
        self.user_data = {}

    def welcome_message(self):
        return "Welcome to the College Admission Chatbot! How can I assist you today?"

    def handle_query(self, user_input):
        if "hello" in user_input.lower():
            return "Hello! " + self.welcome_message()
        elif "admission" in user_input.lower():
            return self.admission_info()
        elif "necessities" in user_input.lower():
            return self.admission_necessities()
        elif "lifetime" in user_input.lower():
            return self.admission_lifetime()
        elif "goodbye" in user_input.lower():
            return "Goodbye! If you have more questions, feel free to ask anytime."
        else:
            return "I'm sorry, I couldn't understand that. Please ask a different question."

    def admission_info(self):
        return "Our college admission process involves several steps, including submitting an application, providing transcripts, and attending an interview."

    def admission_necessities(self):
        return "To be eligible for admission, you need to have a high school diploma or equivalent. Additional needs may vary by program."

    def admission_lifetime(self):
        return "The admission lifetime depend on the program. It's essential to check the specific lifetime for the course you're interested in."

    def chat(self):
        print(self.welcome_message())

        while True:
            user_input = input("User: ")
            if not user_input:
                continue

            if user_input.lower() == "exit":
                print("Goodbye! If you have more questions, feel free to ask anytime.")
                break

            response = self.handle_query(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    chatbot = CollegeAdmissionChatbot()
    chatbot.chat()

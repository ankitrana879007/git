import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    # Basic Conversation ------------------------------------------------------
    if "what is your name" in user_data:
        msg = "My name is Virtual Assistant, My master personal AI helper."
    
    elif "how are you" in user_data:
        msg = "I'm functioning perfectly, thank you. How are you?"

    elif "hello" in user_data or "hye" in user_data or "hi" in user_data:
        msg = "Hello sir, how can I assist you today?"

    elif "good morning" in user_data:
        msg = "Good morning sir. I hope your day starts with positivity."
    
    elif "good night" in user_data:
        msg = "Good night sir. Sweet dreams and take care."
    
    elif "thank you" in user_data:
        msg = "You are most welcome sir."

    elif "who made you" in user_data:
        msg = "I was created by my master, Mr. Ankit, with a lot of ideas and caffeine."

    elif "do you have feelings" in user_data:
        msg = "Not exactly, but I understand emotions well enough to respond politely."

    # Time & System -----------------------------------------------------------
    elif "time now" in user_data or "what time" in user_data:
        current_time = datetime.datetime.now()
        msg = f"The time is {current_time.hour} hour and {current_time.minute} minutes."

    elif "shutdown" in user_data:
        msg = "Okay sir, shutting down my services."

    # Browsing Commands -------------------------------------------------------
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        msg = "Opening Gaana.com for your music experience."

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        msg = "Opening Youtube for you."

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        msg = "Google is ready for you."

    elif "open instagram" in user_data:
        webbrowser.open("https://instagram.com/")
        msg = "Opening Instagram. Enjoy exploring."

    elif "open facebook" in user_data:
        webbrowser.open("https://facebook.com/")
        msg = "Facebook is now open for you."

    # Knowledge Questions -----------------------------------------------------
    elif "who is the prime minister" in user_data:
        msg = "The Prime Minister of India is Narendra Modi."

    elif "distance between earth and moon" in user_data:
        msg = "The average distance between Earth and the Moon is 384,400 kilometers."

    elif "largest ocean" in user_data:
        msg = "The Pacific Ocean is the largest ocean on Earth."

    elif "who invented computer" in user_data:
        msg = "The first mechanical computer was invented by Charles Babbage."

    elif "speed of light" in user_data:
        msg = "The speed of light is approximately 299,792 kilometers per second."

    # Maths -------------------------------------------------------------------
    elif "add" in user_data or "plus" in user_data:
        try:
            nums = [int(s) for s in user_data.split() if s.isdigit()]
            msg = f"The result is {sum(nums)}"
        except:
            msg = "Please tell me the numbers clearly."

    elif "multiply" in user_data:
        try:
            nums = [int(s) for s in user_data.split() if s.isdigit()]
            result = 1
            for n in nums:
                result *= n
            msg = f"The multiplied result is {result}"
        except:
            msg = "I couldn't identify the numbers you said."

    # Weather -----------------------------------------------------------------
    elif "weather" in user_data:
        ans = weather.weather()
        msg = ans

    # Motivational ------------------------------------------------------------
    elif "motivate me" in user_data:
        msg = "Success is not about speed, it's about consistency. Keep moving forward."

    elif "tell me a quote" in user_data:
        msg = "The best way to predict the future is to create it."

    # Jokes -------------------------------------------------------------------
    elif "joke" in user_data:
        msg = "Why don’t programmers like nature? Too many bugs."

    elif "funny" in user_data:
        msg = "I'm not a comedian, but here's one: Parallel lines have so much in common. It’s a shame they’ll never meet."

    # Facts -------------------------------------------------------------------
    elif "tell me a fact" in user_data:
        msg = "Honey never spoils. Archaeologists found honey 3000 years old and it was still safe to eat."

    elif "space fact" in user_data:
        msg = "A day on Venus is longer than a year on Venus."

    # Study Help --------------------------------------------------------------
    elif "what is ai" in user_data:
        msg = "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence."

    elif "what is python" in user_data:
        msg = "Python is a high-level programming language used for automation, AI, data science, and more."

    elif "what is machine learning" in user_data:
        msg = "Machine Learning is a branch of AI where systems learn from data without being explicitly programmed."

    # Creative Replies ---------------------------------------------------------
    elif "are you smart" in user_data:
        msg = "I am as smart as the code written inside me, but I try my best to help you."

    elif "are you alive" in user_data:
        msg = "Not biologically, but digitally I'm always active for you."

    elif "sing a song" in user_data:
        msg = "I can't sing but I can suggest songs. Just say 'play music'."

    elif "tell me something" in user_data:
        msg = "Did you know? Your brain generates enough electricity to power a small light bulb."

    # Catch-All ----------------------------------------------------------------
    else:
        msg = "I'm not fully trained on that question yet, but I'm learning more every day."

    # Speak and Return ---------------------------------------------------------
    text_to_speech.text_to_speech(msg)
    return msg

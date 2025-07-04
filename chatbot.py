import webbrowser
import wikipedia
from pytube import Search
import os
# Ensure that the Wikipedia language is set to English
wikipedia.set_lang("en")

# Function to play a YouTube video based on a search query
def playYoutubeVideo(query):
    try:
        s = Search(query)
        videoUrl = s.results[0].watch_url
        webbrowser.open(videoUrl)
    except Exception as e:
        print(f"Bot: Error searching YouTube: {e}")

print("Hello ! I am your personal assistant. How can I Assist you today?")
print("Type 'bye' to exit the chat.")

while True:
    userInput = input("You: ").strip().lower()
    if not userInput:
        print("Bot: Please enter something.")
        continue

    userInput = userInput.split()
    ls = [ "open","start", "launch", "run"]
    #For exit from the chatbot
    if "bye" in userInput:
        print("Bot: Goodbye! Have a great day!")
        break

    #For searching in google
    elif "search" in userInput:
        searchQuery = " ".join(userInput[1:])
        if searchQuery:
            print(f"Bot: Searching the web for '{searchQuery}'...")
            webbrowser.open(f"https://www.google.com/search?q={searchQuery}")
        else:
            print("Bot: Please provide a search term.")

    #For play vedio in youtube
    elif "play" in userInput:
        searchQuery = " ".join(userInput[1:])
        if searchQuery:
            print(f"Bot: Playing the first YouTube video for '{searchQuery}'...")
            playYoutubeVideo(searchQuery)
        else:
            print("Bot: Please provide a search term for the video.")

    #For searching in wikipedia
    elif "wikipedia" in userInput:
        searchQuery = " ".join(userInput)
        if searchQuery:
            print(f"Bot: Searching Wikipedia for '{searchQuery}'...")
            try:
                summary = wikipedia.summary(searchQuery, sentences=2)
                print(f"Bot: {summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Bot: The term '{searchQuery}' is ambiguous. Please be more specific.")
            except wikipedia.exceptions.PageError:
                print(f"Bot: No Wikipedia page found for '{searchQuery}'.")
        else:
            print("Bot: Please provide a search term for Wikipedia.")

    #For opening websites
    elif "open web" in userInput:
        webName = " ".join(userInput[2:])
        if webName:
            try:
                webbrowser.open(f"https://www.{webName}.com")
                print(f"Bot: Opening {webName}...")
            except Exception as e:
                print(f"Bot: Could not open {webName}. Error: {e}")
        else:
            print("Bot: Please provide a website name to open.")
    
    #For opening applications
    elif any(word in userInput for word in ls):
        app_name = " ".join(userInput[1:])
        if app_name:
            try:
                os.system(f"start {app_name}")
                print(f"Bot: Opening {app_name}...")
            except Exception as e:
                print(f"Bot: Could not open {app_name}. Error: {e}")
        else:
            print("Bot: Please provide an application name to open.")
    
    #For opening websites
    

    







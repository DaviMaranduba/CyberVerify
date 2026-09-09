import rules

def analyze():
    message = input("\033[0;37mEnter the message you want to analyze: \n>\033[0m ")
    for word in rules.suspicious_words:
        if word in message.lower():
            print(word)
    return message


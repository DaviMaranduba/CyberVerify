import rules

def analyze():
    message = input("\033[0;37mEnter the message you want to analyze: \n>\033[0m ")
    found_words = []
    for word in rules.suspicious_words:
        if word in message.lower():
            found_words.append(word)

    if found_words:
        print("Suspicious words found:", found_words)
    else:
        print("No suspicious words found.")

    if len(found_words) == 0:
        return "Low Risk"
    elif len(found_words) <= 2:
        return "Medium Risk"
    else:
        return "High Risk"

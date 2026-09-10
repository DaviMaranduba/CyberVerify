import rules

def analyze():
    message = input("\033[0;37mEnter the message you want to analyze: \n>\033[0m ")
    found_words = []
    for word in rules.suspicious_words:
        if word in message.lower():
            found_words.append(word)

    if found_words:
        print(f"\033[33m*SUSPICIOUS WORDS FOUND*:\033[0m", found_words)
    else:
        print("\033[32m*NO SUSPICIOUS WORDS FOUND.*\033[0m")

    if len(found_words) == 0:
        return "\033[32m🟢 LOW RISK\033[m"
    elif len(found_words) <= 2:
        return "\033[33m🟡 MEDIUM RISK\033[m"
    else:
        return "\033[31m🔴 HIGH RISK\033[m"

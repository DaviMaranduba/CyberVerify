import rules


class MessageAnalyzer:
    def __init__(self, message):
        self.message = message.lower()
        self.found_words = []

    def find_suspicious_words(self):
        self.found_words = []
        for word in rules.suspicious_words:
            if word in self.message:
                self.found_words.append(word)
        return self.found_words

    def get_risk_level(self):
        self.find_suspicious_words()
        if len(self.found_words) == 0:
            return "\033[32m🟢 LOW RISK\033[m"
        elif len(self.found_words) <= 2:
            return "\033[33m🟡 MEDIUM RISK\033[m"
        return "\033[31m🔴 HIGH RISK\033[m"


def get_risk_level(message):
    analyzer = MessageAnalyzer(message)
    return analyzer.get_risk_level()

    
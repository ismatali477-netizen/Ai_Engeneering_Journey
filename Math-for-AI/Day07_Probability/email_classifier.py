def classify_email(probability):
    return "spam" if probability>=0.5 else "not spam"

def classifier_summary(probabilities):
    spam_count=0
    not_spam_count=0
    for prob in probabilities:
        if prob>=0.5:
            spam_count+=1
        else:
            not_spam_count+=1
    return spam_count,not_spam_count
email_probabilities = [0.92, 0.81, 0.35, 0.12, 0.66, 0.48]
if __name__ == "__main__":
    for i, prob in enumerate(email_probabilities, start=1):
        print(f"Email {i}: {classify_email(prob)} ({prob:.2f})")

    spam, not_spam = classifier_summary(email_probabilities)
    print(f"\nSpam Emails: {spam}")
    print(f"Not Spam Emails: {not_spam}")
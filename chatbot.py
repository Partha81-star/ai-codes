def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        msg = input("You: ").lower().strip()

        if msg in ["hello", "hi"]:
            print("Chatbot: Hi! How are you?")

        elif msg == "how are you":
            print("Chatbot: I am fine!")

        elif msg == "what is your name":
            print("Chatbot: My name is AI Bot.")

        elif msg == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
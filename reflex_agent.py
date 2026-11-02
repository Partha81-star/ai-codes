def vacuum(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location=="B":
        return "Left"
    else:
        return"Invalid i/p...!"
location = input("Enter location (A/B): ")
status = input("Enter status (Clean/Dirty): ")
print("Action:", vacuum(location, status))

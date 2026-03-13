from datetime import datetime
def gettime():
    """
    * Returns the current time of day as a string
    ? morning: 5-11, afternoon: 12-16, evening: 17-20, night: 21-4
    """
    hour = datetime.now().hour
    if 5 <= hour <= 11:
        return "morning"
    elif 12 <= hour <= 16:
        return "afternoon"
    elif 17 <= hour <= 20:
        return "evening"
    else:
        return "night"
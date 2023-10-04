# assuming that the twenty four hour clock is e.g. 15:23 read as three twnety three

hour_minute_dictionary = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "one", "14": "two", "15": "three", "16": "four", "17": "five", "18": "six", "19": "seven", "20": "eight", "21": "nine", "22": "ten", "23": "eleven", "24": "twelve"}
tens_dictionary = {"0": "", "1": "ten", "2": "twenty", "3": "thirty", "4": "fourty", "5": "fifty"}
teens_dictionary = {"13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}

def human_readable_time(time):

    hour = time.split(":")[0]
    minutes = time.split(":")[1]

    if minutes == "00":
        return f"{hour_minute_dictionary[hour]} o'clock"
    
    if minutes == "30":
        return f"half past {hour_minute_dictionary[hour]}"
    
    if minutes == "01":
        return f"one minute past {hour_minute_dictionary[hour]}"
    
    if minutes == "59":
        index = str(int(hour) + 1)
        return f"one minute to {hour_minute_dictionary[index]}"
    
    if minutes == "15":
        return f"quarter past {hour_minute_dictionary[hour]}"
    
    if minutes == "45":
        index = str(int(hour) + 1)
        return f"quarter to {hour_minute_dictionary[index]}"
    
    if int(minutes) < 30:
        
        if int(minutes) >= 13 and int(minutes)<= 19:
            return f"{teens_dictionary[minutes]} minutes past {hour_minute_dictionary[hour]}"
        
        if int(minutes) <= 12:
            return f"{hour_minute_dictionary[minutes]} minutes past {hour_minute_dictionary[hour]}"
        
        return f"{tens_dictionary[minutes[0]]} {hour_minute_dictionary[minutes[1]]} minutes past {hour_minute_dictionary[hour]}"
    
    index = str(int(hour) + 1)
    time_till = str(60 - int(minutes))
    if len(time_till) == 1:
        time_till = "0" + time_till

    return f"{tens_dictionary[time_till[0]]} {hour_minute_dictionary[time_till[1]]} minutes to {hour_minute_dictionary[index]}"

time_input = input("Enter a time in the format x:yy: ")
print(human_readable_time(time_input))
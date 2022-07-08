from datetime import datetime
import json

def sample_response(input_text):
    user_message = str(input_text).lower()
    f = open("../response.json")
    data = json.load(f)
    for i in data['Response']:
        if user_message in i['input']:
            return i['output']
    if user_message in ("time","time??","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    return "I don't understand you sucker"

#print(sample_response("xxx"))
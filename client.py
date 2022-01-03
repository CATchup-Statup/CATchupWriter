import requests
import json

URL = "http://127.0.0.1:5000/predict"
#URL = "https://score-rest.herokuapp.com/predict"
#URL = "http://167.99.214.132/predict"

#TEST_AUDIO_FILE = "AudioFIle/voce.wav"

if __name__ == "__main__":
    #files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
    data=json.dumps({"data" : "0@1@2@3@4@5@6"})
    response = requests.post(URL, json=data )
    

    #data = response.json()

    print(str(response))
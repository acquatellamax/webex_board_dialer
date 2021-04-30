import requests
import json

dial_uri = "https://webexapis.com/v1/telephony/calls/dial"
answer_url = "https://webexapis.com/v1/telephony/calls/answer"
divert_url = "https://webexapis.com/v1/telephony/calls/divert"
get_call_status_url = "https://webexapis.com/v1/telephony/calls/"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer MWM5ZjVjNDMtZGExMy00MTI1LTkzYTYtZDgyMzY5MjgyNTU3MzZiODdmMTMtZjkz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
}

###GENERATE DIAL ID

payload_destination = json.dumps({
    "destination": "1000"  # set to the address of the board
})


def dial(uri, header, payload):
    response_dial = requests.request("POST", uri, headers=header, data=payload)
    dial_id_destination = response_dial.json()["callId"]
    return dial_id_destination


callId1 = dial(dial_uri, headers, payload_destination)
print(callId1)


###DIAL DESTINATION USING CALLID1 - SHOULD DIAL BOARD

payload_dial = json.dumps({
  "callId": callId1
})
response = requests.request("POST", answer_url, headers=headers, data=payload_dial)
print(response.text)


###WHILE LOOP TO WAIT USER TO ANSWER CALL AND THEN DIVERT TO HUNT GROUP

response_get_call_status = requests.request("GET", get_call_status_url, headers=headers).json()
#print(response_get_call_status)

while response_get_call_status["items"][0]["state"] != "connected":
    print("ring")
    #print(response_get_call_status)
    response_get_call_status = requests.request("GET", get_call_status_url, headers=headers).json()
    if response_get_call_status["items"][0]["state"] == "connected":
        break


####DIVERT CALL AND CONNECT BOARD WITH HUNT GROUP

payload_divert = json.dumps({
    "callId": callId1,
    "destination": "1010", ### number or address of hunt group
    "toVoicemail": False
})

response_divert = requests.request("POST", divert_url, headers=headers, data=payload_divert)
#print(response_divert.text)
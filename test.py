response_get_call_status = {
    "items": [
        {
            "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL0NBTEwvY2FsbGhhbGYtNDAwNDYzMzE6MA",
            "callSessionId": "MzEwNmQ0NjYtMmQ0NC00NzNjLWI4ZjAtZTM1NGJiZWFhOTQ5",
            "personality": "originator",
            "state": "connected",
            "remoteParty": {
                "name": "Reception .",
                "number": "1000",
                "placeId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1BFT1BMRS9hYjQ0MzZmZS04NTBjLTQzNDYtYThjNS05YjFlYWIyZjVmM2Q",
                "privacyEnabled": False,
                "callType": "location"
            },
            "appearance": 1,
            "created": "2021-04-02T20:42:40.202Z",
            "answered": "2021-04-02T20:43:07.310Z",
            "recordingState": "stopped"
        }
    ]
}

print(response_get_call_status["items"][0]["state"])

print(response_get_call_status["items"][0]["state"] != "connected")

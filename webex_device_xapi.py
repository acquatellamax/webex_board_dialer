import requests

def dial():
    url = "https://10.118.81.163/putxml"

    payload = """
                <Command>
                    <Dial>
                        <Number>+17207746934</Number>
                    </Dial>
                </Command>"""

    headers = {
      'Authorization': 'Basic aW50ZWdyYXRvcjpDMXNjMDEyMzQ=',
      'Content-Type': 'application/xml'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response.text)

import json
import urllib.parse
import urllib.request


# ex. GET
url = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"
headers = {
    "Content-Type": "application/json"
}
req = urllib.request.Request(
    url,
    headers=headers,
    method="GET"
)
# ex. POST
if False:
    url = ""
    data = urllib.parse.urlencode({
        "key": "val"
    }).encode("ascii")
    headers = {
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(
        url,
        headers=headers,
        method="POST"
    )
try:
    with urllib.request.urlopen(req) as resp:
        body = resp.read()
        body = json.loads(body)
        print("-- publishingOffice")
        print(body["publishingOffice"])
        print("-- reportDatetime")
        print(body["reportDatetime"])
        print("-- targetArea")
        print(body["targetArea"])
except urllib.error.HTTPError as err:
    print(err)
except urllib.error.HTTPError as err:
    print(err)

import json,lianzhong_api
def get_yzm(driver,imgname):
    true=1
    result='{"data": {"val": "FAA4", "id": 8631454506}, "result": true}'
    val=json.loads(result)["data"]["val"]
    #val = result.split(":")[2].split(",")[0][1:-1]
    print(val)
    return val

get_yzm(1,2)
有代理的能跑通的
#coding=utf8
import requests
import json
import pandas as pd

class Csv:

    def _get_dataframe(self, obj_list):
        data = {}
        for d in obj_list:
            for key, value in d.items():
                if key not in data:
                    data[key] = []
                data[key].append(value)
        df = pd.DataFrame(data)
        return df

    def to_csv(self, data, filename, **kwargs):
        df = self._get_dataframe(data)
        df.to_csv(filename, **kwargs)

url = 'https://wap3.hispace.hicloud.com/uowap/index?method=internal.getTabDetail&serviceType=13&reqPageNum=1&uri=cb9506a7afc14b5ba9fc89afb9876924&maxResults=25&ver=1.1&locale=en_US'
ip='81.201.60.130:80'
proxies = {
  'https': 'https://' + ip,
}
kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=kv,proxies=proxies)
content = r.content  # 获取json
result = json.loads(content)  # 转换成字典
csv_data = []
for item in result["layoutData"][0]["dataList"]:
    csv_data.append({
        "name": item["name"],
        "tagName": item["tagName"],
        "package": item["package"],
        "downCountDesc": item["downCountDesc"],
        "memo": item["memo"]
    })
#print (csv_data)
csv_file = './app01.csv'
Csv().to_csv(csv_data, csv_file)

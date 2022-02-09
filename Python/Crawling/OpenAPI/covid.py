from xml.etree import ElementTree
import requests
import re

service_key = 'VXBYQ69L5Fwe5N6ROU%2BQDFRw2QT7VAQq2iW9WUSFjTxT5tCatN27CjwGwFKDLtqMhSaBV2BfjIAhytbw2lcWmg%3D%3D'
url = f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}"

res = requests.get(url).text
tree = ElementTree.fromstring(res)      # 파싱

for item in tree[1][0]:                 # body > items
    # print(item.find('gubun').text)
    if item.find('gubun').text == '합계':
        stdDay = re.sub(r'(\D)+', '', item.find('stdDay').text)
        stdDay = stdDay[2:4] + "/" + stdDay[4:6] + "/" + stdDay[6:8]
        incDec = item.find('incDec').text
        local = item.find('localOccCnt').text
        overFlowCnt = item.find('overFlowCnt').text
        print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{local}\n해외발생:{overFlowCnt}')


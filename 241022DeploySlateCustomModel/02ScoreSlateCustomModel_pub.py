# 環境設定
import pprint
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
api_key = 'PASTE YOUR PLATFORM API KEY HERE'
url = 'PASTE YOUR ENDPOINT HERE'

space_id = 'PASTE YOUR SPACE ID HERE'
deployment_id = 'PASTE YOUR DEPLOYMENT ID HERE'


# WMLへの接続
credentials = Credentials(
    api_key=api_key,
    url=url
)

client_space = APIClient(credentials, space_id=space_id)

# 分類したい文章
scoring_payload = {
    "input_data": [{
        "values": [["ディスプレイは色鮮やかで、映画やゲームを楽しむのに最適です。"]]
    }]
}

# 分類実行
response = client_space.deployments.score(deployment_id, scoring_payload)
pprint.pprint(response["predictions"])

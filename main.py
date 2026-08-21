from openai import OpenAI
import requests
import os


client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://ws-kf91ptx5k3159d6p.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)


prompt = """
请生成《安徽科技日报》。

重点：
- 合肥
- 安徽

方向：
1. 人工智能
2. 具身智能
3. 量子科技
4. 可控核聚变
5. 生物科技

要求：
- Markdown格式
- 今日重点
- 产业动态
- 科研突破
- 融资信息
- 中文输出
"""


response = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


report = response.choices[0].message.content


requests.post(
    os.environ["FEISHU_WEBHOOK"],
    json={
        "msg_type":"text",
        "content":{
            "text":report
        }
    },
    timeout=20
)


print("发送成功")

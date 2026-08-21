from openai import OpenAI
import requests
import os


client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)


prompt = """
请生成《安徽前沿科技动态日报》。

重点关注：
- 合肥
- 安徽

领域：
1. 人工智能
2. 具身智能
3. 可控核聚变
4. 量子科技
5. 生物科技

要求：
- Markdown格式
- 包含今日重点
- 包含产业动态
- 包含科研突破
- 包含融资信息
"""


response = client.chat.completions.create(
    model="deepseek-chat",
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
        "msg_type": "text",
        "content": {
            "text": report
        }
    }
)


print("发送成功")

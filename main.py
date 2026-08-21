from openai import OpenAI
import requests
import os


client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


prompt = """
请生成《安徽前沿科技动态日报》。

重点关注：
合肥、安徽。

领域：
1. 人工智能
2. 具身智能
3. 可控核聚变
4. 量子科技
5. 生物科技

要求：
1. Markdown格式
2. 今日重点
3. 产业动态
4. 科研突破
5. 融资信息
6. 中文输出
7. 如果没有真实新闻，请明确写暂无，不要编造
"""


response = client.chat.completions.create(
    model="qwen2.5-7b-instruct",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)


report = response.choices[0].message.content


webhook = os.environ["FEISHU_WEBHOOK"]


requests.post(
    webhook,
    json={
        "msg_type": "text",
        "content": {
            "text": report
        }
    },
    timeout=20
)


print("安徽科技日报发送成功")

from openai import OpenAI
import requests
import os


# 阿里百炼 DashScope
client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
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
- 中文输出
- 内容真实，不要编造不存在的新闻
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


# 飞书机器人
webhook = os.environ["FEISHU_WEBHOOK"]

requests.post(
    webhook,
    json={
        "msg_type": "text",
        "content": {
            "text": report
        }
    },
    timeout=10
)


print("安徽科技日报发送成功")

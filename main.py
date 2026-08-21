from openai import OpenAI
import requests
import os


# =========================
# 阿里云百炼 OpenAI兼容接口
# =========================

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://ws-kf91ptx5k3159d6p.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)


# =========================
# 日报提示词
# =========================

prompt = """
你是一名安徽科技产业研究员。

请生成《安徽前沿科技动态日报》。

重点关注：
- 合肥
- 安徽省

关注领域：

1. 人工智能
2. 具身智能
3. 可控核聚变
4. 量子科技
5. 生物科技

报告结构：

# 安徽前沿科技动态日报

## 今日重点

## 产业动态

## 科研突破

## 融资信息

## 政策与园区动态


要求：
- 中文输出
- Markdown格式
- 信息真实可靠
- 不确定的信息不要编造
- 如果当天没有融资信息，请写“暂无公开融资信息”
"""


# =========================
# 调用模型
# =========================

response = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)


report = response.choices[0].message.content



# =========================
# 推送飞书
# =========================

webhook = os.environ["FEISHU_WEBHOOK"]


result = requests.post(
    webhook,
    json={
        "msg_type": "text",
        "content": {
            "text": report
        }
    },
    timeout=10
)


print("日报生成完成")
print("飞书状态:", result.status_code)

response = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {
            "role":"user",
            "content":"测试API是否正常"
        }
    ]
)

print(response.choices[0].message.content)

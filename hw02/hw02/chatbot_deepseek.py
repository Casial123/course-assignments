"""
Chatbot Demo - 调用火山引擎 DeepSeek API
运行前请先安装：pip install requests
"""

import requests
import json

# ===== 配置区域（请修改成你的）=====
API_KEY = "你的API_KEY"  # 从火山引擎获取
BOT_ID = "你的BOT_ID"    # 从火山引擎获取
API_URL = "https://ark.cn-beijing.volces.com/api/v3/bots/chat/completions"
# ================================

def chat_with_deepseek(user_input):
    """发送消息给DeepSeek并获取回复"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "bot_id": BOT_ID,
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()
        
        reply = result.get("choices", [{}])[0].get("message", {}).get("content", "无回复")
        return reply
    except Exception as e:
        return f"调用失败：{str(e)}"

def main():
    print("="*50)
    print("DeepSeek Chatbot 示例")
    print("输入 'exit' 退出")
    print("="*50)
    
    while True:
        user_input = input("\n👤 你：")
        if user_input.lower() == 'exit':
            print("👋 再见！")
            break
        
        print("🤖 DeepSeek：", end="")
        reply = chat_with_deepseek(user_input)
        print(reply)

if __name__ == "__main__":
    main()

import asyncio
import akasha
from langchain_mcp_adapters.client import MultiServerMCPClient

MODEL = "openai:gpt-4o"

# 定義 MCP 伺服器連接資訊
connection_info = {
    "playwright": {
        "url": "http://localhost:8931/sse",
        "transport": "sse",
    }
}
prompt = """
1. 開啟網站 https://eip.iii.ortg.tw
2. 等待使用者輸入帳號密碼，並且按下登入後登入
3. 點選全會通訊錄
4. 輸入「張芷銓」找出通訊資料
"""

# 使用 MCP 工具
agent = akasha.agents(
    model=MODEL,
    temperature=1.0,
    verbose=True,
    keep_logs=True,
)
# 問問題並使用 MCP 工具回答
response = akasha.call_mcp_agent(agent, connection_info, prompt)

print("\n\n---\n\n")
print(response)

# 保存日誌
agent.save_logs("logs_agent.json")
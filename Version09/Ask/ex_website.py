# 匯入套件
import akasha

# 設定模型資訊
ak = akasha.ask(model="openai:gpt-4o", verbose=True)

# 問下去：問模型本身知道的事情
response = ak(prompt="akasha是什麼？")

# 從參考資料來回答問題
response = ak(
    prompt="akasha是什麼？",
    info=["https://github.com/iii-org/akasha"],
)

# 從靜態網站資料來回答問題
response = ak(
    prompt="今天天氣如何？",
    info=["https://wttr.in/Taipei"],
)

# response = ak(
#     prompt="今天天氣如何？",
#     info=["https://www.cwa.gov.tw/V8/C/W/County/index.html"],
# )

print(response)
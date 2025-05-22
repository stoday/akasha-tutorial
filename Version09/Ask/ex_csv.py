# 匯入套件
import akasha

# 設定模型資訊
ak = akasha.ask(model="openai:gpt-4o", verbose=True)

# 從參考資料來回答問題
response = ak(
    prompt="請問鳶尾花有哪些品種？列出品種的名稱",
    info=["iris.csv"],
)

print('\n\n---\n\n')
print(response)
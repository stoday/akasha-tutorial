# 匯入套件
import akasha

# 設定模型資訊
ak = akasha.ask(model="openai:gpt-4o")

# 從參考資料來回答問題
response = ak(
    prompt="做一個約 200 字的摘要",
    info=["半導體趨勢分析報告.docx"],
)

print('\n\n---\n\n')
print(response)
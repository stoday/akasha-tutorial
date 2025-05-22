# 匯入套件
import akasha

# 設定模型資訊
ak = akasha.ask(model="openai:gpt-4o", verbose=True, temperature=0.5)

# 從參考資料來回答問題
response = ak(
    prompt="""
    請用今天台北的天氣資訊作為開頭，然後說：「好像變熱的天氣，半導體景氣...」，之後帶出半到體產業的摘要，寫成新的一份報告。分段落，但不要條列式說明。也多說一點天氣的事情""",
    info=["https://wttr.in/Taipei",
          "半導體趨勢分析報告.docx",],
)

print('\n\n---\n\n')
print(response)
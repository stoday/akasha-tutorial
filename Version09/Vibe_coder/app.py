import akasha

ak = akasha.ask(
    model="openai:gpt-4o", 
    max_input_tokens=8000, 
    keep_logs=True, verbose=True
)

response = ak(prompt=f"""
              幫我用 streamlit 與 akasha 完成以下寫程式任務:
            
              幫我寫一個問答機器人，可以回答關於 SBIR 的問題。
              這個機器人服務的標題要是「SBIR小幫手」。
              SBIR 的知識從網頁 https://www.moea.gov.tw/Mns/populace/Apply/Apply.aspx?menu_id=32814&apply_id=64 來取得。
            
              除了程式碼外不要有其他說明好讓我可以直接使用變成可執行的檔案。
              """,
              info=["https://tea9297.github.io/akasha/2024/12/29/ask/",
                    "./app_py.txt"])

# 將 response 內容寫入檔案
with open("app_for_show.py", "w", encoding="utf-8") as f:
    f.write(response)
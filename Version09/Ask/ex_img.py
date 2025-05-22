# 匯入套件
import akasha

# 設定模型資訊
ak = akasha.ask(model="openai:gpt-4o", verbose=True)

# 從網站圖片來回答問題
res = ak.vision(
    prompt="這張圖片是什麼?",
    image_path="https://upload.wikimedia.org/wikipedia/" \
    "commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/"
    "2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
)
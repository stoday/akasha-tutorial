import akasha

# 繪製圖片
save_path = akasha.gen_image(
    prompt="一隻可愛的絨毛娃娃，是北海道的長尾山雀，坐在白雪的樹枝上唱歌",
    model="gemini:gemini-2.0-flash-preview-image-generation",
    save_path="長尾山雀.png",
)

# 編輯圖片
save_path = akasha.edit_image(
    model="gemini:gemini-2.0-flash-preview-image-generation",
    prompt="增加一隻可愛的鯊魚娃娃在旁邊",
    images="長尾山雀.png",
    save_path="鯊鯊.png",
    env_file=".env3",
)
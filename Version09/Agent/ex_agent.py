import akasha


### 首先我們要定義一個函數，這個函數會回傳今天的日期 
def today_f():
    from datetime import datetime
    now = datetime.now()

    return "today's date: " + str(now.strftime("%Y-%m-%d %H:%M:%S"))


# 接著，我們要把這個函數轉換成一個工具，讓 agent 可以使用這個工具來回答問題
today_tool = akasha.create_tool(
    "today_date_tool",
    "This is the tool to get today's date, the tool don't have any input parameter.",
    today_f,
)

# 最後，我們要創建一個 agent，並把我們剛剛定義的工具傳入 agent 中
agent = akasha.agents(
    tools=[today_tool], model="openai:gpt-4o", temperature=1.0, verbose=True, keep_logs=True
)

agent("今天幾月幾號?")
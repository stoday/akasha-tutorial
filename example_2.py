import akasha
import torchvision
torchvision.disable_beta_transforms_warning()

boy_1 = akasha.Doc_QA(
    # model='remote:http://20.243.171.253:8601',
    model='openai:gpt-3.5-turbo',
    embeddings='huggingface:all-MiniLM-L6-v2',
    search_type='bm25',
    system_prompt='你是一個工程師，你要跟一個朋友聊天',
    temperature=0.8,
    verbose=False)

boy_2 = akasha.Doc_QA(
    model='remote:http://20.243.171.253:8601',
    embeddings='huggingface:all-MiniLM-L6-v2',
    search_type='bm25',
    system_prompt='你是一個作家，你要跟一個朋友聊天',
    temperature=0.8,
    verbose=False)

history_talk = []

times = 0
while True:
    if len(history_talk) > 0:
        boy_1_say = boy_1.ask_self(history=history_talk, prompt='與對方聊天')
        print(boy_1_say)
        history_talk.append(f'工程師說：{boy_1_say}')

        boy_2_say = boy_2.ask_self(history=history_talk, prompt='與對方聊天')
        print(boy_2_say)
        history_talk.append(f'作家說：{boy_1_say}')
    
    else:
        boy_1_say = boy_1.ask_self(history=history_talk, prompt='與對方打招呼')
        history_talk.append(f'工程師說：{boy_1_say}')
        
    times += 1
    if times > 10:
        break
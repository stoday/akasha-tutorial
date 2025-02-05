import akasha

ak = akasha.Doc_QA(
    model='remote:http://20.243.171.253:8601',
    embeddings='huggingface:all-MiniLM-L6-v2',
    search_type='bm25',
    verbose=True)

# response = ak.get_response(doc_path='./Docs',
#                            prompt='哪些條文有講到暴行的')

# response = ak.get_response(doc_path='./Docs',
#                            prompt='勞動基準法第3條是什麼？')

# response = ak.get_response(doc_path='./Docs',
#                            prompt='如果我老闆不付我薪水怎麼辦？')

keywords_list = []
for i in range(10, 15):
    response = ak.get_response(doc_path='./Docs', prompt=f'列出勞動基準法第{i}條?')
    print(response)

    keywords = ak.ask_self(response + '\n --- \n' + 
                           '''根據以上法條，產生相關的關鍵字，以供後續查找。產生的格式如下:
                           <關鍵字1>, <關鍵字2>, <關鍵字3>, ...''')
    print('\n ***\n', keywords, '\n ***')
    keywords_list.append(keywords.split(', '))
    
rules_keywords = {}
for i in range(10, 15):
    rules_keywords[f'勞動基準法第{i}條'] = keywords_list[i-10]

response = ak.ask_self(info=str(rules_keywords), prompt='請問有關職場暴力的條文有哪些？列出是第幾條的條文')

import akasha

ak = akasha.ask(model='openai:gpt-4o',
                temperature=0.0,
                verbose=True,)
# response = ak('哈囉')
# print(response)

response = ak(prompt='摘要條列式重點',
              info=['https://www.threads.com/@largitdata/post/DJ5eRFtvqR8?xmt=AQF0TbN5AwkW9svCNlC7k73SxTKuML1qk1A-ejtgjB6Nl60',])
print('\n\n---\n\n')
print(response)

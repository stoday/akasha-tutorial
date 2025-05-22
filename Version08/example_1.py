import akasha
import torchvision
torchvision.disable_beta_transforms_warning()

ak = akasha.Doc_QA(
    model='remote:http://20.243.171.253:8601',
    embeddings='huggingface:all-MiniLM-L6-v2',
    search_type='bm25',
    verbose=False)

response = ak.get_response('./Docs_Food', '請推薦我台中伴手禮')
print(response)

import akasha
import akasha.helper as ah


PROMPT = "企業在導入生程式 AI 要注意什麼？"

# create a RAG object and call it ###
ak = akasha.RAG(
    embeddings="openai:text-embedding-ada-002",
    model="openai:gpt-4o",
    max_input_tokens=3000,
    search_type="svm",
    verbose=True,
)

res = ak(
    data_source=["docs/", "https://github.com/iii-org/akasha"],
    prompt=PROMPT,
)

## get the reference document source dictionary that were used to answer the question##
ref_dict = ak.reference()

print('\n\n---\n\n')
print(res)
print(ref_dict)
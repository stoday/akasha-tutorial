import akasha

# python code
import akasha
ak = akasha.ask(
    model='remote:http://172.16.100.100@OpenGVLab--InternVL3-38B',
    env_file='.remote_env',
    verbose=False,
)

response = ak('哈囉，說個笑話吧！')

print('\n\n回答:', response)
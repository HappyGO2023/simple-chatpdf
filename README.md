1. 安装关联包
```shell
pip install -r requirements.txt
```

2. 引入OPENAI_API_KEY
```shell
export OPENAI_API_KEY={your-api-key}
# or
os.environ["OPENAI_API_KEY"] = {your-api-key}
```

3. 进行问答 
```shell
python3 embedding.py 
python3 qa.py 
```

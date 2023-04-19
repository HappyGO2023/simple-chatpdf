1. 安装关联包
pip install -r requirements.txt

2. 引入openai key
export OPENAI_API_KEY={your-api-key}
or
os.environ["OPENAI_API_KEY"] = {your-api-key}

3. 进行问答 
# embedding and persist
python3 embedding.py 
# load data and qa
python3 qa.py 

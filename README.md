1.安装关联包
``` shell 
pip install -r requirements.txt
```

2.引入openai key
```shell 
export OPENAI_API_KEY=....
```
也可以打开代码中的配置 # os.environ["OPENAI_API_KEY"] = "{your-api-key}"修改配置；

3.进行问答

```shell 
python3 embedding.py # embedding and persist
python3 qa.py # load data and qa
```

效果图如下：

<img src="qa.png" alt="export" width="900"/>

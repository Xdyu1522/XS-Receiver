# 笔趣阁小说获取器

几乎支持所有笔趣阁(出了问题我也没办法,可以在Issuse中提出,后面可能会添加支持<毕竟笔趣阁太多了>)  
使用python编写,8线程获取小说
输入链接地址(如http://*\*\*\*\*.com/book/\*\*\*\*\*\*\)与根地址(如http://www.*****.com)开始使用  
注:需要python3.x环境  
主要使用库:`requests` `beautifulsoup4` `tqdm` `fake_useragent` `os` `threading` `math` `ssl`  
使用方法(Windows Powerhell):  
```bash
git clone git@github.com:Xie1522/XS-Receiver.git
cd XS-Receiver
python -m venv rec_env
.\rec_env\Scripts\Activate.ps1
pip install requests beautifulsoup4 tqdm fake_useragent
python .\XS-Receiver.py
```  
当然也可以使用编译后的发布版本  
使用愉快  
Xie 2022.5
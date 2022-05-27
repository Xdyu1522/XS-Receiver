# 笔趣阁小说获取器

<!-- TOC -->

- [笔趣阁小说获取器](#笔趣阁小说获取器)
- [更新日志:](#更新日志)
  - [V1.0.1更新日志](#v101更新日志)
  - [V1.0更新日志](#v10更新日志)

<!-- /TOC -->

几乎支持所有笔趣阁(出了问题我也没办法,可以在Issuse中提出,后面可能会添加支持<毕竟笔趣阁太多了>)  
使用python编写,8线程获取小说
输入链接地址(如http://www.\*\*\*\*\*.com/book/\*\*\*\*\*\)与根地址(如http://www.\*\*\*\*\*.com)开始使用  
注:需要python3.x环境  
主要使用库:`requests`, `beautifulsoup4`, `tqdm`, `fake_useragent`, `colorama`, `os`, `threading`, `math`, `ssl` .   
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

# 更新日志:  
## V1.0.1更新日志  
1. 更新了重试功能,减少获取失败章节数量  
2. 更新了错误输出,更加简单易懂  
3. 更新了颜色输出,虽是终端,美观不能少  

新增使用库: `colorama`  
2022.5.27
## V1.0更新日志  
小说获取程序初代版本,具体请看[上方](#笔趣阁小说获取器)  
如果有无法获取的网站请在Issues中提出,可能会考虑添加支持  
使用愉快  
2022.5
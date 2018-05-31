# 项目背景

- ocr识别课件(PPT)需要大量的样本
- 人工下载的工作量大 效率低

# 项目依赖
- Python2x
- wget
- bs4

# 使用方法
- pip install -r requirements  权限不够就加sudo
- python getPpt.py

# 项目说明
- 1.搜集的样本根据学科分类


| 学科 | 文件夹 |
|:------|:------:|
| 语文 |  yuwen |
| 数学 |  shuxue |
| 英语 |  yingyu |
| 科学 |  kexue |
| 道德 |  daode |
| 生活 |  shenghuo |
| 社会 |  shehui |
| 品德 |  yuwen |
| 物理 |  yuwen |
| 化学 |  yuwen |
| 地理 |  yuwen |
| 历史 |  yuwen |
| 生物 |  yuwen |
| 美术 |  yuwen |
| 音乐 |  yuwen |
| 幼儿 |  yuwen |

- 2.各学科目录下为若干项.rar文件
- 3.需要解压.rar文件  可以用find命令解压
	- find . -name '*.rar' | xargs unrar x
[find命令及参数](http://man.linuxde.net/find)
[更详细的介绍](https://www.cnblogs.com/jiangzhaowei/p/5451173.html)
- 4.并不是所有的rar中全是PPT 需要删除不需要的文件
- 5.删除其他文件
	- find . ! -name '*.ppt*' | xargs rm
	- find . ! -name '*.ppt*' -delete














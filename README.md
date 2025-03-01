## 项目简介

本项目基于兼具加密与计算双重能力的全同态加密算法、利用微软开源库Microsoft-Seal而设计出的一套能够保护医疗数据的云计算系统。这是一套从信息采集到安全云计算的完整服务链的系统，使得医疗数据进行数据分析时能够得到有效的保护。

系统将覆盖医疗数据的从采集到存储及处理整个过程，包含以下四个部分：

**数据采集**：通过硬件采集患者相关数据；

**客户端**：为用户提高数据提交、存储和数据全同态运算的操作窗口；

**服务端存储**：用户管理以及加密后的医疗数据存储；

**第三方云计算**：提供医疗数据经过同态加密后的同态运算服务。

## 安装与使用

### 客户端：

1. `SEAL_core.py`放在项目根目录，直接作为模块import使用`import SEAL_core`；`_SEAL_core.pyd`放在`Python根目录/DLLs`
2. `pip install -r requirements.txt` 安装依赖
3. 进入./config.ini修改url为你的服务器ip+端口8888，即url= http://ip:8888
4. `cmd 运行start.py`即可（用cmd运行，powershell会有问题）

### 服务器:

1. `SEAL_service.py`放在项目根目录，直接作为模块import使用`import SEAL_service`；`_SEAL_service.so`放在`Python根目录/lib-dynload`
2. `pip install -r requirements.txt` 安装依赖
3. 终端运行app.py即可
4. 数据库：建库webproject，表doctor(字段为key_hash),默认ip为127.0.0.1，用户root，密码root


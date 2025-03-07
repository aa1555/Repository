@echo off
:: 将控制台切换为 UTF-8 编码模式
chcp 65001 > nul
cls

::切换目录，使命令在特定目录下执行。
cd /d C:\Users\aa155

echo 请直接输入库名进行安装库：
echo.

:: 获取用户输入
set /p library=python -m pip install 

::执行命令，“%library%”为获取的用户输入
python -m pip install %library%

echo.
echo 安装完成!
echo.

:: pause命令用于暂停批处理文件的执行，并显示一条消息“请按任意键继续. . .”。
pause

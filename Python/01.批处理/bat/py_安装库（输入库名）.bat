@echo off
::65001 是 UTF-8 的代码页，chcp 65001表示将编码设置为 UTF-8。Windows 批处理文件默认使用 ANSI 编码，而中文需要使用 UTF-8 编码。> 是重定向符号，用于将命令的输出重定向到指定位置。nul 是 Windows 系统中的空设备文件，表示丢弃输出。chcp 936会输出提示信息，用> nul将输出信息丢弃，为了界面整洁。
chcp 65001 >nul

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

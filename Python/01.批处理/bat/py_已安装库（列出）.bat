:: pip list 列出所有已安装的库

:: 关闭命令回显,这里用“::”注释掉关闭命令回显命令，这样命令就会回显。需要关闭命令回显时只需把“::”删掉即可。
@echo off 

::切换目录，使命令在特定目录下执行。
cd /d C:\Users\aa155

echo 正在检查已安装的库，请稍后...
echo.

:: 执行命令
python -m pip list

echo.
echo 已列出所有已安装的库!
echo.

:: pause命令用于暂停批处理文件的执行，并显示一条消息“请按任意键继续. . .”。
pause
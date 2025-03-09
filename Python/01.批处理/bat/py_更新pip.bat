@echo off

::切换目录，使命令在特定目录下执行。
cd /d C:\Users\aa155

echo 正在更新pip，请稍等...
echo.

::执行命令
python -m pip install --upgrade pip

echo.
echo pip更新完成!
echo.

:: pause命令用于暂停批处理文件的执行，并显示一条消息“请按任意键继续. . .”。
pause


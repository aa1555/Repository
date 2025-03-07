:: python -m pip list --outdated 列出所有可更新的库(此命令需要联网，请耐心等待)

:: 关闭命令回显,这里用“::”注释掉关闭命令回显命令，这样命令就会回显。需要关闭命令回显时只需把“::”删掉即可。

@echo off 
:: 将控制台切换为 UTF-8 编码模式
chcp 65001 > nul
cls

::切换目录，使命令在特定目录下执行。
cd /d C:\Users\aa155

echo 正在获取可更新的Python库列表,时间稍长，请耐心等待...
echo.

:: 执行命令
python -m pip list --outdated
echo.

echo 库列表检查已完成！
echo ==============================
echo 注意：上方列表显示的是所有可更新的库
echo 若要实际更新，请使用 pip install -U 包名
echo.

:: pause命令用于暂停批处理文件的执行，并显示一条消息“请按任意键继续. . .”。
pause
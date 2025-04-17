:: 说明：将单个py文件打包成单个exe可执行文件。
:: 说明：将本文件和Python文件放在一起，打包完成后会在当前文件夹生成一个dist文件夹，exe可执行文件就在此。

@echo off
chcp 65001 >nul

echo 请直接输入要打包的Python文件名（例如：script.py）：
echo.

set /p python_file=pyinstaller --onefile --windowed 

rem 执行PyInstaller打包命令
pyinstaller --onefile --windowed %python_file%

echo.
echo 打包完成！
echo.

pause

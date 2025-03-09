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

@echo off
chcp 65001 >nul

REM 提示输入虚拟环境安装的目标路径，例如：E:\Python\测试项目
set /p INSTALL_PATH=请输入虚拟环境安装的目标路径（如E:\下载）： 

REM 检查目标路径是否存在
if not exist "%INSTALL_PATH%" (
    echo 目标路径不存在，请先确认路径是否正确。
    pause
    exit /b
)

REM 提示输入虚拟环境名称
set /p ENV_NAME=请输入虚拟环境名称（如venv）： 

REM 拼接完整的虚拟环境路径
set "FULL_PATH=%INSTALL_PATH%\%ENV_NAME%"

REM 使用默认的python命令创建虚拟环境
python -m venv "%FULL_PATH%"

if %errorlevel% equ 0 (
    echo 虚拟环境已成功创建在 %FULL_PATH%
) else (
    echo 创建虚拟环境时出错，请检查 Python 是否正确安装或其他问题。
)

pause

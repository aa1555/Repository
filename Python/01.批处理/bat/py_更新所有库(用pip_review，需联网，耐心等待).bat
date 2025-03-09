@echo off

:: 切换目录，使命令在特定目录下执行
cd /d C:\Users\aa155

:: 显示进度提示
echo 正在检查可更新的库，时间稍长，请耐心等待...
echo.

:: 执行更新操作（需联网）
pip-review --interactive

echo.
echo 更新完成!
echo.

pause
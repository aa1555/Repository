@echo off


::�л�Ŀ¼��ʹ�������ض�Ŀ¼��ִ�С�
cd /d C:\Users\aa155

echo ��ֱ������������а�װ�⣺
echo.

:: ��ȡ�û�����
set /p library=python -m pip install 

::ִ�������%library%��Ϊ��ȡ���û�����
python -m pip install %library%

echo.
echo ��װ���!
echo.

:: pause����������ͣ�������ļ���ִ�У�����ʾһ����Ϣ���밴���������. . .����
pause

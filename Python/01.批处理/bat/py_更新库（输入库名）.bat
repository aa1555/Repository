@echo off

::�л�Ŀ¼��ʹ�������ض�Ŀ¼��ִ�С�
cd /d C:\Users\aa155

echo ��ֱ������������и��¿⣺
echo.

:: ��ȡ�û�����
set /p library=python -m pip install --upgrade 

::ִ�������%library%��Ϊ��ȡ���û�����
python -m pip install --upgrade %library%

echo.
echo �������!
echo.

:: pause����������ͣ�������ļ���ִ�У�����ʾһ����Ϣ���밴���������. . .����
pause

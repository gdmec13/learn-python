@echo off
echo "��ʼִ��"
:: timeout /t 30 /nobreak > NUl
for /l %%i in (12,-1,0) do (
cls
echo.
echo.
echo.
echo. ����ʱ��%%i�� �Զ���װ�����������
ping 127.1 -n 2 >nul
)
PAUSE
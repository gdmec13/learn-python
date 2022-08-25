@echo off
echo "开始执行"
:: timeout /t 30 /nobreak > NUl
for /l %%i in (12,-1,0) do (
cls
echo.
echo.
echo.
echo. 倒计时数%%i后 自动安装完毕启动。。
ping 127.1 -n 2 >nul
)
PAUSE
@echo off
:: �Թ���Ա�������
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
net stop mongodb
net start mongodb
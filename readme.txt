#make .exe file
pyinstaller -F -w main.py
#--------------
#make exe with icon if u want without delete --icon
pyinstaller --onefile --windowed --icon=ssr2.ico main.py
pyinstaller --onefile --key=CHOS_SSR_SECRET! --windowed --icon=ssr2.ico main.py
pyinstaller --onedir --windowed --icon=ssr2.ico main.py

#----- записать пакеты
pip freeze > requirements.txt
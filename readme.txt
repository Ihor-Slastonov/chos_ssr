#make .exe file
pyinstaller -F -w main.py
#--------------
#make exe with icon if u want without delete --icon
pyinstaller --onefile --windowed --icon=ssr1.ico main.py
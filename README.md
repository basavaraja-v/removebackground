1. python3.9 -m venv rmbg_venv
2. source rmbg_venv/bin/activate 
3. py2applet --make-setup app.py
4. python setup.py py2app
5. dist/RemoveBackground.app/Contents/MacOS/RemoveBackground
6. pyinstaller --noconfirm --onedir --windowed --add-data "c:\users\basavaraj\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter/" --icon=icon.png --name=RemoveBackground" app.py

# Example:
(https://github.com/royaldevops/removebackground/blob/main/assets/0.png)

1. python3.9 -m venv rmbg_venv
2. source rmbg_venv/bin/activate 
3. py2applet --make-setup app.py
4. python setup.py py2app
5. dist/RemoveBackground.app/Contents/MacOS/RemoveBackground
# For windows
1. https://www.youtube.com/watch?v=p3tSLatmGvU&t=803s
2. pyinstaller --noconfirm --onedir --windowed --add-data="c:\users\basavaraj\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter/ --add-data="C:\Users\USERNAME\.u2net\u2net.onnx;." --icon=icon.png --name=RemoveBackground" app.py

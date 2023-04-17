# Example:
<img src="https://github.com/royaldevops/removebackground/blob/main/assets/0.png"/>
# How To Use
```
1. python3.9 -m venv rmbg_venv
2. pip install -r requirements.txt
3. source rmbg_venv/bin/activate 
4. python app.py
```
# How To Package For windows
1. [Youtube tutorial](https://www.youtube.com/watch?v=p3tSLatmGvU&t=803s)
2. pyinstaller --noconfirm --onedir --windowed --add-data="c:\users\basavaraj\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter/ --add-data="C:\Users\USERNAME\.u2net\u2net.onnx;." --icon=icon.png --name=RemoveBackground" app.py

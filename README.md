# Сборка проекта

## Windows сборка

Чтобы собрать проект, понадобиться создать и зайти в локальное пространство env

```bash
python3 -m venv packenv
call packenv\scripts\activate.bat
pip3 install PyQt6 PyInstaller
```

По итогу в консоле должно быть что-то подобное:

(packenv) C:\>

Далее через pyinstaller собираем проект

```
pyinstaller --onefile --windowed src/app.py
```

Итоговый файл будет лежать в папке ./dist/app.exe

## Linux сборка

Чтобы собрать проект, понадобиться также создать и зайти в локальное пространство env

```bash
python3 -m venv packenv
source packenv/bin/activate
pip3 install PyQt6 PyInstaller
```

По итогу в консоле должно быть что-то подобное:

(packenv) username@hostname:~/foldername$

Далее через pyinstaller собираем проект

```
pyinstaller --onefile --windowed src/app.py
```

Итоговый файл будет лежать в папке ./dist/app

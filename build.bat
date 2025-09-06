python -m PyInstaller --icon=src/assets/icon.ico --noconsole src/main.py
xcopy "src\assets" "dist\main\assets" /E /I /H /Y /C
move "dist\main\main.exe" "dist\main\ocs2config.exe"
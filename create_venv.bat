@ECHO OFF
setlocal
set PATH=C:\Python37;C:\Python37\Scripts;%path%

python -m venv venv
call venv\Scripts\activate
python -m pip install -r .\requirements.txt 
call venv\Scripts\deactivate

endlocal

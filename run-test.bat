@ECHO OFF
setlocal
set PATH=C:\Python37;C:\Python37\Scripts;%path%

call venv\Scripts\activate
pytest
call venv\Scripts\deactivate

endlocal

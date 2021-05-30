@ECHO OFF
setlocal
set PATH=C:\Python37;C:\Python37\Scripts;%path%

call venv\Scripts\activate
python ./bin_tree_view.py
call venv\Scripts\deactivate

endlocal

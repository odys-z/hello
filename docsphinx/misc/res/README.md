# Error Report

## Usage

.. excel-table::
   :file: res/xmpp-survey.xlsm

## CLI Error

```
Exception occurred:
  File "/home/ody/.local/lib/python3.9/site-packages/openpyxl/worksheet/worksheet.py", line 293, in __getitem__
    raise IndexError("{0} is not a valid coordinate or range".format(key))
IndexError: 0 is not a valid coordinate or range
The full traceback has been saved in /tmp/sphinx-err-cwgkwmz5.log, if you want to report the issue to the developers.
Please also report this if it was a user error, so that a better error message can be provided next time.
A bug report can be filed in the tracker at <https://github.com/sphinx-doc/sphinx/issues>. Thanks!
Makefile:46: recipe for target 'html' failed
make[1]: *** [html] Error 2
make[1]: Leaving directory '/home/ody/git/hello/docsphinx'
Makefile:32: recipe for target 'ghpage' failed
make: *** [ghpage] Error 2
```

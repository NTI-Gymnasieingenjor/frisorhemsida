@echo off

curl.exe -F output=gnu -F "text=<../style.css" https://jigsaw.w3.org/css-validator/validator
curl.exe -F asciiquotes=yes -F out=gnu -F "content=<../index.html" https://validator.nu/

pause
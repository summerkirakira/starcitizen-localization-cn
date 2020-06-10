# StarCitizenModding

English

Star Citizen game modding

System requirements
1. git (optional)
2. Python 3.8: https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe

How setup modding environvement:
1. Inside "...\StarCitizen\LIVE" folder create git repository and checkout all sources from master branch or download latest release archive (https://github.com/defterai/StarCitizenModding/releases)
2. Run modding-begin.py python script to patch "StarCitizen.exe". To restore original version run modding-end.py

Also you can use following applications to install modding environvement:
* https://github.com/h0useRus/StarCitizen
* https://github.com/Shin0by/StarCitizen-Helper

Russian

Модификация игры Star Star Citizen

Требования к системе:
1. Установлен git (опционально)
2. Установлен Python 3.8: https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe

Как настроить среду модификации:
1. Внутри "...\StarCitizen\LIVE" папки создайте git репозиторий и выкачайте все ресурсы с основной "master" ветки разработки или скачайте архив с последним релизом (https://github.com/defterai/StarCitizenModding/releases) и скопируйте в LIVE все с папки верхнего уровня (внутри LIVE должны оказатся папка data и скрипты питона)
2. Запустите modding-begin.py питон скрипт для модификации игрового клиента "StarCitizen.exe". Чтобы востановить оригинальную версию клиента запустите modding-end.py

Также вы можете использовать следующие приложения для установки среды модификации:
* https://github.com/h0useRus/StarCitizen
* https://github.com/Shin0by/StarCitizen-Helper

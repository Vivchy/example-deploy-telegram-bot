# Деплой телеграм бота на сервер

***

Далее _project_ - название проета

## 1. Создать requirements.txt

В корне проекта создать файл зависимостей 

<pre>pip freeze > requirements.txt </pre>

***

## 2. Установить python и  pip на сервер

<pre>sudo apt update

sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

Press [ENTER] to continue or Ctrl-c to cancel adding it.

sudo apt install python3.8 </pre>

Проверить версию 

<pre>python3.8 --version</pre>

Установить pip и virtualenv

<pre>python3.8 -m pip install --upgrade pip

pip --version

pip install virtualenv</pre>

***

## 3. Перенести проект на сервер

1. при помощи git clone  на сервер
2. по ftp

***

## 4. Проверить работу бота (доустановка)

1. Перейти в каталог проекта
2. Прописать доступ к токену 
   1. Создать файл auth_data.py и прописать переменную token
   2. Добавить token в <i>nano /etc/environment</i> <pre>proj_token="токен"</pre>
      1. В конфигурации
      2. TOKEN = os.environ.get("proj_token")
3. Создать venv
   <pre>
   cd project
   
   virtualenv venv
   
   source venv/bin/activate
   </pre>
4. Установить зависимости

    <pre>
    pip install -r requirements.txt
   
    python main.py
    </pre>
Проверить работу

остановить venv 
<pre>
deactivate </pre>
***

## По необходимости установить redis
<pre>
sudo apt install redis-server

redis-cli

127.0.0.1:6379> ping

</pre>

***

### Создать собственную службу для беспрерывной работы бота

<pre>
sudo nano /lib/systemd/system/project.service
</pre>

Прописать в файле

<pre>
[Unit]
Description= description project
After=network.target

[Service]
EnvironmentFile=/etc/environment
ExecStart=/home/project/venv/bin/python main.py
ExecReload=/home/project/venv/bin/python main.py
WorkingDirectory=/home/project/
KillMode=process
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
</pre>

### Запуск 
<pre>
    sudo systemctl enable project
    sudo systemctl start project
</pre>

При обновлении проекта systemctl нужно перезапускать

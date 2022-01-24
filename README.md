# About

Вы должны взглянуть на пакет systemd . Его можно использовать для управления статусом вашего скрипта. Он может перезапустить скрипт, если он умирает или если узел перезагружается.

Вот пример сервиса.

Создайте файл ниже в этом месте: `/lib/systemd/system/example.service`


```
[Unit]
Description=A short description of the script.

[Service]
Type=simple
# Script location
ExecStart=/usr/bin/python path/to/your/python_demo_service.py
# Restart the script in all circumstances (e.g If it exits successfully, fails or crashes).
Restart=always

[Install]
WantedBy=multi-user.target
```

Затем установите службу для автоматического запуска при загрузке и запустите службу:


```
chmod 644 /lib/systemd/system/example.service
systemctl enable example
systemctl start example 

systemctl status example
```


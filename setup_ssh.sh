#!/bin/bash

# Установка SSH-сервера
sudo apt install -y openssh-server

# Создание ключа SSH 
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa

# Копирование ключа на сервер (или в authorized_keys, если на локальной машине)
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Установка правильных прав доступа
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

echo "SSH настроен. Теперь можно подключаться без пароля."

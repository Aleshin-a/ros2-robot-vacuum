#!/bin/bash

# Обновление списка пакетов
sudo apt update

# Установка ROS 2 Humble
sudo apt install -y ros-humble-desktop

# Установка Python-пакетов
sudo apt install -y python3-pip
pip3 install numpy  # Пример Python-зависимости

# Установка дополнительных утилит
sudo apt install -y python3-vcstool python3-colcon-common-extensions git

# Создание и инициализация ROS Workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon_cd_cache_path="$(pwd)/.colcon_cd_cache"
source /opt/ros/humble/setup.bash
colcon build

echo "Установка завершена. Не забудьте source ~/ros2_ws/install/setup.bash"

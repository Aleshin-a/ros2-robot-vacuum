FROM ubuntu:22.04

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    openssh-server \
    python3-pip \
    python3-vcstool \
    python3-colcon-common-extensions \
    git \
    ros-humble-rviz2 \
    ros-humble-usb-cam # For webcam

# Настройка ROS 2
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

ENV ROS_DISTRO humble  #Замените при необходимости

RUN apt-get update && apt-get install -y ros-${ROS_DISTRO}-desktop

# Создание ROS Workspace
RUN mkdir -p /root/ros2_ws/src
WORKDIR /root/ros2_ws

# Копирование скриптов
COPY install.sh ./
COPY setup_ssh.sh ./
RUN chmod +x ./*.sh

# Настройка SSH
RUN ./setup_ssh.sh

# Копирование пакета ROS
COPY src ./src

COPY robot.launch.py ./

# Сборка ROS Workspace
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon build

# Настройка окружения для запуска ROS
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc
RUN echo "source /root/ros2_ws/install/setup.bash" >> /root/.bashrc

EXPOSE 22
CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D && bash"]
# CMD ["ros2", "launch", "my_robot_vacuum", "robot.launch.py", "rviz:=True"] #Пример автозапуска, если RVIZ нужен

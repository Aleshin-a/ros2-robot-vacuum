# ros2-robot-vacuum

## Описание

Этот проект представляет собой базовую систему управления для робота-пылесоса, разработанную с использованием ROS 2. Проект включает узлы для сбора данных с ультразвукового датчика и датчика заряда батареи, а также возможность визуализации данных с помощью RViz.

## Аппаратное обеспечение

*   **Вычислитель:** Raspberry Pi 4 (или аналогичный компьютер с Linux).
*   **Датчик расстояния:** Ультразвуковой датчик HC-SR04.
*   **Датчик заряда батареи:** (Описание типа датчика).
*   **Веб-камера:** (Опционально, для визуальной демонстрации).

## Схема подключения
[Ультразвуковой датчик] –GPIO–> [Raspberry Pi 4] [Датчик заряда батареи] –GPIO/ADC–> [Raspberry Pi 4] [Веб-камера ноутбука] –USB–> [Ноутбук (разработка)]


## Инструкции по установке

1.  **Установите Ubuntu 22.04:**

    ```
    (Инструкции по установке Ubuntu, или ссылка на официальную документацию)
    ```

2.  **Установите ROS 2 Humble:**

    ```
    (Инструкции по установке ROS 2, или ссылка на официальную документацию: https://docs.ros.org/en/humble/Installation.html)
    ```

3.  **Склонируйте репозиторий:**

    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone <your_repository_url> my_robot_vacuum
    ```

4.  **Установите зависимости:**

    ```bash
    cd ~/ros2_ws
    chmod +x install.sh
    ./install.sh
    ```

5.  **Настройте SSH (опционально):**

    ```bash
    chmod +x setup_ssh.sh
    ./setup_ssh.sh
    ```

## Инструкции по запуску

1.  **Соберите пакет:**

    ```bash
    cd ~/ros2_ws
    colcon build
    ```

2.  **Активируйте окружение:**

    ```bash
    source install/setup.bash
    ```

3.  **Запустите launch-файл:**

    ```bash
    ros2 launch my_robot_vacuum robot.launch.py rviz:=True
    ```

    Это запустит узлы `ultrasonic_sensor_node` и `battery_sensor_node`, а также RViz с предварительно настроенной конфигурацией.

## Инструкции по Docker

1.  **Установите Docker:**

    ```
    (Инструкции по установке Docker, или ссылка на официальную документацию)
    ```

2.  **Соберите Docker-образ:**

    ```bash
    cd ~/ros2_ws
    docker build -t my_robot_vacuum_image .
    ```

3.  **Запустите Docker-контейнер:**

    ```bash
    docker run -it --network=host my_robot_vacuum_image
    ```

4.  **Активируйте окружение внутри контейнера:**

    ```bash
    source /root/.bashrc
    ```

5.  **Запустите launch-файл:**

    ```bash
    ros2 launch my_robot_vacuum robot.launch.py rviz:=True
    ```

## Датчики и топики

*   **Ультразвуковой датчик:**
    *   Топик: `/ultrasonic_distance`
    *   Тип сообщения: `std_msgs/Float32`

*   **Датчик заряда батареи:**
    *   Топик: `/battery_level`
    *   Тип сообщения: `std_msgs/Float32`

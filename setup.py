from setuptools import setup
import os
from glob import glob


package_name = 'my_robot_vacuum'


setup(
   name=package_name,
   version='0.0.0',
   packages=[package_name],
   data_files=[
       ('share/ament_index/resource_index/packages',
           ['resource/' + package_name]),
       ('share/' + package_name, ['package.xml']),
       (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')), # Добавляем launch-файлы
       (os.path.join('share', package_name, 'rviz'), glob('rviz/*'))
   ],
   install_requires=['setuptools'],
   zip_safe=True,
   maintainer='aleshin23', 
   maintainer_email= 'aleshin23@example.com',
   description='...',
   license='...',
   tests_require=['pytest'],
   entry_points={
       'console_scripts': [
           'ultrasonic_sensor = my_robot_vacuum.ultrasonic_sensor:main',  # Указываем точку входа
           'battery_sensor = my_robot_vacuum.battery_sensor:main',    # Указываем точку входа
       ],
   },
)


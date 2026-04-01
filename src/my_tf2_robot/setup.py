import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_tf2_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='claw',
    maintainer_email='claw@example.com',
    description='tf2で「ちゃんとしたロボ座標系」を作る学習用パッケージ',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf2_robot_publisher = my_tf2_robot.tf2_robot_publisher:main',
        ],
    },
)

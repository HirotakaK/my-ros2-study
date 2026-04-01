from setuptools import find_packages, setup

package_name = 'my_first_scan'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/scan_foxglove.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2-study',
    maintainer_email='study@example.com',
    description='疑似LaserScanのパブリッシュとRViz2可視化の学習パッケージ',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scan_publisher = my_first_scan.scan_publisher:main',
        ],
    },
)

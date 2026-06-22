import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'img_data_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'images'), glob('images/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rokey',
    maintainer_email='hyunjp03@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'image_publisher = img_data_pkg.2_0_a_image_publisher:main',
            'image_subscriber = img_data_pkg.2_0_b_image_subscriber:main',
            'data_publisher = img_data_pkg.2_0_c_data_publisher:main',
            'data_subscriber = img_data_pkg.2_0_d_data_subscriber:main',
            # 'capture_photo = img_data_pkg.capture_photo:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'data_preprocessing_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'create_data_dirs = data_preprocessing_pkg.create_data_dirs:main',
            'move_image = data_preprocessing_pkg.move_image:main',
            'move_labels = data_preprocessing_pkg.move_labels:main',
        ],
    },
)

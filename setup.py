from setuptools import setup, find_packages

setup(
    name='flask-real-time-map',
    version='0.1.0',

    license='MIT',
    url='https://github.com/hedderich/flask-real-time-map',
    author='Marvin Hedderich',
    author_email='dev@hedderich.info',
    description='Display a live visualization of vehicle position data',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-socketio',
        'gevent',
        'gevent-websocket',
        'haversine'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

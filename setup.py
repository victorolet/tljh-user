from setuptools import setup

setup(
    name="tljh-user",
    author="victorolet",
    version="0.1",
    license="3-clause BSD",
    url='https://github.com/victorolet/tljh-user',
    entry_points={"tljh": ["simple = tljh_user"]},
    py_modules=["tljh_user"],
)
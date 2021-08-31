from setuptools import setup ,find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ImData',
    version='0,0,0',
    description='image dataset creation tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Noureddine Ait Hellal',
    author_email='nnicknamename@gmail.coom',
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['cv2','PyQt5'],
)

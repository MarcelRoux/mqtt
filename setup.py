from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(name='mqtt',
      version='0.0.1',
      description='An MQTT interface.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MarcelRoux/mqtt',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      author='Marcel',
      author_email='',
      license='MIT',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      python_requires='>=3.6'
)

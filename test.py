from setuptools import find_packages


def main():
    print(find_packages(where='src'))
    print(find_packages(where='.'))


if __name__ == '__main__':
    main()

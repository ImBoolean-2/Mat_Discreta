def install_dependencies():
    import pkg_resources
    import subprocess
    import sys
    import os

    os.system('cls' if os.name == 'nt' else 'clear')

    def install(package):
        try:
            dist = pkg_resources.get_distribution(package)
            print('{} ({}) está instalado'.format(dist.key, dist.version))
        except pkg_resources.DistributionNotFound:
            print('{} NO está instalado. Instalación en curso...'.format(package))
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    dependencies = ['pillow', 'matplotlib']

    for package in dependencies:
        install(package)

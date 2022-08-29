import subprocess




def runner():
    subprocess.run("behave src/test/resources/features/feature.feature", shell=True)


runner()
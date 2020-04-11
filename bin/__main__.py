# this is the one piece of code that should be made into an executable
# $ pp install auto-py-to-exe
# $ auto-py-to-exe
#
# rename to __main__.py
# python -m exec

from RoboticsCV.app import main

if __name__ == '__main__':
    main()

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import AutoTeacherApp

if __name__ == "__main__":
    app = AutoTeacherApp()
    app.run()

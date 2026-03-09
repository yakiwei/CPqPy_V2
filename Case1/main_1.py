import os
import shutil
from comsol_1 import comsol_first_step
from phreeqc_1 import phreeqc_first_step
def main_1():
    project_dir = r"D:\Pycharm\CPqPy/case1\Result"
    mph_file = r"D:\Pycharm\CPqPy/case1\Case1_first.mph"
    comsol_first_step(mph_file)
    comsol_outcon_path = os.path.join(project_dir, f"outcon.txt")
    outcon_copy_path = os.path.join(project_dir, f"outcon720.txt")
    shutil.copy(comsol_outcon_path, outcon_copy_path)
    phreeqc_first_step()
if __name__ == "__main__":
    main_1()
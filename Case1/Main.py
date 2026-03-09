import os
import sys
import shutil
import time
from main_1 import main_1
from comsol_2 import comsol_next_step
from phreeqc_2 import phreeqc_next_step

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

path = os.path.abspath(os.path.dirname(__file__))
sys.stdout = Logger('runlog.txt')

def main_2():

    start_time = time.time()
    
    timestep = int(0.01 * 72000)
    total_steps = 100
    project_dir = r"D:\Pycharm\CPqPy/case1\Results"
    mph_file = r"D:\Pycharm\CPqPy/case1\Case1_second.mph"

    print(" Calculation of the initialization time step ")
    main_1()

    print(" Iterative coupling for Subsequent time steps ")
    for step in range(2, total_steps + 1):
        comsol_outcon_path = os.path.join(project_dir, f"outcon_2.txt")
        outcon_copy_path = os.path.join(project_dir, f"outcon{timestep * step}.txt")

        comsol_next_step(mph_file)
        shutil.copy(comsol_outcon_path, outcon_copy_path)


        if step == 2:
            prev_result_path = r'D:\Pycharm\CPqPy/case1\Results\11111111.txt'
        else:
            prev_result_path = r'D:\Pycharm\CPqPy/case1\Results\phresult.txt'
        print(f"PHREEQC uses the previous step result file: {prev_result_path}")
        phreeqc_next_step(prev_result_path)

        phreeqc_initcon_path = os.path.join(project_dir, f"initcon{timestep * step}.txt")
        shutil.copy(os.path.join(project_dir, "infile.txt"), phreeqc_initcon_path)

    print(" All time step calculations are complete! ")
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f" Total calculation time: {total_time/60:.2f} minutes")

if __name__ == "__main__":
    main_2()
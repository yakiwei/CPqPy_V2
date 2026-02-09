def main_1():
    from comsol_1 import comsol_first_step
    from phreeqc_1 import phreeqc_first_step

    mph_file = r"D:\Pycharm\CPqPy/case2\pesti_initial_new.mph"
    comsol_first_step(mph_file)
    phreeqc_first_step()
if __name__ == "__main__":
    main_1()
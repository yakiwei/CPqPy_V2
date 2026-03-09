def phreeqc_next_step(prev_result_path):
    import numpy as np
    import os
    from phreeqc import Phreeqc


    datpath = r"D:\Pycharm\CPqPy/case1\PHREEQC"

    def selected_array(db_path, input_string):
        p = Phreeqc()
        p.set_output_string_on(True)
        error_count = p.load_database(db_path)
        if error_count != 0:
            raise RuntimeError(f"Failed to load database: {db_path}")

        error_count = p.run_string(input_string)
        if error_count != 0:
            raise RuntimeError("Failed to run input string")

        return p.get_selected_output()


    infile_path = r'D:\Pycharm\CPqPy/case1\Results\outcon_2.txt'
    infile = np.loadtxt(infile_path, comments='%', delimiter=None)
    print(infile.shape)


    m = infile.shape[0]

    n = infile.shape[1] - 1

    outn = 6

    if prev_result_path and os.path.exists(prev_result_path):
        phresult = np.loadtxt(prev_result_path)
    else:
        phresult = np.loadtxt('D:\Pycharm\CPqPy/case1\Results/11111111.txt')

    input_string20 = """   """
    for i in range(0, m):
        input_string2 = """
            SOLUTION 0  CaCl2 
                    units            mmol/kgw 
                    temp             25.0
                    pH               #     charge 
                    pe               #    O2(g)   -0.68 
                    Ca               # 
                    Cl               #
                    Na               # 
                    K                # 

            SOLUTION # Initial solution for column 
                    units            mmol/kgw 
                    temp             25.0
                    pH               *     charge 
                    pe               *    O2(g)   -0.68 
                    Ca               *
                    Cl               *
                    Na               *
                    K                *


            EXCHANGE #
                    -equilibrate #
                    X                0.0011 
                    
            SELECTED_OUTPUT 1
                -high_precision       true
                -reset                false
                -solution             false
                -time                 false
                -pH                   true
                -pe                   true
                -totals               Ca Cl  K  Na  
                -active               true

            END
                    """

        for j in range(1, 5):
            if infile[i, j] < 0:
                infile[i, j] = 0

        incr = str(round(phresult[i, 0], 5))
        str1 = 'pH               '
        incr = str1 + incr
        input_string21 = input_string2.replace('pH               #', incr)  # 使用前一个步长的ph

        incr = str(round(phresult[i, 1], 5))
        str1 = 'pe               '
        incr = str1 + incr
        input_string22 = input_string21.replace('pe               #', incr)

        # modify Ca
        incr = str(round(infile[i, 1], 15))
        str1 = 'Ca               '
        incr = str1 + incr
        input_string23 = input_string22.replace('Ca               #', incr)

        # modify Cl
        incr = str(round(infile[i, 2], 10))
        str1 = 'Cl               '
        incr = str1 + incr
        input_string24 = input_string23.replace('Cl               #', incr)

        # modify K
        incr = str(round(infile[i, 3], 10))
        str1 = 'K                '
        incr = str1 + incr
        input_string25 = input_string24.replace('K                #', incr)

        # modify Na
        incr = str(round(infile[i, 4], 10))
        str1 = 'Na               '
        incr = str1 + incr
        input_string26 = input_string25.replace('Na               #', incr)

        # 修改第二初始溶液

        incr = str(round(phresult[i, 0], 5))
        str1 = 'pH               '
        incr = str1 + incr
        input_string27 = input_string26.replace('pH               *', incr)  # 使用前一个步长的ph

        incr = str(round(phresult[i, 1], 5))
        str1 = 'pe               '
        incr = str1 + incr
        input_string28 = input_string27.replace('pe               *', incr)

        # modify Ca
        incr = str(round(phresult[i, 2] * 1000, 15))
        str1 = 'Ca               '
        incr = str1 + incr
        input_string29 = input_string28.replace('Ca               *', incr)

        # modify Cl
        incr = str(round(phresult[i, 3] * 1000, 10))
        str1 = 'Cl               '
        incr = str1 + incr
        input_string291 = input_string29.replace('Cl               *', incr)

        # modify K
        incr = str(round(phresult[i, 4] * 1000, 10))
        str1 = 'K                '
        incr = str1 + incr
        input_string292 = input_string291.replace('K                *', incr)

        # modify Na
        incr = str(round(phresult[i, 5] * 1000, 10))
        str1 = 'Na               '
        incr = str1 + incr
        input_string293 = input_string292.replace('Na               *', incr)

        incr = str(i + 1)
        str1 = 'SOLUTION '
        incr = str1 + incr
        input_string294 = input_string293.replace('SOLUTION #', incr)

        incr = str(i + 1)
        str1 = 'EXCHANGE '
        incr = str1 + incr
        input_string295 = input_string294.replace('EXCHANGE #', incr)

        incr = str(i + 1)
        str1 = '-equilibrate  '
        incr = str1 + incr
        input_string296 = input_string295.replace('-equilibrate #', incr)

        input_string20 = input_string20 + input_string296

    input_string = input_string20
    print(input_string)

    phreeqc_result = selected_array(os.path.join(datpath, 'phreeqc.dat'), input_string)

    print(phreeqc_result)

    species_list = list(phreeqc_result.keys())  # ['Ca(mol/kgw)', 'Cl(mol/kgw)', 'K(mol/kgw)', 'Na(mol/kgw)']
    print(species_list)

    for jj in range(outn):
        species = species_list[jj]
        values = phreeqc_result[species]
        for zz in range(m):
            phresult[zz, jj] = float(values[zz * 4 + 3])

    np.savetxt('D:\Pycharm\CPqPy/case1\Results/phresult.txt', phresult)

    for i in range(0, m):
        for k in range(0, n):
            infile[i, 1 + k] = phresult[i, 2 + k] * 1000
    np.savetxt('D:\Pycharm\CPqPy/case1\Results/infile.txt', infile)
    return

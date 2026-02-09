def phreeqc_next_step():
    import numpy as np
    import os
    from phreeqc import Phreeqc

    datpath = r"D:\Pycharm\CPqPy/case2"

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

    infile_path = r'D:\Pycharm\CPqPy/case2\Results\out_2.txt'
    infile = np.loadtxt(infile_path, comments='%', delimiter=None)
    print(infile.shape)

    timestep = int(0.01 * 864000)

    m = infile.shape[0]

    n = infile.shape[1] - 4

    outn = 10
    phresult = np.zeros((m, outn))


    input_string10 = """   """
    for i in range(0, m):
        input_string1 = """
                SOLUTION #
                    temp      25
                    pH        # charge
                    pe        #
                    redox     pe
                    units     mmol/kgw
                    density   1
                    water     ###
                    A         ###
                    Asn         ###
                    Asx         ###
                    """

        ph = 7
        pe = 4

        for j in range(4, 7):
            if infile[i, j] < 0:
                infile[i, j] = 0

        incr = str(round(ph, 5))
        str1 = 'pH        '
        incr = str1 + incr
        input_string11 = input_string1.replace('pH        #', incr)

        incr = str(round(pe, 5))
        str1 = 'pe        '
        incr = str1 + incr
        input_string12 = input_string11.replace('pe        #', incr)

        # modify A
        incr = str(round(infile[i, 4], 15))
        str1 = 'A        '
        incr = str1 + incr
        input_string13 = input_string12.replace('A         ###', incr)

        # modify B
        incr = str(round(infile[i, 5], 10))
        str1 = 'Asn        '
        incr = str1 + incr
        input_string14 = input_string13.replace('Asn         ###', incr)

        # modify C
        incr = str(round(infile[i, 6], 10))
        str1 = 'Asx        '
        incr = str1 + incr
        input_string15 = input_string14.replace('Asx         ###', incr)

        # modify water
        incr = str(round(infile[i, 3], 10))
        str1 = 'water     '
        incr = str1 + incr
        input_string16 = input_string15.replace('water     ###', incr)

        incr = str(i + 1)
        str1 = 'SOLUTION '
        incr = str1 + incr
        input_string17 = input_string16.replace('SOLUTION #', incr)
        input_string10 = input_string10 + input_string17

    input_string2 = """
            KINETICS #
            R_1
                -formula  A  -1 Asx  1
                -m        100
                -m0       100
                -tol      1e-10
            R_2
                -formula  Asn  1 Asx  -1
                -m        100
                -m0       100
                -tol      1e-10
            R_3
                -formula  A  -1
                -m        100
                -m0       100
                -tol      1e-10
            R_4
                -formula  Asx  -1
                -m        100
                -m0       100
                -tol      1e-10
            R_5
                -formula  Asn  -1
                -m        100
                -m0       100
                -tol      1e-10

            RUN_CELLS
                -cells #
                -time_step    # seconds

            SELECTED_OUTPUT #
                -high_precision       true
                -reset                false
                -solution             true
                -time                 true
                -pH                   true
                -pe                   true
                -water                true
                -charge_balance       true
                -percent_error        true
                -totals               A  Asn  Asx

            End
                """
    # modify knite
    incr = str(m)
    str1 = 'KINETICS 1-'
    incr = str1 + incr
    input_string21 = input_string2.replace('KINETICS #', incr)

    # modify cells

    incr = str(m)
    str1 = '-cells 1-'
    incr = str1 + incr
    input_string22 = input_string21.replace('-cells #', incr)

    # modify timesteps
    incr = str(timestep)
    str1 = '-time_step    '
    incr = str1 + incr
    input_string23 = input_string22.replace('-time_step    #', incr)

    # modify out
    incr = str(m)
    str1 = 'SELECTED_OUTPUT 1-'
    incr = str1 + incr
    input_string24 = input_string23.replace('SELECTED_OUTPUT #', incr)

    input_string = input_string10 + input_string24
    print(input_string)

    phreeqc_result = selected_array(os.path.join(datpath, 'pesti.dat'), input_string)

    print(phreeqc_result)

    species_list = list(phreeqc_result.keys())  # ['Ca(mol/kgw)', 'Cl(mol/kgw)', 'K(mol/kgw)', 'Na(mol/kgw)']

    for jj in range(outn):
        species = species_list[jj]
        values = phreeqc_result[species]
        for zz in range(m + 1, m + m + 1):
            phresult[zz - m - 1, jj] = float(values[zz])
    np.savetxt('D:\Pycharm\CPqPy/case2\Results/result.txt', phresult)

    for i in range(0, m):
        for k in range(0, n):
            infile[i, 4 + k] = phresult[i, 7 + k] * 1000
    np.savetxt('D:\Pycharm\CPqPy/case2\Results/infile.txt', infile, fmt='%.15f')
    return


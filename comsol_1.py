def comsol_first_step(mph_file):
    import mph
    import os
    
    mph_file = os.path.abspath(mph_file)
    client = mph.start()
    model = client.load(mph_file)
    model.solve()
    model.export()
    client.remove(model)
    return

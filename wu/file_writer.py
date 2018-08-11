def write_txt(filename, temporal_units):
    f = open(("output/%s.txt" % filename), "w")
    for k in sorted(temporal_units.keys()):
        unit = temporal_units.get(k)
        for line in unit.get_lines():
            f.write(line + "\n")

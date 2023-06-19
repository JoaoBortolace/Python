import matplotlib.pyplot as plt
import numpy as np

file_name = input("Nome do arquivo sem extenção:\n")
with open(f"{file_name}.mif", "w") as file:
    file.write("WIDTH=8;\n")
    file.write("DEPTH=147456;\n")
    file.write("\n")
    file.write("ADDRESS_RADIX=UNS;\n")
    file.write("DATA_RADIX=BIN;\n")
    file.write("\n")
    file.write("CONTENT BEGIN")
    file.write("\n")
    
    idx = 0
    
    for line in plt.imread(f'{file_name}.bmp').astype(np.int16):
        for pixel in line:
            R, G, B = [(val).astype(np.int16) for val in pixel]
            file.write("\t")
            file.write(f"{idx} : ")
            file.write((str(bin(R))[2:]).zfill(8))
            file.write(";\n")
            idx += 1
            file.write("\t")
            file.write(f"{idx} : ")
            file.write((str(bin(G))[2:]).zfill(8))
            file.write(";\n")
            idx += 1
            file.write("\t")
            file.write(f"{idx} : ")
            file.write((str(bin(B))[2:]).zfill(8))
            file.write(";\n")
            idx += 1
    file.write("END;\n")

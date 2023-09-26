#datos = open("datos.txt").read()
#print(f"datos={datos}, tipo de datos={type(datos)}")
#data = [line.strip() for line in open("writefile.txt")]
#print(data)
#f = open("writefile.txt","w")
#print("Esta es mi primera impresión a un archivo",
#      file=f)
#print([[1,2],[3,4]],
#      file=f,end="")
#f.close()
import numpy as np
# Variable = np.genfromtxt("writefile.txt",
#                          skip_header=1,
#                          skip_footer=1,
#                          delimiter=",",
#                          comments="#",
#                          dtype=None, encoding=None)
# print("VAR=",Variable)
# print("TIPO",Variable.dtype)
np.savetxt("numpyFile.txt", np.ones((6,6)),
           fmt=["%.2f","%.1f","%d","%.3f","%.5f","%.3f"]) 
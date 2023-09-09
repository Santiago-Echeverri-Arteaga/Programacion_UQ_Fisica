def main(nombre,*args,g=-9.8,**kwargs):
    print(f"Buenos dias {nombre}, en tu planeta la gravedad vale {g}")
    for i in range(len(args)):
        print(f"La variable {i} vale {args[i]}")
    for key,value in kwargs.items():
        print(f"La variable {key} vale {value}")
    #return(respuesta)

def cuadratica(y_0:float, v_0:float, t:float, a:float=-9.8):
    resultado = y_0+v_0*t+0.5*a*t**2
    return(resultado)

if __name__ == "__main__":
    #variable = cuadratica(3, 10, 1, a=10)
    var=(1,2,3,4,5,6,7,8)
    dic={"pos":1,"masa":3.5,"name":"Hola","conservativo":True,
         "momentum":12}
    #main("Santiago",*var,**dic)
    print((lambda x_0,v_0,t,a=-9.8:x_0 + v_0*t + 0.5*a*t**2 if a!=0 else x_0)(10,2,3,10)) 
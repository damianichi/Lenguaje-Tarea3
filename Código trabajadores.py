import threading
import time

globvar = 0
def analista():
    print "iniciando analista"
    time.sleep(2)
    print "terminando analista"
    return


def disenador():
    print "iniciando diseno"
    time.sleep(1)
    print "terminando diseno"
    return
 

def programador(tiempo):
    print "inicio {}".format(threading.current_thread().getName())
    time.sleep(tiempo)
    print "termino {}".format(threading.current_thread().getName())
    return
def tester(tiempo):
    global globvar
    print "inicio {}".format(threading.current_thread().getName())
    datoinput = raw_input('Escriba "y" para aprobar en caso contrario otra letra: ')
    if datoinput == 'y': 
        globvar = 1
        print "proyecto completo!!"
    else: 
        time.sleep(tiempo)
        print "termino {}".format(threading.current_thread().getName())

     

print "hola"
if __name__=="__main__":

    

    while globvar == 0:
        
        a = threading.Thread(name="analista", target=analista, args=())
        d = threading.Thread(name="diseno", target=disenador, args=())
        
        p1 = threading.Thread(name="programador1", target=programador, args=(3, ))
        p2 = threading.Thread(name="programador2", target=programador, args=(2, ))
        
        t = threading.Thread(name="tester", target=tester, args=(3, ))
        
        a.start()
        d.start()
        
        a.join()
        d.join()
        
        p1.start()
        p2.start()
        p1.join()
        p2.join()
       
        t.start()
        t.join()
        
        
         
    
    

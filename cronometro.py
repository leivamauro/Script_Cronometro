from time import perf_counter

class Crono():
    def __init__(self):
        self.is_running = False
        self.crono_start = 0
        self.crono_start_global = 0
        self.crono_pause = [0, False]
        self.time_in_pause = 0

    def start(self):
        """inicia el cronometro"""
        if not self.is_running:
            if self.crono_start_global == 0:
                self.crono_start_global = perf_counter()
            else:
                self.crono_start = perf_counter()
                self.time_in_pause += (self.crono_start - self.crono_pause[0])
            self.is_running = True
            self.crono_pause[1] = False
        
    def pause(self):
        """pausa el cronometro"""
        if self.is_running and not self.crono_pause[1]:
            self.is_running = False
            self.crono_pause = [perf_counter(), True]
        
    def restart(self):
        """reinicia el cronometro"""
        self.is_running = False
        self.crono_start = 0
        self.crono_start_global = 0
        self.crono_pause = [0, False]
        self.time_in_pause = 0
                
    def get_time(self) -> int:
        """devuelve el tiempo al usuario"""
        if self.is_running:
            run_time = (perf_counter() - self.crono_start_global) - self.time_in_pause
        else:
            run_time = (self.crono_pause[0] - self.crono_start_global) - self.time_in_pause
        return run_time

    def get_is_running(self):
        return self.is_running

if __name__ == "__main__":
    cronometro = Crono()
    while True:
        entrada = input("opcion: ").lower()
        if entrada == "salir":
            break
        elif entrada == "iniciar":
            cronometro.start()
        elif entrada == "pausar":
            cronometro.pause()
        elif entrada == "reiniciar":
            cronometro.restart()
        elif entrada == "tiempo":
            tiempo = cronometro.get_time()
            print("el tiempo es: ", str(tiempo))
        else:
            print("opcion incorrecta")
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
                
    def get_time(self) -> float:
        """devuelve el tiempo al usuario, obtener los milisegundo da mejor presicion"""
        if self.is_running:
            run_time = (perf_counter() - self.crono_start_global) - self.time_in_pause
        else:
            run_time = (self.crono_pause[0] - self.crono_start_global) - self.time_in_pause
        return run_time

    def get_is_running(self) -> bool:
        """muestra si el cronometro esta en funcionamiento o no"""
        return self.is_running

    def get_time_in_HHMMSSms(self) -> str:
        """retorna una string con el tiempo en formato -> 00:00:00.000"""
        crono_time = self.get_time()
        if not crono_time:
            return "00:00:00.000"
        hours = int(crono_time // 3600)
        minutes = int((crono_time % 3600) // 60)
        seconds = int(crono_time % 60)
        miliseconds = crono_time - int(crono_time)
        miliseconds *= 1000
        miliseconds = round(miliseconds)
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:03}"

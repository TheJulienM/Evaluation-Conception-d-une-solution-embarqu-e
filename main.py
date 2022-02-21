import datetime
import time
import threading
from datetime import datetime
from datetime import timedelta
current_time = datetime.now()
n = 2
future_time = current_time + timedelta(minutes=n)

class my_task(threading.Thread):
    name = None
    period = None
    execution_time = None
    priority = None
    oilProducer = None

    ############################################################################
    def __init__(self, name, period, execution_time, priority, oilProducer):

        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.priority = priority
        self.oilProducer = oilProducer

        threading.Thread.__init__(self)

    def produceOil(self):
        global tank

        if(self.name == "Pump 1" and tank + 10 <= 50) :
            tank += 10
            print("Quantity of oil in Tank : " + str(tank))
        elif(self.name == "Pump 2" and tank + 20 <= 50) :
            tank += 20
            print("Quantity of oil in Tank : " + str(tank))
        if (tank >= 30):
            needOil = False


    def consumeOil(self):
        global tank
        global needOil
        if(tank <= 50 ) :
            if(self.name == "Machine 1") :
                tank -= 25
            elif(self.name == "Machine 2") :
                tank -= 5
        if(tank <= 30) :
            needOil = True
        print("Quantity of oil in Tank : " + str(tank))

    def produceWheels(self):
        global nbWheels
        if(tank >= 5) :
            nbWheels += 1
            self.consumeOil()
        print("Quantity of wheels : " + str(nbWheels))

    def produceMotor(self):
        global nbMotors
        if(tank >= 25) :
            nbMotors += 1
            self.consumeOil()
        print("Quantity of motors : " + str(nbMotors))

    ############################################################################
    def run(self):


        print(self.name + " : Starting task")
        if(self.name == "Pump 1" or self.name == "Pump 2") :
            self.produceOil()
        elif(self.name == "Machine 1") :
            self.produceMotor()
        elif (self.name == "Machine 2"):
            self.produceWheels()
        time.sleep(self.execution_time)
        print(self.name + " : Stopping task")
        time.sleep(self.period - self.execution_time)

####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

    task_list = []

    global tank
    tank = 0

    global nbWheels
    nbWheels = 0

    global nbMotors
    nbMotors = 0

    global needOil
    needOil = True

    # Instanciation of task objects

    task_list.append(my_task(name="Pump 1", period=5, execution_time=2, priority=0, oilProducer=True))
    task_list.append(my_task(name="Pump 2", period=15, execution_time=3, priority=0, oilProducer=True))
    task_list.append(my_task(name="Machine 1", period=5, execution_time=5, priority=0, oilProducer=False))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, priority=0, oilProducer=False))

    while(True) :
    # while(current_time < future_time) :
        current_time = datetime.now()
        task_to_run = None

        current_time = datetime.now()
        for current_task in task_list:

            if needOil is True :
                if (tank < 50):
                    if current_task.oilProducer == True:
                        task_to_run = current_task
                        if (tank >= 30):
                            needOil = False
            else :
                if current_task.oilProducer == False :
                    if nbWheels/4 > nbMotors :
                        task_to_run = task_list[2]
                    else :
                        task_to_run = task_list[3]

        if task_to_run == None:
            time.sleep(1)
        else:
            task_to_run.run()


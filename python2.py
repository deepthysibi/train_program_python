class train:
    startengine=False
    movetrain=False
    def __init__(self,train_nm,st_loc,end_loc,st_time,end_time,station):
        self.train_nm=train_nm
        self.st_loc=st_loc
        self.end_loc=end_loc
        self.st_time=st_time
        self.end_time=end_time
        self.station=station
    def display(self):
        print("your train name is ",self.train_nm,"starts at",self.st_time)
    def start_engine(self,e_time,e_loc):
        self.e_time = e_time
        self.e_loc = e_loc
        if self.e_time > self.st_time:
            print("train already started")
            train.startengine = True
            train.movetrain = True
        elif self.e_time==self.st_time and self.st_loc==self.e_loc:
            print("Please start the train")
            train.startengine = True
            train.movetrain = True
        else:
            print("it is not a time for particular train")
            train.startengine = False
            train.movetrain = False
    def move_train(self):
        if train.startengine == True and train.movetrain == True:
            print("train is moving")
        elif train.startengine == True and train.movetrain == False:
            print("start moving")
        elif train.startengine == False and train.movetrain == False:
            print("Engine not started")
    def stop_train(self):
        if train.startengine == False:
            print("Engine is already stop")
        elif train.startengine == True and train.movetrain == False:
            print("Stop engine")
        elif train.startengine == True and train.movetrain == True:
            print("you can't stop the train")
    def get_start(self):
        if train.movetrain == True:
            print("Train departe form ",self.station)
        else:
            print("now train in station",self.station)
    def get_destinaton(self):
        if self.station == self.end_loc:
            print("you find your location at ",self.end_time)
        else:
            print("destination not found")





a=train("parassuram express","kannur","calicut",9.0,12.0,"Mahi")
a.display()
a.start_engine(9.0,"kannur")
a.move_train()
a.stop_train()
a.get_start()
a.get_destinaton()








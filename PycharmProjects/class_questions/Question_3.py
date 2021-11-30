class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def encourage(self):
       print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


Danny = GoodBoss("Danny", "Calm", "Calm2", "Bearded")
Danny.encourage()
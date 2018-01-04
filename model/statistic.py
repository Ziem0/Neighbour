class Statistic:

    all_units = []
    statistic = {'województwo':0, 'powiat':0, 'gmina miejska':0, 'gmina wiejska':0, 
                 'gmina miejsko-wiejska':0, 'miasto':0, 'obszar wiejski':0, 'miasto na prawach powiatu':0,
                 'delegatura':0}

    def __init__(self, _id, name, type):
        self._id = _id
        self.name = name
        self.type = type
        Statistic.all_units.append(self)


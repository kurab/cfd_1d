import yaml

CONFIG_FILE = './config/config.yml'


class LoadConditions(object):
    """ condition loader """

    def __init__(self):
        self._cond = self.load_conditions()

    @property
    def cond(self):
        return self._cond

    def load_conditions(self):
        """ read conditions from yml """
        with open(CONFIG_FILE, 'r') as config:
            cond = yaml.load(config, Loader=yaml.SafeLoader)
            cond['calc']['dx'] = cond['geo']['xl'] / cond['calc']['ni']
            return cond

    def load_initial_shape(self):
        """ set initial shape. triangle shape for example """
        # params for initial shape
        xp = 5.0  # x at peak
        cp = 0.5  # grind

        f = [0] * self._cond['calc']['ni']
        for i in range(self._cond['calc']['ni']):
            x = self._cond['calc']['dx'] * i
            if x < xp:
                f[i] = cp / xp * x
            elif x < xp * 2:
                f[i] = - cp / xp * x + 2 * cp
            else:
                f[i] = 0
        return f

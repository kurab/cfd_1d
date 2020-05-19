class FlowCalculation(object):
    """ flow calculators """

    def __init__(self, calc_cond, flow_cond):
        # unpack calc_cond
        self.ni = calc_cond['ni']
        self.dx = calc_cond['dx']
        self.dt = calc_cond['dt']

        self.flow_cond = flow_cond

    def upwind_method(self, f):
        """ upwind difference method """
        fn = {0: 0}
        for i in range(1, self.ni):
            fn[i] = f[i] - self.flow_cond['c'] * \
                (f[i] - f[i-1]) * self.dt / self.dx

        for i in range(self.ni):
            f[i] = fn[i]

        return f

    def central_method(self, f):
        """ central difference method """
        fn = {0: 0}
        for i in range(1, self.ni):
            fn[i] = (f[i] + self.flow_cond['c'] * self.dt / 2.0 / self.dx *
                     f[i-1]) / (1 + self.flow_cond['c'] * self.dt / 2.0
                                / self.dx)

        for i in range(self.ni):
            f[i] = fn[i]

        return f

    def cip_method(self, f, fd):
        """ CIP: Cubic-Interpolated Pseudo-Particle method """
        fn = [0] * self.ni
        fdn = [0] * self.ni
        if fd == fdn:
            for i in range(1, self.ni):
                fd[i] = (f[i] - f[i-1]) / (2.0 * self.dx)
            fd[0] = fd[1]

        xi = self.dx - self.flow_cond['c'] * self.dt
        for i in range(1, self.ni):
            a = - 2.0 * (f[i] - f[i-1]) / self.dx ** 3 + \
                (fd[i] + fd[i-1]) / self.dx ** 2
            b = 3.0 * (f[i] - f[i-1]) / self.dx ** 2 - \
                (fd[i] + 2.0 * fd[i-1]) / self.dx

            fn[i] = a * xi ** 3 + b * xi ** 2 + fd[i-1] * xi + f[i-1]
            fdn[i] = 3.0 * a * xi ** 2 + 2.0 * b * xi + fd[i-1]

        for i in range(self.ni):
            f[i] = fn[i]
            fd[i] = fdn[i]

        return [f, fd]

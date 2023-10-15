class Computer:
    def init(self, cpufreq, cpucores, ram, hdd=None, ssd=None):
        self.cpufreq = cpufreq
        self.cpucores = cpucores
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd
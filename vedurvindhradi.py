class vedu:
    def __init__(self, value):
        self.value = value
    
    def wind_level_name(self):
        if 0 <= self.value <= 0.2:
            return 'Logn'
        elif 0.3 <= self.value <= 1.5:
            return 'Andvari'
        elif 1.6 <= self.value <= 3.3:
            return 'Kul'
        elif 3.4 <= self.value <= 5.4:
            return 'Gola'
        elif 5.5 <= self.value <= 7.9:
            return 'Stinningsgola'
        elif 8.0 <= self.value <= 10.7:
            return 'Kaldi'
        elif 10.8 <= self.value <= 13.8:
            return 'Stinningskaldi'
        elif 13.9 <= self.value <= 17.1:
            return 'Allhvass vindur'
        elif 17.2 <= self.value <= 20.7:
            return 'Hvassvidri'
        elif 20.8 <= self.value <= 24.4:
            return 'Stormur'
        elif 24.5 <= self.value <= 28.4:
            return 'Rok'
        elif 28.5 <= self.value <= 32.6:
            return 'Ofsavedur'
        elif 32.7 <= self.value:
            return 'Farvidri'
        
val = vedu(float(input()))
print(val.wind_level_name())
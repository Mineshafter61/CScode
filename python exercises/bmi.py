class bmi:
    healthlevel = 'Healthy'
    def __init__(self, weight, height):
        self.BMI = weight/(height**2)
        if self.BMI < 20:
            self.healthlevel = 'Below healthy'
        elif self.BMI > 25:
            self.healthlevel = 'Above healthy'
r = bmi(eval(input('Weight? ')),eval(input('Height? ')))
print('BMI = '+str(r.BMI)); print('Health level = '+str(r.healthlevel))
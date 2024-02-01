class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15,5)
        Fahrenheit = round(celsius * 1.80 + 32.00,5)
        
        print(f'Temperature at {celsius} Celsius converted in Kelvin is {kelvin} and converted in Fahrenheit is {Fahrenheit}')
        return [kelvin , Fahrenheit ]
        
        
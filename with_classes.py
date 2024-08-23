import os
import sys

path = "/Users/hussain.ali/Desktop/Python projects/weatherdata/"
model_data = {}
os.chdir(path)

class WeatherManMain:
    
    def usageInfo(self):
        print('Usage: weatherman [report#] [data_dir]')
        print('[Report #]')
        print('1 for Annual Max/Min Temperature')
        print('2 for the Hottest day of each year')
        
# Class to read file 
class FileParser:
    
    def file_iteration_and_handling(self):
        for filename in os.listdir(path=path):
            if filename.endswith('.txt'):  # Process only .txt files
                file_path = os.path.join(path, filename)
                
                # Open and read the file
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    
                    empty_line = lines[0]
                    print(empty_line)
                    
                    
                    header = [head.strip() for head in lines[1].strip().split(',')]
                    #print(header)
                    pkt_value = ['PKT', 'PKST']

                    
                    files_data = lines[2:-1]
                    #print(files_data)
                    
                    for line in files_data:
                        values = [value.strip() for value in line.strip().split(',')]
                        model_data = dict(zip(header, values))
                        
                    print(model_data)
                    print(f"The data of PKT is {model_data['Max TemperatureC']}")
                    
#obj = FileParser()
#obj

weather_man_object = WeatherManMain()
weather_man_object.usageInfo()
'''
class ArgParser:
    
    
'''   
class Report:
    
    def __init__(self):
        self.reports = {
            'annual_report' : AnnualReport(),
            'hottest_day' : HottestDay()
        }
        
class AnnualReport:
    
    def report(self, year, max_temperature, min_temperature, max_humidity, min_humidity):
        self.year = model_data['PKT'] 
        self.max_temperature = model_data['Max TemperatureC']
        self.min_temperature = model_data['Min TemperatureC']
        self.max_humidity = model_data['Max Humidity']
        self.min_humidity = model_data['Min Humidity']


class HottestDay:
    
    def report(self, year, date, temperature):
        self.year = model_data['PKT']
        self.date = model_data['PKT']
        self.temperature = model_data['']

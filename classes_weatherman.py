import os
import sys
import glob

file_directory = "/Users/hussain.ali/Desktop/Python projects/weatherdata/"

class FileParser:
    
    def read_files_of_a_year(self, year):
        
        data_of_a_year = []
        
        files_in_a_year = os.path.join(file_directory, f"lahore_weather_{year}_*")
        files_in_a_year = glob.glob(files_in_a_year)
        #print(files_in_a_year)
        
        for file in files_in_a_year:
            data_in_file = self.read_file(file)
            
            data_of_a_year.extend(data_in_file)
        #print(len(data_of_a_year))
        return data_of_a_year
            
            
    def read_file(self, filename):
    
        all_values = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for line_index in range(2,len(lines) - 1):
                values = [value.strip() for value in lines[line_index].strip().split(',')]
                #print(values)
                all_values.append(values)
                
            return all_values
                            
                                                        
class ArgParser:
    
    def user_input(self):
        if len(sys.argv) < 3:
            print("Error: Not enough arguments provided.")
            print("Usage: python script_name.py <report_number> <data_directory>")
            sys.exit(1)  # Exit the script with an error code
        
        report_number = sys.argv[1]
        data_directory = sys.argv[2]
        return report_number, data_directory
            
            
class Report:
    
    def __init__(self, year) :
        self.file_parser = FileParser()
        self.data = []

        self.data = self.file_parser.read_files_of_a_year(year)

        
    
    def max_temperature(self, report_number):
        
        max_temperature_of_a_year = float('-inf')
        date = ''
        for row in self.data:
            
            if row[1] and float(row[1]) > max_temperature_of_a_year:
                max_temperature_of_a_year = float(row[1])
                date = row[0]
                
        year = date.strip().split('-')[0]
        #print(year)
                
        
        if report_number == '1':
            return max_temperature_of_a_year
        elif report_number == '2':
            return date, max_temperature_of_a_year


    def min_temperature(self):
        min_temperature_of_a_year = min(float(row[3]) if row[3] else float('+inf') for row in self.data)
        temp = [float(row[3]) if row[3] else float('+inf') for row in self.data]
        #print(len(self.data), temp)
        #print(min_temperature_of_a_year)
        
        return int(min_temperature_of_a_year)
        
    def max_humidity(self):
        max_humidity_of_a_year = max(float(row[7]) if row[7] else float('-inf') for row in self.data)
        #print(max_humidity_of_a_year)
        
        return int(max_humidity_of_a_year)
        
    def min_humidity(self):
        min_humidity_of_a_year = min(float(row[9]) if row[9] else float('+inf') for row in self.data)
        #print(min_humidity_of_a_year)
        
        return int(min_humidity_of_a_year)

    #def year(self):
        

class AnnualReport:
    
    
    def __init__(self):
        pass
    
    def annual_report_summary(self, report_number):
            
        years = list(range(1996,2012))
        #print(years)
           
        print("\nYearly Summary (Max/Min Temperature):")
        print("Year\t\tMAX Temp\t\tMIN Temp\t\tMAX Humidity\t\tMIN Humidity")
        print("-"*50)   
            
        for present_year in years:
            report_of_year = Report(present_year)

            max_temp_data = report_of_year.max_temperature(report_number)
            min_temp_data = report_of_year.min_temperature()
            max_humidit = report_of_year.max_humidity()
            min_humidit = report_of_year.min_humidity()
        
            print(f"{present_year}\t\t{max_temp_data}C\t\t\t{min_temp_data}C\t\t\t{max_humidit}\t\t\t{min_humidit}")
            

class HottestDay:
    
    def __init__(self):
        pass

    def hottest_report_summary(self, report_number):
        years = list(range(1996,2012))
        #print(years)
           
        print("\nYearly Summary (Hottest days of each year):")
        print("Year\t\tDate\t\t\tTemp")
        print("-"*50)   
            
        for present_year in years:
            report_of_year = Report(present_year)

            max_temp_data = report_of_year.max_temperature(report_number)
            date = report_of_year.max_temperature(report_number)
        
            print(f"{present_year}\t\t{date[0]}\t\t{max_temp_data[1]}C")


class ReportHandler:
    
    def user_input(self, report_number, data_directory):
        
        #print(report_number, type(report_number))
        if int(report_number) == 1:
            annual_report = AnnualReport()
            #print(annual_report)
            annual_report.annual_report_summary(report_number)
        elif int(report_number)  == 2:
            hottest_day = HottestDay()
            hottest_day.hottest_report_summary(report_number)
        
                     
class WeatherManMain:
    
    
    def __init__(self):
        self.arg_parser = ArgParser() 
    
    #report_number, data_directory = arg_parser.user_input()
    def usage_info(self):
        print("Usage: weatherman [report#] [data_dir]\n")
        print("[Report #]")
        print("1 for Annual Max/Min Temperature")
        print("2 for the Hottest day of each year")

        result = self.arg_parser.user_input()
        report_handler = ReportHandler()
        report_handler.user_input(result[0], result[1])
        

weather_man_main = WeatherManMain()
weather_man_main.usage_info()
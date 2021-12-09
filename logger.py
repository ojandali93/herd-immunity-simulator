from datetime import datetime

class Logger(object):
  def __init__(self, file_name):
    self.filename = file_name
    
  def write_metadata(self,pop_size, vacc_percent, virus_name, mortality_rate, basic_repro_num):
    new = datetime.now()
    date_time = now.strftime("%%m/%d/%y - %H:%M:%S")
    file = open(self.file_name, 'w')
    file.write(f'********** HERD IMMUNITY SIMULATION -{dt_string}- **********\n\n')
    file.write(f'Population Size: {pop_size} | Initially Vaccinated %: {vacc_percentage * 100} | Virus: {virus_name} | Mortality Rate: {mortality_rate} | Reproductive Rate: {repro_rate}\n\n')
    file.close

if __name__ == '__main__':
  myLogger = Logger('answer.txt')
  myLogger.write_metadata(500, .1, 'Covid', .75, .25)
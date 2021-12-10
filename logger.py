from datetime import datetime

class Logger(object):
  def __init__(self, file_name):
    self.file_name = file_name
    
  def write_metadata(self, pop_size, vacc_percent, virus_name, mortality_rate, repro_rate):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%y - %H:%M:%S")
    file = open(self.file_name, 'w+')
    file.write(f'********** HERD IMMUNITY SIMULATION ** {date_time} **********\n\n')
    file.write(f'Population Size: {pop_size} | Initially Vaccinated %: {vacc_percent * 100} | Virus: {virus_name} | Mortality Rate: {mortality_rate} | Reproductive Rate: {repro_rate} \n\n')
    file.close

  def write_results(self, total_population, total_vaccinated, total_dead, total_infected):
    file = open(self.file_name, 'w+')
    file.write(f'************ Time Step ** {step} ************\n')
    file.write(f'Total population: {total_population} | Total vaccinated: {total_vaccinated} | Total dead: {total_dead} | Total infected: {total_infected}\n\n')
    file.close

if __name__ == '__main__':
    myLogger = Logger('answers.txt')
    myLogger.write_metadata(100, 0.10, 'Ebola', 0.70, 0.25,)

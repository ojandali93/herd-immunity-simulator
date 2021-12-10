import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
  def __init__(self, virus, pop_size, vacc_percent, initial_infected=1, interactions=100):
    self.logger = Logger('Log.txt')
    self.virus = virus
    self.pop_size = pop_size
    self.vacc_percent = vacc_percent
    self.initial_infected = initial_infected
    self.interactions = interactions

    self.total_population = []
    self.total_dead = []
    self.currently_vaccinated = []
    self.currently_infected = []   
    self.currently_alive = []
    self.newly_infected = []
    
    self.currently_dead_count = 0
    self.currently_alive_count = pop_size
    self.new_dead_count = 0
    self.total_vaccinated_count = int(pop_size * self.vacc_percent)
    self.total_dead_count = 0
    self.total_immune_count = 0
    self.total_infected_count = 0

    self.default_population = self._create_population()

  def _create_population(self):
    total_vaccinated = self.total_vaccinated_count
    initial_infected = self.initial_infected
    remaining_population = int(self.pop_size - total_vaccinated - initial_infected)
    init_vac_id = 0
    init_infected_id = 0
    init_remaining_id = 0 
    while init_vac_id < total_vaccinated:
      init_vac_id += 1 
      vaccinated_person = Person(init_vac_id, True, None)
      self.total_population.append(vaccinated_person)
      self.currently_vaccinated.append(vaccinated_person)
      self.currently_alive.append(vaccinated_person)
      self.currently_alive_count +=1
    while init_infected_id < initial_infected:
      init_infected_id += 1 
      infected_person = Person(len(self.total_population) + 1, False, self.virus)
      self.total_population.append(infected_person)
      self.currently_infected.append(infected_person)
      self.currently_alive.append(infected_person)
      self.currently_alive_count +=1
    while init_remaining_id < remaining_population:
      init_remaining_id += 1 
      remaining_person = Person(len(self.total_population) + 1, False, None)
      self.total_population.append(remaining_person)
      self.currently_alive.append(remaining_person)
      self.currently_alive_count +=1
    print(len(self.total_population))
    print(len(self.currently_alive))
    print(len(self.currently_vaccinated))
    print(len(self.currently_infected))

  def _simulation_should_continue(self):
    run_again = True
    alive_count = self.total_vaccinated_count + self.total_dead_count
    if self.pop_size == alive_count:
      run_again = False 
    elif self.total_infected_count == 0:
      run_again = False
    return run_again

  def run(self):
    self.logger.write_metadata(self.pop_size, self.vacc_percent, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
    time_step_counter = 0
    should_continue = True
    while should_continue:
      time_step_counter += 1
      print(f'Current Time Step - {time_step_counter}\n')
      # print(f'Total vaccinated: {self.total_vaccinated_count} | Total dead: {self.total_dead_count} | Total infected: {self.total_infected_count}\n\n')
      self.time_step()
      should_continue = self._simulation_should_continue()
    print(f'Simulation complete in {time_step_counter} steps!')

  def time_step(self):
    for infected_person in self.currently_infected:
      for interaction in range(self.interactions):
        random_selected_person = random.choice(self.currently_alive)
        while random_selected_person.infection:
          random_selected_person = random.choice(self.currently_alive)
        self.interaction(infected_person, random_selected_person)
        if random_selected_person.did_survived_infection():
          self.currently_vaccinated.append(random_selected_person)
          self.total_vaccinated_count += 1 
        else:
          self.total_dead.append(random_selected_person)
          self.currently_alive.remove(random_selected_person)
          self.total_dead_count += 1 
          self.currently_alive_count -= 1
    print(f'Total vaccinated: {self.total_vaccinated_count} | Total dead: {self.total_dead_count} | Total infected: {self.total_infected_count}\n\n')
    self._infect_newly_infected()

  def interaction(self, infected_person, random_person):
    if random_person.infection == None and random_person.is_vaccinated == False:
      random_value = random.uniform(0, 1)
      if random_value < infected_person.infection.repro_rate:
        if random_person._id not in self.currently_infected:
          self.newly_infected.append(random_person)
          self.total_infected_count += 1
    else:
      pass


  def _infect_newly_infected(self):
    for person in self.newly_infected:
      person.infection = self.virus
      self.total_population.remove(person)
      self.total_infected_count += 1
      self.total_population.append(person)
    self.newly_infected = []
      
if __name__ == "__main__":
  virus_name_input = input('What is the virus name?  ')
  repro_rate_input = input('What is the reproduction rate?  ')
  mortality_rate_input = input('What is the mortality rate?  ')

  population_size_input = input('What is the population size?  ')
  vacc_percentage_input = input('What percentage of the population is vaccinated?  ')
  initial_infected_input = input('How many people are initially infected?  ')
  average_interactions_input = input('How many interactions should each infected person have?  ')

  repro_rate = int(repro_rate_input) / 100
  mortality_rate = int(mortality_rate_input) / 100
  vacc_percentage = int(vacc_percentage_input) / 100
  population_size_input = int(population_size_input)
  initial_infected_input = int(initial_infected_input)
  average_interactions_input = int(average_interactions_input)

  virus = Virus(virus_name_input, repro_rate, mortality_rate)
  sim = Simulation(virus, population_size_input, vacc_percentage, initial_infected_input, average_interactions_input)
  sim.run()
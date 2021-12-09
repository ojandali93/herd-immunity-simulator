import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
  def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1, interactions=100):
    self.logger = Logger('answers.txt')
    self.pop_size = pop_size
    self.virus = virus
    self.initial_infected = initial_infected
    self.vacc_percentage = vacc_percentage 
    self.interactions = interactions

    self.total_vaccinated = int(pop_size * self.vacc_percentage)
    self.currently_infected = []  
    self.population = [] 
    self.newly_infected = [] 
    self.newly_dead = 0
    self.total_dead = 0
    self.n_person_id = 0  
    self.total_immune = 0 
    self.total_infected = 0
    self._create_population()

  def _create_population(self):
    all_people = []
    total_vaccinated = int(self.pop_size * self.vacc_percentage)
    remaining_population = int(self.pop_size - total_vaccinated - initial_infected)
    initial_vac_id = 0
    initial_infected_id = 0
    inital_remainder_id = 0
    while initial_vac_id < total_vaccinated:
      vaccinated_person = Person(initial_vac_id + 1, True, None)
      people.append(vaccinated_person)
    while initial_infected_id < initial_infected:
      self.total_infexted += 1 
      infected_person = Person(len(people) + 1, False, self.virus)
      people.append(infected_person)
    while inital_remainder_id < remaining_population:
      remaining_person = Person(len(people) + 1, False, None)
      people.append(remaining_person)

  def _simulation_should_continue(self):
    keep_running = True
      if self.pop_size == self.total_vaccinated + self.total_dead:
          keep_running = False
      if self.total_infected == 0:
          keep_running = False
      return keep_running

  def run(self):
    time_step_counter = 0
    should_continue = self._simulation_should_continue()

    while should_continue:
      print(f'======TIME STEP {time_step_counter}=======')
      self.time_step()
      self.current_infected = []
      self._infect_newly_infected()
      self.logger.log_time_step(step_num, len(self.newly_infected), self.newly_dead, self.total_infected, self.total_dead, self.total_immune, len(self.population), self.herd_immunity)
      self.newly_infected = []
      self.newly_dead = 0
      time_step_counter +=1
      should_continue = self._simulation_should_continue()

  def time_step(self):
    currently_infected = self.current_infected
    for person in currently_infected:
      random_sample = random.sample(self.population, self.average_interactions)
      for r_person in random_sample:
        self.interaction(person, r_person)

  def interaction(self, person, random_person):
    assert person.is_alive == True
    assert random_person.is_alive == True
    if random_person.is_vaccinated or random_person.infection:
      pass
    elif random_person.infection == None and random_person.is_vaccinated == False:
      if random.uniform(0, 1) < person.infection.repro_rate:
        if random_person._id not in self.newly_infected:
          self.newly_infected.append(random_person._id)
          self.total_infected += 1
  

  def _infect_newly_infected(self):
    for _id in self.newly_infected:
      for person in self.population:
        if person._id == _id:
          person.infection = self.virus
    self.newly_infected = []
    
if __name__ == "__main__":
  virus_name = validate_input('What is the virus name?  ', str)
  repro_rate = validate_input('What is the reproduction rate?  ')/100
  mortality_rate = validate_input('What is the mortality rate?  ')/100

  population_size = validate_input('What is the population size?  ')
  vacc_percentage = validate_input('What percentage of the population is vaccinated?  ')/100
  initial_infected = validate_input('How many people are initially infected?  ')
  average_interactions = validate_input('How many interactions should each infected person have?  ')

  virus = Virus(virus_name, repro_rate, mortality_rate)
  simulation = Simulation(virus, population_size, vacc_percentage, initial_infected, average_interactions)

  simulation.run()
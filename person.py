import random
from virus import Virus

class Person(object):
  def __init__(self, _id, is_vaccinated, infection = None):
    self._id = _id 
    self.alive = True 
    self.vaccinated = is_vaccinated
    self.infection = infection

  def did_survived_infection(self):
    if self.infection:
      if(random.uniform(0,1) > self.infection.mortality_rate):
        self.is_vaccinated = True
        self.infection = None
      else:
        self.is_alive = False
        self.Infection = False

if __name__ == '__main__':
  vaccinated_person = Person(1, True)
  assert vaccinated_person._id == 1
  assert vaccinated_person.is_alive is True
  assert vaccinated_person.is_vaccinated is True
  assert vaccinated_person.infection is None

  unvaccinated_person = Person(2, False)
  assert vaccinated_person._id == 2
  assert vaccinated_person.is_alive is True
  assert vaccinated_person.is_vaccinated is False

  covid = Virus("Covid", 0.8, 0.25)

  person_3 = Person(3, False, covid)
  assert person_3._id == 3
  assert person_3.is_vaccinated == False
  assert person_4.infection == virus

  person_4 = Person(4, False, covid)
  survived = person_4.did_survive_infection()
  if survived:
    assert person_4.is_alive is True
    assert person_4.is_vaccinated is True
    assert person_4.infection is None
  else:
    assert person_4.is_alive is False
    assert person_4.is_vaccinated is False
    assert person_4.infection is not None

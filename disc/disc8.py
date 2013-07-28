current_year = 2013

class Animal(object):
	def __init__(self):
		self.is_alive = True # It’s alive!!!

class Pet(Animal):
	def __init__(self, name, year_of_birth, owner=None):
		Animal.__init__(self) # call the parent’s constructor
		self.name = name
		self.age = current_year - year_of_birth
		self.owner = owner

	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")

	def talk(self):
		print("...")

class Dog(Pet):
	def __init__(self, name, yob, owner, color):
		Pet.__init__(self, name, yob, owner)
		self.color = color

	def talk(self):
		print("Woof!")

class Cat(Pet):
	def __init__(self, name, yob, owner, lives=9):
		Pet.__init__(self, name, yob, owner)
		self.lives = lives

	def talk(self):
		"""A cat says ’Meow!’ when asked to talk."""
		print("Meow!")

	def lose_life(self):
		"""A cat can only lose a life if they have
		at least one life. When lives reach zero,
		the ’is_alive’ variable becomes False.
		"""
		if self.lives > 0:
			self.lives -= 1
			if self.lives == 0:
				self.is_alive = False
		else:
			print("This cat has no more lives to lose :(")

class NoisyCat(Cat):
	"""A class that behaves just like a Cat, but always
	repeats things twice.
	"""
	def __init__(self, name, yob, owner, lives=9):
		Cat.__init__(self, name, yob, owner, lives)

	def talk(self):
		"""A NoisyCat will always repeat what he/she said
		twice.
		"""
		Cat.talk(self)
		Cat.talk(self)

def type_tag(x):
	return type_tag.tags[type(x)]

class HN_record(object):
	"""A student record formatted via Hamilton's standard"""
	def __init__(self, name, grade):
		"""name is a string containing the student's name,
		and grade is a grade object"""
		self.student_info = [name, grade] 

class JO_record(object):
	"""A student record formatted via Julia's standard"""
	def __init__(self, name, grade):
		"""name is a string containing the student's name,
		and grade is a grade object"""
		self.student_info = {'name': name, 'grade': grade}

type_tag.tags = {HN_record: 'HN', JO_record: 'JO'}

def get_name(record):
	data_type = type_tag(record)
	return get_name.implementations[data_type](record)

def get_grade(record):
	data_type = type_tag(record)
	return get_grade.implementations[data_type](record)

get_name.implementations = {}
get_name.implementations['HN'] = lambda x: x.student_info[0]
get_name.implementations['JO'] = lambda x: x.student_info['name']
get_grade.implementations = {}
get_grade.implementations['HN'] = lambda x: x.student_info[1]
get_grade.implementations['JO'] = lambda x: x.student_info['grade']


class HN_grade(object):
	def __init__(self, total_points):
		if total_points > 90:
			letter_grade = ’A’
		else:
			letter_grade = ’F’
		self.grade_info = (total_points, letter_grade)

class JO_grade(object):
	def __init__(self, total_points):
		self.grade_info = total_points

type_tag.tags[HN_grade] = 'HN'
type_tag.tags[JO_grade] = 'JO'

def get_points(grade):
	data_type = type_tag(grade)
	return get_total.implementations[data_type](grade)

get_points.implementations = {}
get_points.implementations['HN'] = lambda x: x.grade_info[0]
get_points.implementations['JO'] = lambda x: x.grade_info

def compute_average_total(records):
	total = 0
	for record in records:
		grade = get_grade(record)
		total += get_points(grade)
	return total / len(records)

class AK_grade(object):
	"""A student record formatted via John’s standard"""
	def __init__(self, name_str, grade_num):
	"""NOTE: name_str must be a string, grade_num must be a number"""

def convert_to_AK(records):
	ak_records = []
	for record in records:
		ak_records.append(AK_grade(get_name(record)), AK_grade(get_grade(record)))
	return ak_records

if __name__  == '__main__':
	from doctest import run_docstring_examples
	run_docstring_examples(mutate_rational, globals(), True)

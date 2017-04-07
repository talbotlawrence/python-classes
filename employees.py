class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date
        self.employees = set()

    def get_name(self):
        """Returns the name of the company"""
        
        return self.name


class Employee:
    """This represents Employees at a company"""

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

    def get_name(self):
        """Returns the Employee name"""
        
        return self.name

    def set_name(self, name):
        """Sets the employee name"""

        self.name = name

    # Add the remaining methods to fill the requirements above

talbot_corp = Company('Talbot Corp','Talbot Corporation','12-3-1999')
print("My name of the company is {} and the title is {} baby!!".format(talbot_corp.name,talbot_corp.title))

jennifer = Employee('Jen Lawrence','CEO','12-3-1999')
talbot = Employee('Talbot Lawrence','CIO','12-3-1999')
maddie = Employee('Madelyn Lawrence','CFO','12-3-1999')
print("{} is the {} of the company".format(jennifer.name,jennifer.job_title))

talbot_corp.employees.add(jennifer)
talbot_corp.employees.add(talbot)
talbot_corp.employees.add(maddie)
print(talbot_corp)

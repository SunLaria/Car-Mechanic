class Car:
    # רישום של רכב חדש עם הפרטים הרלוונטיים של הרכב שם שנת ייצור צבע מספר רישוי שם
#  בעל הרכב תאריך כניסה אחרון למוסך תאריך טיפול אחרון
    def __init__(self, model, year, color, numberplate, holder_name, last_garage_visit, last_treatment):
        self.model = model
        self.year = year
        self.color = color
        self.numberplate = numberplate
        self.holder_name = holder_name
        self.last_garage_visit = last_garage_visit
        self.last_treatment = last_treatment

   
    def print_info(self):
        print(f'{self.model}, {self.year}, {self.color}, {self.numberplate},{self.holder_name},{self.last_garage_visit},{self.last_treatment}')

    
    def __repr__(self):
        return self.numberplate
    

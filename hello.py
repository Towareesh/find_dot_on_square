class NewClass:
    """docstring for NewClass"""
    def __init__(self, arg):
        """magic method"""
        self.arg = arg
    
    def main(self, arg):
        return 'Hi'

a = 'hLLO'
rec = NewClass(a).main(a)
print(rec)
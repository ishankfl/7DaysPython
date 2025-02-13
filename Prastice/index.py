class CheckStatic:
    __school_name = "Hello"
    def __init__(self):
        self.variablename="How"
    @staticmethod
    def StaticMethod():
        print("Hello world")
        
    @classmethod
    def staticTest(cls):
        
        print(cls.StaticMethod())
        print("Hello Static Test")
    
    
obj = CheckStatic()
print(obj.staticTest())

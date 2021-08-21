from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    
    @staticmethod
    def bcryp(pwd :str ):
         return pwd_context.hash(pwd)
    
    @staticmethod
    def verify(hashed_pwd:str , pwd:str): 
        return pwd_context.verify(pwd,hashed_pwd)
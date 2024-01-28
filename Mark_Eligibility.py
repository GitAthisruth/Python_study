class Marks():
    def __init__(self,Name,Roll_num,Malayalam,English,Hindi,Maths):
          self.Name=Name
          self.Roll_num=Roll_num
          self.Malayalam=Malayalam
          self.English=English
          self.Hindi=Hindi
          self.Maths=Maths
          self.Total_mrk_cand=self.Malayalam+self.English+self.Hindi+self.Maths
          self.Total_marks=400
          self.percentage=self.Total_mrk_cand/self.Total_marks

    def Malayalam_Grade(self):
        if self.Malayalam >=90 and self.Malayalam <=100:
           return 'A'
        elif  self.Malayalam >=80 and self.Malayalam <90 :
            return 'B'
        elif  self.Malayalam >=70 and self.Malayalam <80 :
            return 'C'
        elif  self.Malayalam >=60 and self.Malayalam <70 :
            return 'D'
        elif self.Malayalam <60:
             return 'Fail(F)'
        else:
            return 'invalid input'

    def English_Grade(self):
        if self.English >=90 and self.English <=100:
           return 'A'
        elif  self.English >=80 and self.English <90 :
            return 'B'
        elif  self.English >=70 and self.English <80 :
            return 'C'
        elif  self.English >=60 and self.English <70 :
            return 'D'
        elif self.English <60:
             return 'Fail(F)'
        else:
             return 'invalid input'

    
    def Hindi_Grade(self):
        if self.Hindi >=90 and self.Hindi <=100:
           return 'A'
        elif  self.Hindi >=80 and self.Hindi <90 :
            return 'B'
        elif  self.Hindi >=70 and self.Hindi <80 :
            return 'C'
        elif  self.Hindi >=60 and self.Hindi <70 :
            return 'D'
        elif self.Hindi <60:
             return 'Fail(F)'
        else:
             return 'invalid input'


    def Maths_Grade(self):
        if self.Maths >=90 and self.Maths <=100:
           return 'A'
        elif  self.Maths >=80 and self.Maths <90 :
            return 'B'
        elif  self.Maths >=70 and self.Maths <80 :
            return 'C'
        elif  self.Maths >=60 and self.Maths <70 :
            return 'D'
        elif self.Maths <60:
             return 'Fail(F)'

        else:
              return 'invalid input'

    
       
    def Eligibility(self):

        if self.Malayalam >59 and self.English >59 and self.Hindi >59 and self.Maths >59:
            if self.Malayalam <=100 and self.English <=100 and self.Hindi <=100 and self.Maths <=100:
               return  f" Name: {self.Name} \n Malayalam_marks:{self.Malayalam} \n Grade:{self.Malayalam_Grade()} \n English_marks:{self.English} \n Grade:{self.English_Grade()}\n Hindi_marks:{self.Hindi} \n Grade:{self.Hindi_Grade()}\n Maths_marks:{self.Maths} \n Grade:{self.Maths_Grade()} \n Total mark : {self.Total_mrk_cand} \n Total Percentage : {self.percentage*100}"
        elif self.Malayalam <60 and self.English <60 and self.Hindi <60 and self.Maths <60:
            return f" Name: {self.Name} \n Malayalam_marks:{self.Malayalam} \n Grade:{self.Malayalam_Grade()} \n English_marks:{self.English} \n Grade:{self.English_Grade()}\n Hindi_marks:{self.Hindi} \n Grade:{self.Hindi_Grade()}\n Maths_marks:{self.Maths} \n Grade:{self.Maths_Grade()} \n Total mark : {'..'} \n Total Percentage : {'..'}"

        else:
            return 'invalid input'

         
          

          
student1=Marks('Alex',12345,67,89,90,60)
student2=Marks('Amal',12345,58,121,90,100)
student3=Marks('Akhil',12346,100,100,100,100)
student4=Marks('Aswin',12346,60,60,60,60)
student5=Marks('Aswin',12346,59,59,59)



print(student1.Eligibility())
print()
print(student2.Eligibility())
print()
print(student3.Eligibility())
print()
print(student4.Eligibility())
print()
print(student5.Eligibility())







# # def fizzBuzz(n):
# #     # Write your code here
# #     for i in range(1,n+1):
# #         if i % 3 == 0 and i % 5 == 0:
# #            print("FizzBuzz")
# #         elif i % 3 == 0:
# #             print("Fizz")
# #         elif i % 5 == 0:
# #             print("Buzz")
# #         else:
# #             print(i)          

# # if __name__ == '__main__':
# #     n = int(input().strip())

# #     fizzBuzz(n)





# # def reverse_words_order_and_swap_cases(sentence):
# #     # Split the sentence into words
# #     words = sentence.split()

# #     # Reverse the order of words and swap case for each word
# #     reversed_words = [word.swapcase() for word in reversed(words)]

# #     # Join the reversed and modified words back into a single string
# #     result = ' '.join(reversed_words)

# #     return result

# # if __name__ == '__main__':
# #     sentence = input()
# #     result = reverse_words_order_and_swap_cases(sentence)
# #     print(result)

# #Time complexity
# class square_numbers:
#     def __init__(self):
#         self.s_number = []
        
#     def sn(self,num):       
#         for n in num:
#             self.s_number.append(n*n)
#         return self.s_number
        
# if __name__ == "__main__":
#     num = [1,2,3,4]
#     sn = square_numbers()
#     # results = 
#     print(sn.sn(num), "sn")

# class looping:
#     def __init__(self):
#         self.num = [1,2,3,4,4,55,7,6,9]
        
#     def loops(self):
#         for i in range(len(self.num)):
#             for j in range(i+1, len(self.num)):
#                 if self.num[i] == self.num[j]:
#                     print(self.num[i],"di")
                    
# if __name__ == "__main__":
#     l = looping()
#     l.loops()                
                  
     
# # space complexcity

# class odd:
#     def __init__(self):
        
#         self.allnum = []
        
#     def creat(self):
#         put = input("entr: ")
#         num = put.split(",")
#         for n in num:
#             n = int(n)
#             if n % 2 ==1:
#                 self.allnum.append(n)
                
#         print(self.allnum)        
                
# if __name__ =="__main__":
#     sp = odd()
#     sp.creat()                
            
            
# class all_price:
#     def __init__(self):
#         self.exp = [2200,2350,2600,2130,2190]
#     def price_day(self):
#         extra = self.exp[1] - self.exp[0]
#         print(extra)
#         e_thre_month = self.exp[1] + self.exp[0] + self.exp[3   ]
#         print(e_thre_month,"333 month")
#         for i in range(len(self.exp)):
#             if self.exp[i] == 2000:
#                 return print(i,"yes")
#             else:
#                 print("no") 
#             break
#         self.exp.append(1980)
#         print(self.exp)
               
    
# if __name__ == "__main__":
#    p = all_price()
#    p.price_day()                
        
        
# class month:
#     def __init__(self):
#         self.heros=['spider man','thor','hulk','iron man','captain america']   
#     def monthly_exp(self):
#         print(len(self.heros))
#         self.heros.append("b p")
#         print(self.heros)
#         self.heros.pop()
#         print(self.heros)
#         self.heros.insert(3,"bp")
#         print(self.heros)
#         self.heros[1:3] = ["doc"] # removing thor and hulk and adding doc   
#         print(self.heros)
#         self.heros.sort()
#         print(self.heros)
#         # for i in range(len(self.heros)):
#         #     return print(len(i),"lennene")
#         # for j in range(self.heros.append(i)):
#         #     print(j,"append")     
         
# if __name__ == "__main__":
#    p = month()
#    p.monthly_exp()                    



# import random

# # Create a 2D matrix with random integers between 0 and 255.

# def create_matrix():
#     height = int(input("Enter height"))
#     width = int(input("Enter width"))
    
  
#     matrix = [[random.randint(0, 255) for _ in range(width)] for _ in range(height)]  #underscore is use as place holder so it dont store value
#     return matrix

# def transposed(matrix):
#     trans = [[matrix[i][j] for j in range(len(matrix))] for i in range(len(matrix[0]))]
#     return trans

# matrix = create_matrix()
# print("Original",matrix)
# for n in matrix:
#     print("n",n)


# trans_matrix = transposed(matrix)
# print("transMatrix", trans_matrix)

# for col in trans_matrix:
#     print(col,"coll")
    
   

# def triangle(val):
#     for i in range(1, val + 1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()    
# val = int(input("Enter : "))

# triangle(val)

def pyramid(val):
    for i in range(1,val + 1):
        for j in range(val - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print("*", end=" ")  
        print()
        
val = int(input("Enter py"))
pyramid(val)
def rect(height,width):
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
            
height = int(input("Enter: "))
width = int(input("Enter: "))

rect(height, width)

def print_empty_rectangle(height, width):
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("*", end="  ")  # Print "*" for the border
            else:
                print(" ", end=" ")  # Print a space for the inside
        print()  # Move to the next line after each row

# Prompt the user for input
height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Call the function with user input
print_empty_rectangle(height, width)

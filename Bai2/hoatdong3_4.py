import math

print("Bài tập 3.1")
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))   
print(int(so_thuc))      


print("\n Bài tập 3.2")
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))        
print(round(b))      
print(round(b, 2))  
print(pow(c, 2))     
print(divmod(c, d)) 

print("\nBài tập 3.3 ")
a_pt, b_pt, c_pt = 1, -3, 2

delta = b_pt ** 2 - 4 * a_pt * c_pt
x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")


print("\nBài tập 4.1 ")
cau = "Lap trinh Python rat thu vi"

print(cau[0])       
print(cau[-1])       
print(cau[4:10])     
print(cau[:8])       
print(cau[11:])      
print(cau[::-1])     


is_palindrome = (cau == cau[::-1])
print(f"Chuoi '{cau}' co phai Palindrome không?: {is_palindrome}")



print("\n Bài tập 4.2 ")
ten = "Nam"

ten_moi = "T" + ten[1:]
print(ten_moi)  


print("\n Bài tập 4.3")
cau_str = " Toi dang HOC Python rat vui "

print(cau_str.strip())                         
print(cau_str.strip().upper())                 
print(cau_str.strip().lower())               
print(cau_str.strip().replace("HOC", "hoc"))   
print(len(cau_str.strip().split()))            
print(cau_str.count("o"))                      
print(cau_str.find("Python"))                  
print(cau_str.strip().startswith("Toi"))       
print(cau_str.strip().endswith("vui"))         
print("-".join(["Python", "that", "thu", "vi"])) 


print("\n Bài tập 4.4")
ho_ten_tho = "   nguyen   van    an   "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()

print(f"Họ tên thô: '{ho_ten_tho}'")
print(f"Họ tên sạch: '{ho_ten_sach}'")
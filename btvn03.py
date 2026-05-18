import random
# Nhập dữ liệu
name_patient = input("Nhập Họ và Tên của bệnh nhân: ") # Nhập họ và tên thì sẽ sử dụng kiểu dữ liệu char
disease_id = f"BN{random.randint(100,999)}" # id bệnh nhân sẽ để tự động bằng cách sử dụng random
examination_department = input("Nhập khoa/phòng khám chỉ định: ") # Nhập đại chỉ khoa cũng sử dụng kiểu dữ liệu char

# In phiếu
print("---PHIẾU KHÁM BỆNH---")
print("Họ và Tên:",name_patient)
print("Mã BA:",disease_id)
print("Khoa/Phòng khám chỉ định:",examination_department)
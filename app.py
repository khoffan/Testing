#1. แสดงค่าจำนวนเต็มที่มากที่สุด กำหนดให้ $number = array(1,2,31,4,15,6,7,22,9,10);
def findMax(nums):
    result = 0
    for num in nums:
        if num > result:
            result = num
    return result

#2. แสดงค่าจำนวนเต็มที่น้อยที่สุด กำหนดให้ $number = array(1,2,31,4,15,6,7,22,9,10);
def findMin(nums):
    result = nums[0]
    for num in nums:
        if num < result:
            result = num
    return result

#3. เรียงลำดับตัวเลขจากน้อยไปหามาก กำหนดให้ $number = array(1,2,31,4,15,6,7,22,9,10);
def sortMin2Max(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

#4. เรียงลำดับตัวเลขจากมากไปหาน้อย กำหนดให้ $number = array(1,2,31,4,15,6,7,22,9,10);
def sortMax2Min(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums
number = [1,2,31,4,15,6,7,22,9,10]
print(f"แสดงค่าจำนวนเต็มที่มากที่สุด = {findMax(number)}")
print(f"แสดงค่าจำนวนเต็มที่น้อยที่สุด = {findMin(number)}")
print(f"เรียงลำดับตัวเลขจากน้อยไปหามาก = {sortMin2Max(number)}")
print(f"เรียงลำดับตัวเลขจากมากไปหาน้อย = {sortMax2Min(number)}")


#5. หาจำนวนเฉพาะที่อยู่ระหว่าง 0 ถึง 500
def findPrimeNum():
    result = []
    for num in range(501):
        if num != 0:
            if ((num == 0 or num == 2 or num == 3 or num == 5 or num == 7) or 
                (num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0)):
                result.append(num)
    print(f"จำนวนเฉพาะทั้งหมด = {result}")
findPrimeNum()


#6. แสดงค่า factorial ใส่จำนวนเต็ม 5 ให้แสดงค่าของ 5! ว่ามีค่าเท่าไหร่
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(f"factorial = {factorial(5)}")
#7. จากสูตร a^2 + b^2 = c^2 ให้หาค่าด้านตรงข้ามมุมฉากของ สามเหลี่ยม โดยให้ input เป็นค่า a และ b และผลลัพธ์เป็นค่า c
def pythagorean(a, b):
    return (a**2 + b**2)**0.5

print(f"pythagorean = {pythagorean(3,4)}")
#8. โปรแกรมแปลงเลขฐาน 2 เป็น เลขฐาน 10 เช่น 0111 = 7
def binary2decimal(binary_string):
    decimal = 0
    binary_str = binary_string[::-1]
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal += 2**i
    return decimal
binary_str = "1101"
print(f"โปรแกรมแปลงเลขฐาน 2 เป็น เลขฐาน 10 = {binary2decimal(binary_str)}")
#9. โปรแกรมแปลงเลขฐาน 10 เป็น เลขฐาน 2 เช่น 30 = 11110
def decimal2binary(decimal):
    binary_str = ""
    while decimal > 0:
        binary_str = f"{decimal%2}{binary_str}"
        decimal = decimal // 2
    return binary_str

print(f"โปรแกรมแปลงเลขฐาน 10 เป็น เลขฐาน 2 = {decimal2binary(7)}")
#10. กำหนดให้ $matrixA = array(
#				array(1,2,3),
#				array(4,5,6),
#				array(7,8,9)
#			);

#			$matrixB = array(
#				array(1,1,1),
#				array(1,1,1),
#				array(1,1,1)
#			);
#	จงหาค่า $matrixA + $matrixB

matrixA = [[1,2,3],[4,5,6],[7,8,9]]
matrixB = [[1,1,1],[1,1,1],[1,1,1]]
def matrixAdd(matrixA, matrixB):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[0])):
            result[i][j] = matrixA[i][j] + matrixB[i][j]
    return result
print(f"บวกเมทริก = {matrixAdd(matrixA, matrixB)}")

#Bonus. (optional)
#แสดงผลดาว (*) ให้เป็นรูปกากบาท โดยมี input เป็นจำนวนแถวของดาว
#ตัวอย่าง
#input: 5
#result: 
#*       *
#  *   *
#    *
#  *   *
#*       *

def print_pattern(n):
    # ตรวจสอบให้ n เป็นเลขคี่ (odd number) เพราะรูปแบบที่ต้องการต้องการแถวเป็นจำนวนคี่
    if n % 2 == 0:
        print("กรุณากรอกจำนวนแถวเป็นเลขคี่")
        return
    
    mid = n // 2
    for i in range(mid + 1):
        if i == 0:
            print(" " * i + "*" + " " * (n - 2 - i * 2) + "*")
        elif i == mid:
            print(" " * i + "*")
        else:
            print(" " * i + "*" + " " * (n - 2 - 2 * i) + "*")
    
    for i in range(mid - 1, -1, -1):
        if i == 0:
            print(" " * i + "*" + " " * (n - 2 - i * 2) + "*")
        elif i == mid:
            print(" " * i + "*")
        else:
            print(" " * i + "*" + " " * (n - 2 - 2 * i) + "*")
            
# รับค่าจากผู้ใช้
n = int(input("กรุณากรอกจำนวนแถว (เลขคี่): "))
print_pattern(n)




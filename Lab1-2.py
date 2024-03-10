score = int(input("รับค่าคะแนน:"))
if score>=80 and score <=100:
    print("A")
elif score>=70 and score <=79:
    print("B")
elif score>=60 and score <=69:
    print("C")
elif score>=50 and score <=59:
    print("D")
elif score>=0 and score <=49:
    print("F")
else:
    print("กรุณารับค่าคะแนน 0-100:")
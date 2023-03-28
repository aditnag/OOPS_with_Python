# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classHeld = int(input())
classAtte = int(input())
per = classAtte / classHeld * 100
if per >= 75:
    print(f"{per} and is allowed to sit in the exam")
else:
    print(f"{per} and is not allowed to sit in the exam")


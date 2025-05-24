from delay_write import delay

def maincal():
    # تعریف متغیر برای گرفتن مقدار
    
    x= float(input('Please enter the first number : '))
    y = float(input('Please enter the second number : '))
    
    # تعریف متغیر برای محاسبات
    c1 = x + y
    c2 = x - y
    c3 = x / y
    c4 = x * y
    
    # تعریف متغیر برای نشان دادن محایبات با ماژول delay
    delay(f'The plus of numbers is {c1}')
    delay(f'The subtract of numbers is {c2}')
    delay(f'The multiplication of numbers is {c4}')
    delay(f'The division of numbers is {c3}')
 
maincal()
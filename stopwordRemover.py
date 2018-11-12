import re
from tqdm import tqdm

def remove_proNone(text):
    proNoneList=[
        "در",
        "را",
        "به",
        "از",
        "که",
        "این",
        "ایا",
        "با",
        "تا",
        "می",
        "نیز",
        "یا",
        "ما",
        "باید",
        "اند",
        "هم",
        "همچنین",
        "برای",
        "ها",
        "ان",
        "وی",
        "یک",
        "خود",
        "بر",
        "دو",
        "انها",
        "اما",
        "دیگر",
        "اگر"
        "را",
        "های",
        "و",
        "نمی",
        "هر",
        "ای",
        "زیر",
        "البته",
        "بدین",
        "چون",
        "زیرا",
        "فراوان",
        "اند",
        "اییم",
        "اید",
        "براساس",
        "قبلا",
        "یک",
        "ان",
        "بسیار",
        "ما",
        "شما",
        "اینکه"
        ]
 
        
    for key in tqdm(proNoneList):
        reText = r'\b'+key+r'\b'
        text = re.sub(reText, r'', text)
        
    return text

    
def remove_regularWords(text):
    regularWordList=[
        "است",
        "امدم",
        "امد",
        "امدن",
        "امدند",
        "امده",
        "امدی",
        "امدید",
        "امدیم",
        "اورد",
        "اوردم",
        "اوردن",
        "اوردند",
        "اورده",
        "اوردی",
        "اوردید",
        "اوردیم",
        "اورم",
        "اورند",
        "اوری",
        "اورید",
        "اوریم",
        "اید",
        "ایم",
        "ايند",
        "ایی",
        "ایید",
        "اییم",
        "باش",
        "باشد",
        "باشند",
        "باشی",
        "باشم",
        "باشید",
        "باشیم",
        "باید",
        "بتوان",
        "بتواند",
        "بتوانم",
        "بتوانی",
        "بتوانیم",
        "بتوانید",
        "بتوانند",
        "بخواه",
        "بخواهم",
        "بخواهد",
        "بخواهند",
        "بخواهی",
        "بخواهید",
        "بخواهیم",
        "بکن",
        "بکند",
        "بکنم",
        "بکنند",
        "بکنی",
        "بکنید",
        "بکنیم",
        "بگو",
        "بگوید",
        "بگویم",
        "بگویند",
        "بگویی",
        "بگویید", 
        "بگوییم",
        "بگیر",
        "بگیرد",
        "بگیرم",
        "بگیرند",
        "بگیری",
        "بگیرید",
        "بگیریم",
        "بود",
        "بودم",
        "بودن",
        "بودند",
        "بوده",
        "بودی",
        "بودید",
        "بودیم",
        "بیا",
        "بیاب",
        "بیابد",
        "بیابم",
        "بیابند",
        "بیابی",
        "بیابید",
        "بیابیم",
        "بیاور",
        "بیاورد",
        "بیاورم",
        "بیاورند",
        "بیاوری",
        "بیاورید",
        "بیاوریم",
        "بیاید",
        "بیایم",
        "بیایند",
        "بیابی",
        "بیایید",
        "بیاییم",
        "تواند",
        "توانست",
        "توانستم",
        "توانستن",
        "توانستید",
        "توانسته",
        "توانستی",
        "توانستند",
        "توانستیم",
        "توانم",
        "توانند",
        "توانی",
        "توانید",
        "توانیم",
        "خواست",
        "خواستم",
        "خواستن",
        "خواستند",
        "خواسته",
        "خواستی",
        "خواستید",
        "خواستیم",
        "خواهد",
        "خواهم",
        "خواهند",
        "خواهی",
        "خواهید",
        "خواهیم",
        "داد",
        "دار",
        "دارد",
        "دارم",
        "دارند",
        "داری",
        "دارید",
        "داریم",
        "داشت",
        "داشتم",
        "داشتن",
        "داشتند",
        "داشته",
        "داشتی",
        "داشتید",
        "داشتیم",
        "شد",
        "شده",
        "شود",
        "کرد",
        "کردم",
        "کردن",
        "کردند",
        "کرده",
        "کردی",
        "کردید",
        "کردیم",
        "کن",
        "کند",
        "کنم",
        "کنند",
        "کنی",
        "کنید",
        "کنیم",
        "گرفت",
        "گرفتم",
        "گرفتن",
        "گرفتند",
        "گرفته",
        "گرفتی",
        "گرفتید",
        "گرفتیم",
        "گفت",
        "گفتم",
        "گفتن",
        "گفتند",
        "گفته",
        "گفتی",
        "گفتید",
        "گفتیم",
        "گوید",
        "گویم",
        "گویند",
        "گویی",
        "گویید",
        "گوییم",
        "گیرد",
        "گیرم",
        "گیرند",
        "گیری",
        "گیرید",
        "گیریم",
        "هست",
        "هستم",
        "هستند",
        "هستی",
        "هستید",
        "هستیم",
        "یابد",
        "یابم",
        "یابند",
        "یابی",
        "یابید",
        "یابیم",
        "یافت",
        "یافتم",
        "یافتن",
        "یافتند",
        "یافته",
        "یافتی",
        "یافتید",
        "یافتیم",
        "برسد",
        "برسم",
        "برسی",
        "برسیم",
        "برسید",
        "برسند",
    ]
    
    for key in tqdm(regularWordList):
        reText = r'\b'+key+r'\b'
        text = re.sub(reText, r'', text)
        
    return text

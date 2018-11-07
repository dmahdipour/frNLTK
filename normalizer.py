import re
from tqdm import tqdm

def my_normalizing(normalText):
    nm_dic = {
        'ي' : 'ی',
        'ي' : 'ی',
        'ئ' : 'ی',
        'ي' : 'ی',
        'ﯤ' : 'ی',
        'ة' : 'ه',
        'ﻙ' : 'ک',
        'ﻚ' : 'ک',
        'ؤ' : 'و',
        'أ' : 'ا',
        'إ' : 'ا',
        'ٱ' : 'ا',    
        'ء' : '',
        'آ' : 'ا',
        'ِ' : '',
        '' : '',
        'َ' : '',
        'ٍ' : '',
        'ٌ' : '',
        'ً' : '',
        'ّ' : '',
        'ـ' : '',
        '{' : ' { ',
        '}' : ' } ',
        '[' : ' [ ',
        ']' : ' ] ',
        '(' : ' ( ',
        ')' : ' ) ',
        ',' : '،',
        ';' : '؛',
        '«' : ' « ',
        '»' : ' » ',
        '\u200a' : ' ',
        '\u200b' : ' ',
        '\u200c' : ' ',
        '\u200d' : ' ',
        '\u200e' : ' ',
        '\u200f' : ' ',
        '‌' : ' ',
        ':' : ':',
        ':' : ' : ',
        '!' : ' ! ',
        '?' : ' ? ',
        '؟' : ' ؟ ',
        '،' : ' ، ',
        '؛' : ' ؛ ',
        '/' : ' / ',
        '\\' : ' \\ ',
        '-' : ' ',
        '"' : ' " ',
        "'" : " ' ",
        '..' : '.',
        '.' : ' . ',
        '\n' : ' ',
        '\r' : ' ',
        '\t' : ' ',
        '\f' : ' ',
        '\v' : ' ',
        '!' : ' ! ',
        '@' : ' @ ',
        '#' : ' # ',
        '$' : ' $ ',
        '%' : ' % ',
        '^' : ' ^ ',
        '&' : ' & ',
        '*' : ' * ',
        '  ' : ' '
    }

    for key in tqdm(nm_dic):
        normalText = normalText.replace(key, nm_dic[key])

        normalText = re.sub(r'([a-zA-Z]*)(\d+)([a-zA-Z]*)', r'\1 \2 \3', normalText)

        normalText = re.sub(r'([\W\d\s]*)([ن][م][ی])([\s]+)([\w])', r'\1\2\4', normalText)
        normalText = re.sub(r'([\W\d\s]*)([م][ی])([\s]+)([\w])', r'\1\2\4', normalText)

        normalText = re.sub(r'([\w])([ه][ا][ی])([\W\d\s]+)', r'\1 \2\3', normalText)
        normalText = re.sub(r'([\w])([ه][ا][ی]$)', r'\1 \2', normalText)
        normalText = re.sub(r'([\w])([ه][ا])([\W\d\s]+)', r'\1 \2\3', normalText)
        normalText = re.sub(r'([\w])([ه][ا]$)', r'\1 \2', normalText)

        normalText = re.sub(r'([\s])([ی])([\W\d\s]+)', r' \3', normalText)

    
    return normalText


def my_tiny_normalizing(normalText):
    nm_dic1 = {
        'ي' : 'ی',
        'ي' : 'ی',
        'ئ' : 'ی',
        'ي' : 'ی',
        'ﯤ' : 'ی',
        'ة' : 'ه',
        'ﻙ' : 'ک',
        'ﻚ' : 'ک',
        'ؤ' : 'و',
        'أ' : 'ا',
        'إ' : 'ا',
        'ٱ' : 'ا',    
        'ء' : '',
        'آ' : 'ا',
        'ِ' : '',
        '' : '',
        'َ' : '',
        'ٍ' : '',
        'ٌ' : '',
        'ً' : '',
        'ّ' : '',
        'ـ' : '',
        '{' : '',
        '}' : '',
        '[' : '',
        ']' : '',
        '(' : '',
        ')' : '',
        ',' : '',
        '' : '؛',
        '«' : '',
        '»' : '',
        '\u200a' : ' ',
        '\u200b' : ' ',
        '\u200c' : ' ',
        '\u200d' : ' ',
        '\u200e' : ' ',
        '\u200f' : ' ',
        '‌' : ' ',
        ':' : '',
        ':' : '',
        '!' : '',
        '?' : '',
        '؟' : '',
        '،' : '',
        '؛' : '',
        '/' : '',
        '\\' : '',
        '-' : '',
        '–' : '',
        '"' : '',
        "'" : "",
        '..' : '',
        '.' : '',
        '\n' : ' ',
        '\r' : ' ',
        '\t' : ' ',
        '\f' : ' ',
        '\v' : ' ',
        '!' : ' ',
        '@' : ' ',
        '#' : ' ',
        '$' : ' ',
        '%' : ' ',
        '^' : ' ',
        '&' : ' ',
        '*' : ' '
    }

    for key in tqdm(nm_dic1):
        normalText = normalText.replace(key, nm_dic1[key])

        normalText = re.sub(r'([a-zA-Z]*)(\d+)([a-zA-Z]*)', r'\1 \2 \3', normalText)

        normalText = re.sub(r'([\w])([ه][ا][ی])([\W\d\s]+)', r'\1\3', normalText)
        normalText = re.sub(r'([\w])([ه][ا][ی]$)', r'\1', normalText)
        normalText = re.sub(r'([\w])([ه][ا])([\W\d\s]+)', r'\1\3', normalText)
        normalText = re.sub(r'([\w])([ه][ا]$)', r'\1', normalText)

        normalText = re.sub(r'([\s])([ی])([\W\d\s]+)', r' \3', normalText)

    
    return normalText
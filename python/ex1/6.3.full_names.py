
def full_names(first_names, last_names, min_len =0):
    return [ str.title(f_name+" " + l_name) for f_name in first_names for l_name in last_names if len(f_name )+len(l_name)+1 >= min_len ]


first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']

# התנאים הבאים צריכים להתקיים
a1 = full_names(first_names, last_names, 10) == ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi']
a2 = full_names(first_names, last_names) == ['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi']
print(a1 and a2)

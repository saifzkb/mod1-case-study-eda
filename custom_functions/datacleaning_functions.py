

def remove_postfix(column1):
    column1=column1.str.replace('+','')
    column1=column1.str.replace(',','')
    column1=column1.str.replace('$','')
    column1=column1.str.replace("''","")
    return column1


def to_float(column2):
    column2=column2.astype('float')
    return column2


def to_date_time(column3):
    column3=pd.to_datetime(column3)
    return column3




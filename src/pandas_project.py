import re

def clean_years(year):
    if year == 0 :
        year = '0000'
        return(year)
    else:
        return year

def clean_date(date):
        a = re.findall(r'\w*\s*\d{2}-\w{3}-\d{2,4}', date)
        b = re.findall(r'[A-Za-z]{3}-', date)
        c = re.findall(r'\d{4}', date)
        
        if a:
            if re.findall(r'\w*\s*\d{2}-\w{3}-\d{4}', str(a)):
                i = a[0]
                j = re.findall(r'\d{2}-\w{3}-',i)
                return(j[0])
            elif re.findall(r'\w*\s*\d{2}-\w{3}-\d{2}', str(a)):
                i = a[0]
                j = re.findall(r'\d{2}-\w{3}-',i)
                return(j[0])
            elif re.findall(r'\d{2}-\w{3}', str(a)):
                return a[0]
            elif re.findall(r'\d{2}-\w{3}', str(a)):
                i = a[0]
                j = re.findall(r'\d{2}-\w{3}-',i)
                return(j[0])
        if b:
            return('01-' + b[0])
        if c:
            return('01-Jan-')
        else:
            return date


def trans_date(date):
    a = re.findall(r'\d{2}-\w{3}-', date)
    if a:
        i = re.findall(r'\w{3}', str(a))
        
        if i[0] == str('Jan'):
            j = i[0]
            j = a[0].replace('Jan', '01')
            return j
        elif i[0] == str('Feb'):
            j = i[0]
            j = a[0].replace('Feb', '02')
            return j
        elif i[0] == str('Mar'):
            j = i[0]
            j = a[0].replace('Mar', '03')
            return j
        elif i[0] == str('Apr'):
            j = i[0]
            j = a[0].replace('Apr', '04')
            return j
        elif i[0] == str('May'):
            j = i[0]
            j = a[0].replace('May', '05')
            return j
        elif i[0] == str('Jun'):
            j = i[0]
            j = a[0].replace('Jun', '06')
            return j
        elif i[0] == str('Jul'):
            j = i[0]
            j = a[0].replace('Jul', '07')
            return j
        elif i[0] == str('Aug'):
            j = i[0]
            j = a[0].replace('Aug', '08')
            return j
        elif i[0] == str('Sep'):
            j = i[0]
            j = a[0].replace('Sep', '09')
            return j
        elif i[0] == str('Oct'):
            j = i[0]
            j = a[0].replace('Oct', '10')
            return j
        elif i[0] == str('Nov'):
            j = i[0]
            j = a[0].replace('Nov', '11')
            return j
        elif i[0] == str('Dec'):
            j = i[0]
            j = a[0].replace('Dec', '12')
            return j

def clean_injury(injury):
    no_injurys = re.findall(r'([N,n]o [I,i]njury[s]?|Minor injury|Minor injuries|minor injuries|Survived)', str(injury))
    leg = re.findall(r'(leg|Leg|LEG|Thigh|THIGH|thigh|calf|CALF|Calf|Knee|knee|KNEE)', str(injury))
    arm = re.findall(r'(arm|Arm|ARM)', str(injury))
    foot = re.findall(r'(foot|Foot|FOOT|ankle|ANKLE|Ankle|heel|HEEL|Heel|Toe|toe|feet|FEET|Feet)', str(injury))
    hand = re.findall(r'(hand|Hand|HAND|Finger|FINGER|finger)', str(injury))
    head = re.findall(r'(head|Head|HEAD)', str(injury))
    cheast = re.findall(r'(Chest|chest|CHEST|Torso|TORSO|torso|Back|back)', str(injury))
    
    
    if no_injurys:
        return 'No Injury'
    elif leg:
        return 'Leg Injury'
    elif arm:
        return 'Arm Injury'
    elif foot:
        return 'Foot Injury'
    elif hand:
        return 'Hand Injury'
    elif head:
        return 'Head Injury'
    elif cheast:
        return 'Chest Injury'
    else:
        return 'Indeterminate Injury'


def clean_hour(hour):
        a = re.findall(r'\d{2}\w?\d{2}', str(hour))
        night = re.findall(r'(night|Night|NIGHT|dark|Dark|DARK|dusk|Dusk|sunset|Sunset|sundown)', str(hour))
        afternoon = re.findall(r'(noon|Noon|NOON|non|P.M.|pm|PM|Midday)', str(hour))
        morning = re.findall(r'(morning|Morning|AM|A.M|am|dawn|Dawn)', str(hour))
        evening = re.findall(r'(evening|Evening)', str(hour))
        
        if a:
            j = a[0]
            j = j.split('h')
            j = j[0]
            if '00' <= j <= '12':
                return 'Morning'
            elif '12' <= j <= '17':
                return 'Afternoon'
            elif '17' <= j <= '21':
                return 'Evening'
            elif '21' <= j <= '24':
                return 'Night'
        elif night:
            return 'Night'
        elif afternoon:
            return 'Afternoon'
        elif morning:
            return 'Morning'
        elif evening:
            return 'Evening'
        else:
            return 'Indeterminate'

def clean_age(age):
    a = re.findall(r'\d{1,2}', str(age))
    if a:
        i = [int(sublista) for sublista in a]
        b = sum([int(sublista) for sublista in a]) / len(i)
        return int(b)
    else:
        return 0
def frequency(lst):
    dict = {}
    for getal in lst:
        if getal in dict:
            dict[getal]+=1
        else:
            dict[getal] = 1
    return dict

grades = [100,95,95,101,100,102]
frequency(grades)
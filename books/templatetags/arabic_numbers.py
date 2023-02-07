from django import template

register = template.Library()


@register.filter(name='enToArNumb')
def enToArNumb(numbers): 

    dic = { 
        '0':'۰', 
        '1':'١', 
        '2':'٢', 
        '3':'۳', 
        '4':'٤', 
        '5':'٥', 
        '6':'٦', 
        '7':'۷', 
        '8':'۸', 
        '9':'۹', 
        #.:'۰', 
    }
    numbers = str(numbers)
    ar_numbers = ""
    for number in numbers:
      ar_number = dic.get(number)
      ar_numbers = ar_numbers + ar_number
    return ar_numbers
  #else: 
    #print("we are here")
    #print (number)
    #return "not int"

height = eval( input() )

while height != -9999:
    weight = eval( input() )
    BMI = weight/(height/100)**2
    print("BMI: {:.2f}".format(BMI))
    if BMI <18.5:
        print("State: under weight")
    elif 18.5 <= BMI < 25:
        print("State: normal")
    elif 25.0 <= BMI < 30:
        print("State: over weight")
    elif 30 <= BMI:
        print("State: fat")

    height=eval( input() )
        

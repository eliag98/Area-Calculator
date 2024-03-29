import math

def empty_line():
    print("")

def reload():
    app()

def ask_for_reload():
    empty_line()
    print("Do you have another calculation?")
    print("1. Yes. Reload the program")
    print("2. No. I have finished")
    empty_line()
    answer = input("Response: ")
    if answer == "1" :
        reload()
    elif answer == "2":
        empty_line()
        print("##############################################################")
        print("Thank you for using our software. Press any key to continue...")
        p = input("##############################################################")
        empty_line()
    else:
        print("Please choose an option from above: ")
        ask_for_reload()

def square_area():
    square_d = input("Please enter the one diagonal of the square: ")
    try:
        empty_line()
        f_square_d = float(square_d)
        square_area_calc = f_square_d * f_square_d
        sresult = " ==> The Square area calculated is: " + str(square_area_calc) + " <== "
        print("#"*len(sresult))
        print(sresult)
        print("#"*len(sresult))
        ask_for_reload()
    except:
        empty_line()
        print("### Wrong input ... Please provide a number ###")
        empty_line()
        square_area()

def rectangle_area():
    rec_dia_l = input("Please enter the length diagonal of the rectangle: ")
    rec_dia_h = input("Please enter the height diagonal of the rectangle: ")
    try:
        empty_line()
        f_rec_dia_l = float(rec_dia_l)
        f_rec_dia_h = float(rec_dia_h)
        if f_rec_dia_l == f_rec_dia_h:
            print("This is a sqaure!!")
            empty_line()
            rectangle_area_calc = f_rec_dia_l * f_rec_dia_h
            rresult = " ==> The Square area calculated is: " + str(rectangle_area_calc) + " <== "
        else:
            rectangle_area_calc = f_rec_dia_l * f_rec_dia_h
            rresult = " ==> The Rectangle area calculated is: " + str(rectangle_area_calc) + " <== "
        print("#"*len(rresult))
        print(rresult)
        print("#"*len(rresult))
        ask_for_reload()
    except:
        empty_line()
        print("### Wrong input ... Please provide a number ###")
        empty_line()
        rectangle_area()

def circle_area():
    radius = input("Please enter the radius of the circle: ")
    try:
        empty_line()
        f_radius = float(radius)
        circle_area_calc = math.pi* f_radius* f_radius
        print(type(circle_area_calc))
        cresult = " ==> The Circle area calculated is: " + str(circle_area_calc) + " <== "
        print("#"*len(cresult))
        print(cresult)
        print("#"*len(cresult))
        ask_for_reload()
    except:
        empty_line()
        print("### Wrong input ... Please provide a number ###")
        empty_line()
        circle_area()

def main_choices():
    empty_line()
    print("Here you can calculate the area of:")
    print("A. Square")
    print("B. Rectangle")
    print("C. Circle")
    empty_line()
    global user_choice
    user_choice = input("Please type A, B or C to proceed to the selected calculation: ")
    empty_line()
    if user_choice == "A" :
        square_area()
    elif user_choice == "B":
        rectangle_area()
    elif user_choice == "C":
        circle_area()
    else:
        print("Please choose one of the choices.")
        main_choices()

def app():
    empty_line()
    print("Hello and welcome to the Area Calculator")
    print("----------------------------------------")
    main_choices()

app()


### Made By Elia ###
### email: eliework98@gmail.com ###

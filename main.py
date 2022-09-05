print("Система расчёта штрафов")

car_speed = 170
is_town = True

fine_for_1_to_10 = 20
fine_for_11_to_15 = 40
fine_for_16_to_20 = 60
fine_for_21_to_25 = 100
fine_for_26_to_30 = 150
fine_for_31_to_40 = 200
fine_for_41_to_50 = 320
fine_for_51_to_60 = 480
fine_for_61_to_70 = 600
fine_for_71_and_more = 700

town_speed = 50
country_speed = 70

if is_town:
    over_speed = car_speed - town_speed
else:
    over_speed = car_speed - country_speed

if over_speed < 1:
    print("Скорость не превышена или превышена незначительно")
elif 1 <= over_speed < 10:
    print("Штраф:" + str(fine_for_1_to_10) + "Евро")
elif 11 <= over_speed < 15:
    print("Штраф: " + str(fine_for_11_to_15)+ "Евро")
elif 16 <= over_speed < 20:
    print("Штраф: " + str(fine_for_16_to_20)+ "Евро")
elif 21 <= over_speed < 25:
    print("Штраф: " + str(fine_for_21_to_25)+ "Евро")
elif 26 <= over_speed < 30:
    print("Штраф: " + str(fine_for_26_to_30)+ "Евро")
elif 31 <= over_speed < 40:
    print("Штраф: " + str(fine_for_31_to_40)+ "Евро")
elif 41 <= over_speed < 50:
    print("Штраф: " + str(fine_for_41_to_50)+ "Евро")
elif 51 <= over_speed < 60:
    print("Штраф: " + str(fine_for_51_to_60)+ "Евро")
elif 61 <= over_speed < 70:
    print("Штраф: " + str(fine_for_61_to_70)+ "Евро")
elif over_speed >= 70:
    print("Штраф: " + str(fine_for_71_and_more)+ "Евро")

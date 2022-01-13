presion = float(input("Introduzca la presión en kiloPascales: "))
p_p_i_kp = presion / 6.89476
mmhg_kp = presion * 7.50062
atm_kp = presion / 0.00986923
r_p = round(p_p_i_kp, 2)
r_m = round(mmhg_kp, 2)
r_a = round(atm_kp, 2)
print("El equivalente es: " + str(r_p) + " libra por pulgada^2,", str(r_m) + " mm de Hg,", str(r_a) + " atm.")

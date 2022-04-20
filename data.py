class Data:
    modules = []
    def __init__(self, type, global_name, local_name, human_name=None) -> None:
        self.type = type
        self.global_name = global_name
        self.local_name = local_name
        self.human_name = human_name
        Data.modules.append(self)




# Data("Натуральные числа", "P-1", "NZER_N_B")
# Data("Натуральные числа", "P-2", "COM_NN_D")
# Data("Натуральные числа", "P-3", "ADD_1N_N")
# Data("Натуральные числа", "P-4", "ADD_NN_N")
# Data("Натуральные числа", "P-5", "SUB_NN_N")
# Data("Натуральные числа", "P-6", "MUL_ND_N")
# Data("Натуральные числа", "P-7", "MUL_Nk_N")
# Data("Натуральные числа", "P-8", "MUL_NN_N")
# Data("Натуральные числа", "P-9", "SUB_NDN_N")
# Data("Натуральные числа", "P-10", "DIV_NN_Dk")
# Data("Натуральные числа", "P-11", "DIV_NN_N")
# Data("Натуральные числа", "P-12", "MOD_NN_N")
# Data("Натуральные числа", "P-13", "GCF_NN_N")
# Data("Натуральные числа", "P-14", "LCM_NN_N")

# Data("Целые числа", "Z-1", "ABS_Z_N")
# Data("Целые числа", "Z-2", "POZ_Z_D")
# Data("Целые числа", "Z-3", "MUL_ZM_Z")
# Data("Целые числа", "Z-4", "TRANS_N_Z")
# Data("Целые числа", "Z-5", "TRANS_Z_N")
# Data("Целые числа", "Z-6", "ADD_ZZ_Z")
# Data("Целые числа", "Z-7", "SUB_ZZ_Z")
# Data("Целые числа", "Z-8", "MUL_ZZ_Z")
# Data("Целые числа", "Z-9", "DIV_ZZ_Z")
# Data("Целые числа", "Z-10", "MOD_ZZ_Z")

# Data("Рациональные числа", "Q-1", "RED_Q_Q")
# Data("Рациональные числа", "Q-2", "INT_Q_B")
# Data("Рациональные числа", "Q-3", "TRANS_Z_Q")
# Data("Рациональные числа", "Q-4", "TRANS_Q_Z")
# Data("Рациональные числа", "Q-5", "ADD_QQ_Q")
# Data("Рациональные числа", "Q-6", "SUB_QQ_Q")
# Data("Рациональные числа", "Q-7", "MUL_QQ_Q")
# Data("Рациональные числа", "Q-8", "DIV_QQ_Q")

Data("Многочлены", "P-1", "ADD_PP_P")
Data("Многочлены", "P-2", "SUB_PP_P")
Data("Многочлены", "P-3", "MUL_PQ_P")
Data("Многочлены", "P-4", "MUL_Pxk_P")
Data("Многочлены", "P-5", "LED_P_Q")
Data("Многочлены", "P-6", "DEG_P_N")
Data("Многочлены", "P-7", "FAC_P_Q")
Data("Многочлены", "P-8", "MUL_PP_P")
Data("Многочлены", "P-9", "DIV_PP_P")
Data("Многочлены", "P-10", "MOD_PP_P")
Data("Многочлены", "P-11", "GCF_PP_P")
Data("Многочлены", "P-12", "DER_P_P")
Data("Многочлены", "P-13", "NMR_P_P")


for i in Data.modules:
    print(f'\n{{"system_name":"{i.local_name}" ,\n"human_name": 321}},')
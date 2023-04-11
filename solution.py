import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    # Рассчитываем пропорции для каждой выборки
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    # Рассчитываем объединенную пропорцию
    p_combined = (x_success + y_success) / (x_cnt + y_cnt)
    
    # Рассчитываем статистику теста
    z = (p1 - p2) / np.sqrt(p_combined * (1 - p_combined) * (1 / x_cnt + 1 / y_cnt))
    
    # Рассчитываем двухсторонний p-value
    p_value = 2 * (1 - norm.cdf(abs(z)))
    
    # Сравниваем p-value с уровнем значимости и принимаем решение
    alpha = 0.08
    return p_value < alpha
   

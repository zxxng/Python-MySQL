
import pandas as pd

name_series = pd.Series(['김수안', '김수정', '박동윤', '강이안', '강지안'])
age_series = pd.Series([19, 23, 22, 19, 16])
gender_series = pd.Series(['여', '여', '남', '여', '남'])
grade_series = pd.Series([4.35, 4.23, 4.25, 4.37, 4.25])
print(name_series, age_series, gender_series, grade_series)

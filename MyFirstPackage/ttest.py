# user_df : DataFrame Name
# col : x axis column
# value : y axis column
# group1, group2 : col (x column) 기준으로 분류된 이름

import seaborn as sns
from statannot import add_stat_annotation
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')  
plt.rcParams['axes.unicode_minus'] = False

import warnings
warnings.filterwarnings('ignore')


def ttest_auto(user_df, col, value, group1, group2):
    f1 = sns.boxplot(data=user_df, x=col, y = value, palette='pastel')
    f2 = sns.stripplot(data=user_df, x=col, y = value, alpha=.5, color='r')

    add_stat_annotation(f1, data=user_df, x =col, y = value,
                        box_pairs=[((group1), (group2))],
                        test='t-test_ind', text_format='star', loc='inside', verbose=2)
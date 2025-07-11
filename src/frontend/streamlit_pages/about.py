import streamlit as st

st.set_page_config(page_title="About")

st.title("О приложении")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ссылки на проект")
    st.markdown("[Репозиторий проекта](https://github.com/digreen17/ab_calculator)")

with col2:
    st.subheader("Прочие ссылки")
    st.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")
    st.markdown("[Telegram](https://t.me/digreen_17)")

st.markdown("---")  


table_md = """
### Приложение включает в себя:

#### 1. Sample-size calculator  
Калькулятор минимального числа наблюдений в каждой группе эксперимента.

**Параметры ввода**

| Поле | Что означает |
|------|--------------|
| **Metric type** | `continuous`  непрерывная метрика <br> `binary` бинарная метрика |
| **MDE (%)** | Минимально детектируемый эффект в процентах |
| **Power (1−β)** | Вероятность обнаружить эффект, если он существует |
| **Alpha (α)** | Уровень статистической значимости  |

Если выбран тип метрики **`continuous`** дополнительно укажите:

| Поле | Что означает |
|------|--------------|
| **Mean** | ожидаемое среднее значение |
| **Standard deviation**  | стандартное отклонение |

Если распределение асимметрично, отметьте чекбокс **Data is skewed?** — расчёт применит поправку.

Если выбран тип метрики **`binary`** дополнительно укажите:

| Поле | Что означает |
|------|--------------|
| **p** | наблюдаемая вероятность успеха для бинарной метрики |

"""

st.markdown(table_md, unsafe_allow_html=True)



st.markdown(
    """
1. Заполните параметры выше.  
2. Внизу появится значение **Minimum sample size** —
   минимальное число наблюдений в каждой группе.
"""
)

st.divider()
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Репозиторий проекта")
    st.markdown("- [GitHub](https://github.com/digreen17/ab_calculator)")

import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы
st.set_page_config(page_title="VAPS - Digital Finance", layout="wide")

st.title("🛡️ VAPS: Цифровой Вавилон")
st.markdown("### Интеллектуальный помощник по финансовой грамотности")

# Боковая панель (Ввод данных)
st.sidebar.header("📥 Ввод данных")
income = st.sidebar.number_input("Ваш доход за месяц (тг):", min_value=0, value=200000)
savings_target = income * 0.1  # Золотое правило: отложи 10%

st.sidebar.subheader("Расходы")
food = st.sidebar.slider("Еда", 0, 100000, 40000)
rent = st.sidebar.slider("Аренда/Жилье", 0, 150000, 80000)
leisure = st.sidebar.slider("Развлечения", 0, 50000, 25000)
other = st.sidebar.slider("Прочее", 0, 50000, 10000)

# Логика расчетов
total_expenses = food + rent + leisure + other
balance = income - total_expenses

# Основная область
col1, col2, col3 = st.columns(3)
col1.metric("Общий расход", f"{total_expenses} ₸", delta=f"{total_expenses/income:.1%}", delta_color="inverse")
col2.metric("Остаток", f"{balance} ₸")
col3.metric("Совет Вавилона (10%)", f"{savings_target} ₸")

# Визуализация
st.subheader("📊 Аналитика бюджета")
df = pd.DataFrame({
    "Категория": ["Еда", "Аренда", "Развлечения", "Прочее", "Свободно"],
    "Сумма": [food, rent, leisure, other, max(0, balance)]
})
fig = px.pie(df, values='Сумма', names='Категория', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig, use_container_width=True)

# Блок финансовой грамотности (ИИ-рекомендации)
st.subheader("💡 Персональные рекомендации")
if balance < savings_target:
    st.error(f"⚠️ Твои расходы слишком велики! Ты не можешь отложить 10% ({savings_target} ₸).")
    st.info("**Урок из Вавилона:** Контролируй свои траты. То, что ты называешь 'необходимыми расходами', всегда растет пропорционально твоим доходам, если ты не сопротивляешься этому.")
else:
    st.success(f"✅ Отлично! Ты соблюдаешь закон богатства. {int(savings_target)} ₸ отправлены в накопления.")

# Финансовая цель
st.subheader("🎯 Прогресс цели: Накопить на обучение")
goal = 500000
current_saved = 125000 + (max(0, balance) * 0.5)
progress = min(1.0, current_saved / goal)
st.progress(progress)
st.write(f"Собрано {int(current_saved)} из {goal} ₸ ({progress:.1%})")

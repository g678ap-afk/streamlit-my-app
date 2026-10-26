import streamlit as st

st.set_page_config(
    page_title="Мій Супер-додаток",
    page_icon="https://img.icons8.com/nolan/1200/bongo-cat.jpg",
    layout="wide"
)

st.title("Ласкаво просимо до мого додатку")

tab1, tab2, tab3 = st.tabs(["Про Мене", "Мій Інструмент", "🔗 Корисні посилання"])

with tab1:
    st.header("Знайомство з Автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZPba5Sodo2n8VmVdnMzzgkTP3-zqTYcB19pgepSn8iLrQcqFbIm6Y19k&s=10.png",
            caption="Я",
            width=300
        )
    with col2:
        st.subheader("Привіт, я майбутній Python Developer")
        st.write("Я навчаюсь в Малій Академії IT STEP. Створюю круті веб-додатки")
        with st.container():
            st.info("Контакти для зв'язку")
            st.markdown("- GitHub: [Мій профіль](https://github.com)")
            st.markdown("- E-Mail: student@itstep.org")

with tab2:
    st.info("Ця вкладка у розробці")

with tab3:
    st.header("🔗 Корисні посилання")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Навчальні сайти
        - 🐍 [Python.org](https://www.python.org/) — офіційний сайт Python
        - 📖 [W3Schools Python](https://www.w3schools.com/python/) — уроки з Python
        - 🎓 [freeCodeCamp](https://www.freecodecamp.org/) — безкоштовні курси
        - 💡 [Real Python](https://realpython.com/) — якісні статті та туторіали
        """)
    
    with col2:
        st.markdown("""
        ### 🎮 Ігри та практика
        - 🧩 [Codewars](https://www.codewars.com/) — завдання з програмування
        - 🏆 [LeetCode](https://leetcode.com/) — алгоритми та задачі
        - 🎯 [HackerRank](https://www.hackerrank.com/) — практика кодингу
        - 🕹️ [CodeCombat](https://codecombat.com/) — вчимося через гру
        """)
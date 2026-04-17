import streamlit as st
import g4f

st.set_page_config(page_title="مساعد المراجعة الذكي", page_icon="📚")
st.title("📚 أستاذ المراجعة بالدارجة")

lesson_input = st.text_area("لصق الدرس ديالك هنا:", height=200)

if st.button("لخص ليا الدرس ✨"):
    if lesson_input:
        with st.spinner('جاري التحليل...'):
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    provider=g4f.Provider.Blackbox,
                    messages=[{"role": "user", "content": f"لخص هاد الدرس بدارجة مغربية وعطيني 3 أسئلة: {lesson_input}"}],
                )
                st.success("ها هو التلخيص والأسئلة:")
                st.write(response)
            except Exception as e:
                st.error(f"وقع مشكل: {e}")
    else:
        st.warning("عفاك حط النص أولاً!")

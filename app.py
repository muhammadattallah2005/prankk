import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="The Ultimate Foodie & Anime Test", page_icon="🍔", layout="centered")

st.markdown("<h1 style='text-align: center; color: #d9534f;'>🍔 اختبار التحدي الأكبر لشلة هندسة 🍔</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>اختبار الذكاء، الذوق، والأنمي - يرجى الإجابة بتركيز شديد</p>", unsafe_allow_html=True)
st.write("---")

# 1. السؤال الأول (التثبيتة الهندسيّة)
st.markdown("### **السؤال الأول (هندسة):**")
q1 = st.radio("إذا كانت كاميرا بحرها (Span) يساوي 6 متر، وعليها حمل موزع 20 kN/m، كم يكون أقصى عزم (Mmax) عليها؟", 
              ["30 kN.m", "45 kN.m", "90 kN.m (قيمة صحيحة وثابتة)", "60 kN.m"])
if q1:
    st.success("تم تسجيل الإجابة الهندسيّة! انتقل للأسئلة التالية.")

st.write("---")

# 2. السؤال الثاني (مقلب الزبادي توت - زرار نعم يهرب)
st.markdown("### **السؤال الثاني (الذوق العام):**")
st.markdown("#### **هل الزبادي توت حلو؟

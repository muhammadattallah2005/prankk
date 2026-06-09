import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="The Ultimate Foodie Legend Test", page_icon="🍔", layout="centered")

st.markdown("<h1 style='text-align: center; color: #d9534f;'>🍔 اختبار أسطورة الأكل الحقيقي 🍔</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>اختبار تحديد الهوية والذوق العام لشلة هندسة</p>", unsafe_allow_html=True)
st.write("---")

# السؤال الأول (التثبيتة الهندسيّة عشان يصدقوا)
st.markdown("### **السؤال الأول:**")
q1 = st.radio("إذا كانت كاميرا بحرها (Span) يساوي 6 متر، وعليها حمل موزع 20 kN/m، كم يكون أقصى عزم (Mmax) عليها؟", 
              ["30 kN.m", "45 kN.m", "90 kN.m (قيمة صحيحة وثابتة)", "60 kN.m"])

if q1:
    st.success("إجابة مسجلة بنجاح! انتقل الآن للسؤال التالي والأهم.")
    st.write("")

st.write("---")

# السؤال الثاني المعدل والمضبوط (خناقة الأكل)
st.markdown("### **السؤال الثاني (سؤال الذوق والسرعة):**")
st.markdown("#### **مين هو الأسطورة الحقيقي واللي ذوقه دايماً أحسن في الأكل؟**")

# الكود المطور لقلب زرار رغد سحرياً وتعديل الاستجابة على التليفون
html_code = """
<div style="position: relative; height: 280px; width: 100%; border: 2px solid #d9534f; border-radius: 12px; background-color: #fffdf9; padding: 20px; box-shadow: inset 0 0 10px rgba(0,0,0,0.05);">
    
    <!-- زرار محمد (البطل) -->
    <button id="mohamed_btn" onclick="showResult()" style="
        position: absolute; 
        left: 15%; 
        top: 80px; 
        background-color: #337ab7; 
        color: white; 
        border: none;
        padding: 15px 40px; 
        font-size: 18px; 
        font-weight: bold;
        border-radius: 30px; 
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        transition: transform 0.1s;">
        محمد 😎
    </button>

    <!-- زرار رغد (المتغير والمتحول) -->
    <button id="raghad_btn" onmouseover="transformButton()" ontouchstart="transformButton()" onclick="transformButton()" style="
        position: absolute; 
        left: 55%; 
        top: 80px; 
        background-color: #f05454; 
        color: white; 
        border: none;
        padding: 15px 40px; 
        font-size: 18px; 
        font-weight: bold;
        border-radius: 30px; 
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        transition: all 0.1s ease-in-out;">
        رغد 🌸
    </button>
    
    <!-- رسالة النتيجة النهائية المضبوطة -->
    <div id="final_result" style="
        text-align: center; 
        padding-top: 170px; 
        font-size: 20px; 
        font-weight: bold; 
        color: #d9534f; 
        display: none;
        line-height: 1.6;">
        🎉 ذكاء خارق واعتراف تاريخي لا مفر منه! 🎉<br>
        تم تسجيل الإجابة وتوثيقها: محمد هو أسطورة الأكل الرسمي والوحيد في الشلة، بذوقه العالي وبإقرار صريح من رغد وباقي المقاطعة! 🍔 تفضلوا بقبول فائق الاحترام لذوق القيادة! 🚀
    </div>
</div>

<script>
function transformButton() {
    var btn = document.getElementById('raghad_btn');
    btn.innerHTML = "محمد برضه 😎";
    btn.style.backgroundColor = "#337ab7";
    btn.style.left = "45%";
}

function showResult() {
    document.getElementById('final_result').style.display = 'block';
    document.getElementById('raghad_btn').style.display = 'none';
    document.getElementById('mohamed_btn').style.display = 'none';
}
</script>
"""

# تشغيل المقلب المطور
components.html(html_code, height=330)

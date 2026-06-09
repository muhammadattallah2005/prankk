import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="Civil Engineering IQ Test", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2b580c;'>🧠 اختبار الذكاء والتركيز الهندسي 🧠</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777;'>خاص بشلة هندسة أسيوط - يرجى الإجابة بتركيز</p>", unsafe_allow_html=True)
st.write("---")

# السؤال الأول (التثبيتة الهندسيّة)
st.markdown("### **السؤال الأول:**")
q1 = st.radio("إذا كانت كاميرا بحرها (Span) يساوي 6 متر، وعليها حمل موزع 20 kN/m، كم يكون أقصى عزم (Mmax) عليها؟", 
              ["30 kN.m", "45 kN.m", "90 kN.m (قيمة صحيحة وثابتة)", "60 kN.m"])

if q1:
    st.success("إجابة مسجلة! انتقل للسؤال التالي المعتمد على الذكاء الاجتماعي الإنشائي.")
    st.write("")

st.write("---")

# السؤال الثاني المعدل (خناقة الأكل)
st.markdown("### **السؤال الثاني (سؤال السرعة والبديهة):**")
st.markdown("#### **مين هو الأسطورة الحقيقي واللي ذوقه دايماً أحسن في الأكل؟**")

# الكود السحري لقلب زرار رغد إلى محمد
html_code = """
<div style="position: relative; height: 300px; width: 100%; border: 2px solid #2b580c; border-radius: 10px; background-color: #fafafa; padding: 20px;">
    
    <button id="mohamed_btn" onclick="showResult()" style="
        position: absolute; 
        left: 20%; 
        top: 80px; 
        background-color: #4f98ca; 
        color: white; 
        border: none;
        padding: 15px 45px; 
        font-size: 20px; 
        font-weight: bold;
        border-radius: 8px; 
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        محمد 😎
    </button>

    <button id="raghad_btn" onmouseover="transformButton()" onclick="transformButton()" style="
        position: absolute; 
        left: 55%; 
        top: 80px; 
        background-color: #f67280; 
        color: white; 
        border: none;
        padding: 15px 45px; 
        font-size: 20px; 
        font-weight: bold;
        border-radius: 8px; 
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.2s ease;">
        رغد 🌸
    </button>
    
    <div id="final_result" style="
        text-align: center; 
        padding-top: 180px; 
        font-size: 22px; 
        font-weight: bold; 
        color: #2b580c; 
        display: none;
        line-height: 1.6;">
        🎉 ذكاء خارق واعتراف تاريخي! 🎉<br>
        تم تسجيل الإجابة بنجاح: محمد هو أسطورة الأكل الرسمي والوحيد في الشلة، برغبة وإقرار من رغد ومريم وباقي المقاطعة! 🥳 تفضلوا بقبول فائق الاحترام لكرش القيادة! 🍔🚀
    </div>
</div>

<script>
// دالة تحويل الزرار سحرياً
function transformButton() {
    var btn = document.getElementById('raghad_btn');
    
    // تغيير النص المكتوب على الزرار
    btn.innerHTML = "محمد برضه 😎";
    
    // تغيير لون الزرار عشان يبقى زي زرار محمد التاني
    btn.style.backgroundColor = "#4f98ca";
    
    // نقل الزرار شوية عشان الحركة تبان صياعة وميلمسوش رغد خالص
    btn.style.left = "50%";
}

function showResult() {
    document.getElementById('final_result').style.display = 'block';
    document.getElementById('raghad_btn').style.display = 'none';
    document.getElementById('mohamed_btn').style.display = 'none';
}
</script>
"""

# تشغيل المقلب
components.html(html_code, height=350)

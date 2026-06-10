import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="The Ultimate Foodie & Anime Test", page_icon="🍔", layout="centered")

st.markdown("""<h1 style='text-align: center; color: #d9534f;'>🍔 اختبار التحدي الأكبر لشلة هندسة 🍔</h1>""", unsafe_allow_html=True)
st.markdown("""<p style='text-align: center; color: #666;'>اختبار الذكاء، الذوق، والأنمي - يرجى الإجابة بتركيز شديد</p>""", unsafe_allow_html=True)
st.write("---")

# 1. السؤال الأول (هندسة)
st.markdown("""### **السؤال الأول (هندسة):**""")
q1 = st.radio("إذا كانت كاميرا بحرها (Span) يساوي 6 متر، وعليها حمل موزع 20 kN/m، كم يكون أقصى عزم (Mmax) عليها؟", 
              ["30 kN.m", "45 kN.m", "90 kN.m (قيمة صحيحة وثابتة)", "60 kN.m"])
if q1:
    st.success("تم تسجيل الإجابة الهندسيّة! انتقل للأسئلة التالية.")

st.write("---")

# 2. السؤال الثاني (الزبادي توت)
st.markdown("""### **السؤال الثاني (الذوق العام):**""")
st.markdown("""#### **هل الزبادي توت حلو؟ 🍧**""")

html_zabadi = """
<div style="position: relative; height: 180px; width: 100%; border: 1px solid #ddd; border-radius: 8px; background-color: #fff; padding: 10px;">
    <button id="yes_zabadi" onmouseover="moveZabadi()" ontouchstart="moveZabadi()" onclick="moveZabadi()" style="position: absolute; left: 25%; top: 50px; background-color: #28a745; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 20px; cursor: pointer;">نعم 👍</button>
    <button onclick="alert('تم تسجيل إجابتك: الزبادي توت وحش فعلاً ❌')" style="position: absolute; left: 60%; top: 50px; background-color: #dc3545; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 20px; cursor: pointer;">لأ طبعاً 🤮</button>
</div>
<script>
function moveZabadi() {
    var btn = document.getElementById('yes_zabadi');
    btn.style.left = (Math.random() * (window.innerWidth - 150)) + 'px';
    btn.style.top = (Math.random() * 100) + 'px';
}
</script>
"""
components.html(html_zabadi, height=200)

st.write("---")

# 3. السؤال الثالث الجديد (مقلب الشاي - زرار حلو يهرب)
st.markdown("""### **السؤال الثالث (الكيف الهندسي):**""")
st.markdown("""#### **طعم الشاي نتن ولا حلو؟ ☕**""")

html_tea = """
<div style="position: relative; height: 180px; width: 100%; border: 1px solid #ddd; border-radius: 8px; background-color: #fff; padding: 10px;">
    <!-- زرار حلو اللي بيهرب -->
    <button id="sweet_tea" onmouseover="moveTea()" ontouchstart="moveTea()" onclick="moveTea()" style="position: absolute; left: 25%; top: 50px; background-color: #28a745; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 20px; cursor: pointer;">حلو وزي الفل 😍</button>
    
    <!-- زرار نتن الثابت -->
    <button onclick="alert('تم تسجيل إجابتك: الشاي نتن ومالوش عازة ❌')" style="position: absolute; left: 60%; top: 50px; background-color: #ba7a3a; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 20px; cursor: pointer;">نتن 🤮</button>
</div>
<script>
function moveTea() {
    var btn = document.getElementById('sweet_tea');
    btn.style.left = (Math.random() * (window.innerWidth - 180)) + 'px';
    btn.style.top = (Math.random() * 100) + 'px';
}
</script>
"""
components.html(html_tea, height=200)

st.write("---")

# 4. السؤال الرابع (الأنمي)
st.markdown("""### **السؤال الرابع (الأنمي):**""")
st.markdown("""#### **مين أقوى هجومياً وفي القتال: ميكاسا ولا ليفاي؟ ⚔️**""")

html_anime = """
<div style="position: relative; height: 180px; width: 100%; border: 1px solid #ddd; border-radius: 8px; background-color: #fff; padding: 10px;">
    <button id="mikasa_btn" onmouseover="moveMikasa()" ontouchstart="moveMikasa()" onclick="moveMikasa()" style="position: absolute; left: 25%; top: 50px; background-color: #e83e8c; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 20px; cursor: pointer;">ميكاسا 🧣</button>
    <button onclick="alert('تم تسجيل إجابتك: ليفاي الهيكل أقوى طبعاً ⚔️')" style="position: absolute; left: 60%; top: 50px; background-color: #111; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 20px; cursor: pointer;">ليفاي أكرمان ☕</button>
</div>
<script>
function moveMikasa() {
    var btn = document.getElementById('mikasa_btn');
    btn.style.left = (Math.random() * (window.innerWidth - 150)) + 'px';
    btn.style.top = (Math.random() * 100) + 'px';
}
</script>
"""
components.html(html_anime, height=200)

st.write("---")

# 5. السؤال الخامس والأخير (أسطورة الأكل)
st.markdown("""### **السؤال الخامس والأخير (حسم اللقب):**""")
st.markdown("""#### **مين هو الأسطورة الحقيقي واللي ذوقه دايماً أحسن في الأكل؟**""")

html_food = """
<div style="position: relative; height: 260px; width: 100%; border: 2px solid #d9534f; border-radius: 12px; background-color: #fffdf9; padding: 20px;">
    <button id="mohamed_btn" onclick="showResult()" style="position: absolute; left: 15%; top: 60px; background-color: #337ab7; color: white; border: none; padding: 15px 40px; font-size: 18px; font-weight: bold; border-radius: 30px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.15);">محمد 😎</button>
    <button id="raghad_btn" onmouseover="transformButton()" ontouchstart="transformButton()" onclick="transformButton()" style="position: absolute; left: 55%; top: 60px; background-color: #f05454; color: white; border: none; padding: 15px 40px; font-size: 18px; font-weight: bold; border-radius: 30px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.15); transition: all 0.1s ease-in-out;">رغد 🌸</button>
    <div id="final_result" style="text-align: center; padding-top: 150px; font-size: 19px; font-weight: bold; color: #d9534f; display: none; line-height: 1.6;">
        🎉 ذكاء خارق واعتراف تاريخي لا مفر منه! 🎉<br>
        تم تسجيل الإجابات وتوثيقها بالكامل: محمد هو أسطورة الأكل الرسمي والوحيد في الشلة، بذوقه العالي وبإقرار صريح من رغد وباقي المقاطعة! 🍔 تفضلوا بقبول فائق الاحترام لذوق القيادة! 🚀
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
components.html(html_food, height=300)

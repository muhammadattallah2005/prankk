import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="تصويت مهم جداً", page_icon="👑", layout="centered")

# عنوان الموقع
st.markdown("<h1 style='text-align: center; color: #1e3d59;'>👑 استفتاء حسم القيادة 👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>مين هو الـ Team Leader الحقيقي والفعلي لمشروع التخرج؟</h3>", unsafe_allow_html=True)

# الكود السحري لهروب زرار أماني واختيار محمد
html_code = """
<div style="position: relative; height: 350px; width: 100%; border: 1px dashed #ccc; border-radius: 10px; background-color: #f5f5f5;">
    
    <button id="mohamed_btn" onclick="showLeader()" style="
        position: absolute; 
        left: 25%; 
        top: 120px; 
        background-color: #007bff; 
        color: white; 
        border: none;
        padding: 15px 40px; 
        font-size: 20px; 
        font-weight: bold;
        border-radius: 8px; 
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;">
        محمد 😎
    </button>

    <button id="amani_btn" onmouseover="escapeButton()" onclick="escapeButton()" style="
        position: absolute; 
        left: 55%; 
        top: 120px; 
        background-color: #e83e8c; 
        color: white; 
        border: none;
        padding: 15px 40px; 
        font-size: 20px; 
        font-weight: bold;
        border-radius: 8px; 
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.1s ease;">
        أماني 👑
    </button>
    
    <div id="result_message" style="
        text-align: center; 
        padding-top: 220px; 
        font-size: 22px; 
        font-weight: bold; 
        color: #28a745; 
        display: none;
        line-height: 1.6;">
        🎉 عاش.. الاعتراف بالحق فضيلة! 🎉<br>
        تم اعتماد النتيجة: محمد هو القائد التاريخي والشرعي للمشروع بامتياز وبموافقة جميع الأطراف! 🥳🚀
    </div>
</div>

<script>
// دالة تخلي زرار أماني يطير بشكل عشوائي ومجنون في الشاشة
function escapeButton() {
    var btn = document.getElementById('amani_btn');
    
    // حساب أبعاد عشوائية تناسب مساحة البوكس الرمادي
    var x = Math.random() * (window.innerWidth - 180);
    var y = Math.random() * (180); // محددين الارتفاع عشان يفضل جوة النطاق
    
    // نقل الزرار للإحداثيات الجديدة فورا
    btn.style.left = x + 'px';
    btn.style.top = y + 'px';
}

// دالة إعلان الفوز لما يضغطوا على محمد
function showLeader() {
    document.getElementById('result_message').style.display = 'block';
    document.getElementById('amani_btn').style.display = 'none';   // اختفاء زرار أماني تماماً
    document.getElementById('mohamed_btn').style.display = 'none';  // اختفاء زرار محمد
}
</script>
"""

# تشغيل الكود في الـ Streamlit
components.html(html_code, height=400)

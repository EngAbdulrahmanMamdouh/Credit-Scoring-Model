import streamlit as st
import pandas as pd
import numpy as np
import joblib

# تحميل الموديل والميزات
@st.cache_resource
def load_model():
    model = joblib.load('credit_scoring_model.pkl')
    features = joblib.load('model_features.pkl')
    return model, features

model, model_features = load_model()

# إعدادات واجهة التطبيق
st.set_page_config(page_title="Credit Scoring System", page_icon="💳", layout="centered")
st.title("💳 Credit Scoring & Delinquency Predictor")
st.write("أدخل بيانات العميل لتقييم مدى خطورة تعثره ماليًا خلال سنتين.")
st.divider()

# استمارة إدخال البيانات
with st.form("customer_form"):
    st.subheader("👤 بيانات العميل الأساسية")
    age = st.number_input("العمر (Age)", min_value=18, max_value=100, value=35)
    NumberOfDependents = st.number_input("عدد أفراد الأسرة المعالين (Dependents)", min_value=0, max_value=20, value=1)
    MonthlyIncome = st.number_input("الدخل الشهري بالدولار ($ Monthly Income)", min_value=0.0, value=5000.0, step=500.0)
    DebtRatio = st.number_input("نسبة الدين (إجمالي الديون / الدخل)", min_value=0.0, value=0.35, step=0.05)
    
    st.subheader("📊 التاريخ الائتماني وسجل السداد")
    RevolvingUtilizationOfUnsecuredLines = st.number_input("نسبة استهلاك الحد الائتماني (Utilization)", min_value=0.0, value=0.3, step=0.1)
    Num30_59 = st.number_input("عدد مرات التأخر من 30 لـ 59 يومًا (آخر سنتين)", min_value=0, max_value=20, value=0)
    Num60_89 = st.number_input("عدد مرات التأخر من 60 لـ 89 يومًا (آخر سنتين)", min_value=0, max_value=20, value=0)
    Num90Late = st.number_input("عدد مرات التأخر لأكثر من 90 يومًا", min_value=0, max_value=20, value=0)
    
    st.subheader("🏠 القروض الحالية")
    NumberRealEstateLoansOrLines = st.number_input("عدد قروض التمويل العقاري", min_value=0, max_value=10, value=0)
    NumberOfOpenCreditLinesAndLoans = st.number_input("عدد خطوط الائتمان والقروض المفتوحة الأخرى", min_value=0, max_value=50, value=5)
    
    submit_button = st.form_submit_button(label="🔍 تحليل مخاطر الائتمان")

# معالجة البيانات عند الضغط على الزر
if submit_button:
    # حساب الميزات الجديدة تلقائياً (Feature Engineering)
    MonthlyDebt = DebtRatio * MonthlyIncome
    HasPastDue = 1 if (Num30_59 + Num60_89 + Num90Late > 0) else 0
    IncomePerDependent = MonthlyIncome / (NumberOfDependents + 1)
    TotalPastDueCount = Num30_59 + Num60_89 + Num90Late
    
    input_data = {
        'RevolvingUtilizationOfUnsecuredLines': RevolvingUtilizationOfUnsecuredLines,
        'age': age,
        'NumberOfTime30-59DaysPastDueNotWorse': Num30_59,
        'DebtRatio': DebtRatio,
        'MonthlyIncome': MonthlyIncome,
        'NumberOfOpenCreditLinesAndLoans': NumberOfOpenCreditLinesAndLoans,
        'NumberOfTimes90DaysLate': Num90Late,
        'NumberRealEstateLoansOrLines': NumberRealEstateLoansOrLines,
        'NumberOfTime60-89DaysPastDueNotWorse': Num60_89,
        'NumberOfDependents': NumberOfDependents,
        'MonthlyDebt': MonthlyDebt,
        'HasPastDue': HasPastDue,
        'IncomePerDependent': IncomePerDependent,
        'TotalPastDueCount': TotalPastDueCount
    }
    
    # تحويل الداتا وترتيبها لتطابق الموديل
    input_df = pd.DataFrame([input_data])[model_features]
    
    # التنبؤ
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    st.divider()
    st.subheader("🎯 نتيجة التقييم:")
    
    if prediction == 1:
        st.error(f"⚠️ **عميل عالي الخطورة (High Risk):** الموديل يتوقع تعثر العميل ماليًا. (نسبة الخطورة: {probability:.2%})")
    else:
        st.success(f"✅ **عميل آمن (Low Risk):** العميل ملتزم بالسداد وضمن الحدود الآمنة. (نسبة الخطورة: {probability:.2%})")
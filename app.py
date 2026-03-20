import streamlit as st

st.set_page_config(page_title="简单计算器", page_icon="🧮")

st.title("🧮 简单计算器")
st.write("这是一个用 Streamlit 做的入门小案例。")

# 输入框
num1 = st.number_input("请输入第一个数字", value=0.0)
num2 = st.number_input("请输入第二个数字", value=0.0)

# 运算类型
operation = st.selectbox(
    "请选择运算类型",
    ["加法", "减法", "乘法", "除法"]
)

# 按钮
if st.button("开始计算"):
    if operation == "加法":
        result = num1 + num2
        st.success(f"计算结果：{num1} + {num2} = {result}")

    elif operation == "减法":
        result = num1 - num2
        st.success(f"计算结果：{num1} - {num2} = {result}")

    elif operation == "乘法":
        result = num1 * num2
        st.success(f"计算结果：{num1} × {num2} = {result}")

    elif operation == "除法":
        if num2 == 0:
            st.error("除数不能为 0，请重新输入。")
        else:
            result = num1 / num2
            st.success(f"计算结果：{num1} ÷ {num2} = {result}")
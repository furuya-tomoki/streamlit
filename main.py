import streamlit as st
# streamlitを読み込む
import numpy as np
# numpyを読み込む
import pandas as pd
# pandasを読み込む
from PIL import Image
# 画像を読み込む
import time
st.title("Streamlit")
# サイトのタイトル表示
st.write("DataFrame")
# サイトに表記する内容

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)


# if st.checkbox("show Image"):
# チェックボックスの作成
#     img = Image.open("S__1941509.jpg")
#     st.image(img, caption="cat", use_column_width=True)

# option = st.selectbox(
# セレクトボックスの作成
#     "好きな数字を教えてください",
#     list(range(1, 11))
# )
# "好きな数字は、", option, "です"

# text = st.sidebar.text_input("趣味はなんですか？")
# テキスト入力の作成
# condition = st.sidebar.slider("今の調子は？", 0, 100, 50)
# (最小値、最大値、デフォルト値の順で選択)
# "趣味は", text
# "コンディション", condition
# sidebar = 横画面に設置

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
expander1.write("回答")
expander2 = st.expander("問い合わせ")
expander2.write("回答")
expander3 = st.expander("問い合わせ")
expander3.write("回答")


# df = pd.DataFrame({
#     "1列目": [1, 2, 3, 4],
#     "2列目": [10, 20, 30, 40]
# })
# st.write(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )
# 新宿の緯度、経度にランダム数値を表示

# st.map(df)
# mapを表示
# st.line_chart(df)
# 折れ線グラフの表示
# st.area_chart(df)
# エリアチャートの表示
# st.bar_chart(df)
# グラフの表示

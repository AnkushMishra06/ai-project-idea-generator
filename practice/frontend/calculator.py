import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

if 'display' not in st.session_state:
    st.session_state.display = ""
if 'history' not in st.session_state:
    st.session_state.history = []
if 'result' not in st.session_state:
    st.session_state.result = False
if 'show_hist' not in st.session_state:
    st.session_state.show_hist = False

def press(val):
    if st.session_state.result:
        st.session_state.display = ""
        st.session_state.result = False
    st.session_state.display += val
    st.rerun()

def clear():
    st.session_state.display = ""
    st.session_state.result = False
    st.rerun()

def backspace():
    st.session_state.display = st.session_state.display[:-1]
    st.rerun()

def evaluate():
    expression = st.session_state.display
    if not expression:
        return
    try:
        answer = eval(expression)
        answer = int(answer) if int(answer)==float(answer) else round(float(answer),10)
        record = f"{expression} = {answer}"
        st.session_state.history = ([record] + st.session_state.history)[:5]
        st.session_state.display = str(answer)
        st.session_state.result = True
    except ZeroDivisionError:
        st.session_state.display = "Error Division by 0"
        st.session_state.result = True
    except Exception:
        st.session_state.display = "Error Occurred"
        st.session_state.result = True

    st.rerun()


display_scr = st.session_state.display or "0"
st.markdown(display_scr, unsafe_allow_html=True)


r1 = st.columns(4)
with r1[0]:
    with st.container():
        if st.button("C",  key="c"):  clear()
with r1[1]:
    if st.button("del",  key="bs"): backspace()
with r1[2]:
    if st.button("%",  key="pct"): press("%")
with r1[3]:
    if st.button("÷",  key="div"): press("/")

r2 = st.columns(4)
with r2[0]:
    if st.button("7", key="7"):
        press("7")
with r2[1]:
    if st.button("8", key="8"):
        press("8")
with r2[2]:
    if st.button("9", key="9"):
        press("9")
with r2[3]:
    if st.button("X", key="mul"):
        press("*")

r3 = st.columns(4)
with r3[0]:
    if st.button("4", key="4"):
        press("4")
with r3[1]:
    if st.button("5", key="5"):
        press("5")
with r3[2]:
    if st.button("6", key="6"):
        press("6")
with r3[3]:
    if st.button("_", key="sub"):
        press("-")

r4 = st.columns(4)
with r4[0]:
    if st.button("1", key="1"):
        press("1")
with r4[1]:
    if st.button("2", key="2"):
        press("2")
with r4[2]:
    if st.button("3", key="3"):
        press("3")
with r4[3]:
    if st.button("Add", key="add"):
        press("+")

r5 = st.columns([2,1,1])
with r5[0]:
    if st.button("0", key="0", use_container_width=True):
        press("0")
with r5[1]:
    if st.button(".", key="."):
        press(".")
with r5[2]:
    if st.button("=", key="eq"):
        evaluate()

history_label = "Hide History" if st.session_state.show_hist else "Show History"
if st.button(history_label, key="hist", use_container_width=True):
    st.session_state.show_hist = not st.session_state.show_hist
    st.rerun()

if st.session_state.show_hist:
    if st.session_state.history:
        rows = "<br>".join(
            f"<span style='color:#6c7086'>{i+1}.</span>  {h}"
            for i, h in enumerate(st.session_state.history)
        )
        st.markdown(f'<div class="hist-panel"><h4>Last Calculations</h4>{rows}</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="hist-panel"><h4>Last Calculations</h4><em>No history yet.</em></div>',
                    unsafe_allow_html=True)
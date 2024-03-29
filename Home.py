import streamlit as st

st.title('A title _italics_ :blue[colors] emojis :sunglasses:')
st.divider()

st.header('This is a header')
st.caption('Caption: is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')
st.divider()

st.markdown('### you can use Markdown directly, or write, or text')
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
st.write('This is write')
st.text('This is text')
st.divider()


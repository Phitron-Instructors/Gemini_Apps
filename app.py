import streamlit as st 
from summary_quiz_generator import note_summarizer,quiz_generator,generate_audio_summary
from PIL import Image



st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quiz")

st.divider()


with st.sidebar:
    st.header("Controls")

    uploaded= st.file_uploader(
        "Upload the photos of your notes",
        type =['jpeg','jpg','png'],
        accept_multiple_files =True

    )

    option_selected = st.selectbox(
        "Enter the difficulty of Quiz",
        ("Easy","Medium","Hard"),
        index = None
    )

    clicked = st.button("Click the button to initiate AI",type="primary")

if clicked:
    if uploaded is not None and option_selected:
        if len(uploaded)>5:
            st.warning("Upload at max 5 images")
        else:
            with st.spinner("AI is writing note for you...."):
                img = [Image.open(image) for image in uploaded]
                st.subheader("Uploaded photos")
                cols = st.columns(len(img))
                for i , file in enumerate(img):
                    with cols[i]:
                        st.image(file,width=100)
                with st.container(border=True):
                    notes = note_summarizer(img)
                    st.markdown(notes)
                    notes =notes.replace("*", "")
                    st.audio(generate_audio_summary(notes))
                st.divider()


                with st.container(border=True):
                    st.subheader(f"❓ Quiz ({option_selected} Level)")
                    st.markdown(quiz_generator(img, option_selected))



       


       

            

        


       
    if uploaded is None: 
        st.warning("Upload atleast 1 image")
    if option_selected is None: 
        st.warning("Select a difficulty")

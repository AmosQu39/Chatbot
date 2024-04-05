import openai
import streamlit as st
from streamlit_chat import message
from streamlit_modal import Modal
import time

# Setting page title and header
st.set_page_config(page_title="NaN", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Guess who I am 😬</h1>", unsafe_allow_html=True)

# Set org ID and API key
# openai.organization = "<YOUR_OPENAI_ORG_ID>"
openai.api_key = "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"
content1="Opps! Your voice is finally indistinguishable in the digital world!"
Counts=0
Limits=10

# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are an actor performing in Faust."}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0

# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
st.sidebar.title("Sidebar")
model_name = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-3.5-turbo"
else:
    model = "gpt-4"

# reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are an actor performing in Faust."}
    ]
    st.session_state['number_tokens'] = []
    st.session_state['model_name'] = []
    st.session_state['cost'] = []
    st.session_state['total_cost'] = 0.0
    st.session_state['total_tokens'] = []
    counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")





# generate a response
def generate_response(prompt,Counts):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = openai.chat.completions.create(
        model=model,
        messages=st.session_state['messages']
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": response})
    Counts+=1
    # print(st.session_state['messages'])
    total_tokens = completion.usage.total_tokens
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    return response, total_tokens, prompt_tokens, completion_tokens


# container for chat history
response_container = st.container()
# container for text box
container = st.container()

# define a new modal
my_modal=Modal(title="",key="modal_key",max_width=200)


def input_select(Counts):
    if Counts==0:
        inp="Let's start the conversation!"
    else:
        inp="Your voice is not yet diminished from the digital space, let's move on!"
    return inp


with container:
    with st.form(key='my_form', clear_on_submit=True):
        submit_button = st.form_submit_button(label='Send')
        user_input = st.text_area(input_select(Counts), key='input1', height=100)






    if submit_button and user_input:
        output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input,Counts)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        st.session_state['model_name'].append(model_name)
        st.session_state['total_tokens'].append(total_tokens)


        # from https://openai.com/pricing#language-models
        if model_name == "GPT-3.5":
            cost = total_tokens * 0.002 / 1000
        else:
            cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

        st.session_state['cost'].append(cost)
        st.session_state['total_cost'] += cost

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            Counts+=1
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

            st.write(
                f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}; This conversation has been going for {Counts} times. It may continue for another {Limits-Counts} times")
            counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f},")
        if Counts > Limits:
            st.session_state['generated'] = []
            st.session_state['past'] = []
            st.session_state['messages'] = [
                {"role": "system", "content": "You are an actor performing in Faust."}
            ]


            time.sleep(5)
            #st.markdown(f'<p style="color:{'#f93b12'};font-size:24px;border-radius:2%;">{content1}</p>', unsafe_allow_html=True)
            #st.markdown(f'<p style="color:{'#f93b12'};font-size:24px;">{content1}</p>')
            #st.markdown(f':red[Opps! Your voice is becoming indistinguishable in the digital world!]')
            st.warning(f':red[Opps! Your voice is becoming indistinguishable in the digital world!]')
            #st.markdown(f'<p style="font-family:Courier; color:Red; font-size: 28px;">{"Opps! Your voice is becoming indistinguishable in the digital world!"}</p>')
            Limits = 3
            Counts=0
            time.sleep(5)
            st.rerun()
            # st.stop()
            # clear_btn_click=st.button("See you next time!",key="confirm")



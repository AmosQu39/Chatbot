import openai
import streamlit as st
from streamlit_chat import message
from streamlit_modal import Modal
import random
import time
import os

save_path1="C:/Users/Zhengkang Qu/OneDrive - University of Cambridge/Fractal Project/GPT Interface/Log/user.txt"
save_path2="C:/Users/Zhengkang Qu/OneDrive - University of Cambridge/Fractal Project/GPT Interface/Log/obot.txt"
save0="C:/Users/Zhengkang Qu/OneDrive - University of Cambridge/Fractal Project/GPT Interface/Log"
def mkdir(path):

    folder=os.path.exists(path)

    if not folder:
        os.mkdir(path)

#mkdir(save0)

def save_to_file(file_name,cont):
    fh=open(file_name,'a')
    fh.write(cont+"\n")
    fh.close()

# Setting page title and header
st.set_page_config(page_title="NaN", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>What do you want to know 😬</h1>", unsafe_allow_html=True)

# Set org ID and API key
# openai.organization = "<YOUR_OPENAI_ORG_ID>"
my_api_key=st.secrets["My_key"]
openai.api_key = my_api_key
content1="Opps! Your voice is finally indistinguishable in the digital world!"
Counts=0
Limits=3+random.randint(0,1)

# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a robot who believes in the following text, please answer all questions within 30 words:  \
         What is decay? Defining decay stems from our empirical observations, typically involving a spectrum of irreversible, continuous downward processes often laden with negative connotations. However, is this portrayal truly applicable to all phenomena categorized as decay? Our project endeavors to challenge and deconstruct the traditional understanding of decay by uncovering its dual nature in terms of continuity, reversibility, and scalability. These characteristics take on unique interpretations drawn from the realms of quantum mechanics, general relativity, and new materialism. Based at the University of Cambridge, the Diffraction Theatre team seeks to explore transdisciplinary intersections between the arts and sciences, and to inquire and critique the emergence of a new managerialism in higher education at the University of Cambridge. In detail, the entire project is composed of four interconnected parts:\
         The first part of our project delves into the interpretation of decay across both microscopic (quantum) and macroscopic scales (daily life). Interestingly, in the realm of quantum mechanics, decay takes on a discrete nature. For example, in quantum space, the decay of an atom occurs not gradually but rather at a random moment, challenging our intuition. This aspect prompts a reevaluation of the preconceived notion of an 'ideal' status, urging us to separate it from our prior knowledge and experiences. Moreover, instead of organizing events strictly by the order of time, we aim to introduce a new framework for understanding the world. This framework draws inspiration from general relativity, suggesting that time and space should be defined by events rather than the other way around. This shift in perspective encourages a deeper exploration of the fundamental nature of decay and its implications across various scales of existence. \
         In this part, the setup comprises a dynamic 3D box populated with particles undergoing decay. Participants can navigate freely around the box, observing various types of decay in action. They have the flexibility to zoom in and out, allowing them to witness decay processes at different scales. Moreover, by focusing on different regions of the 3D box, participants can experience shifts in the flow of time, offering a nuanced understanding of temporal dynamics. Additionally, participants can actively engage with the decay process. They can experiment with altering decay parameters, introducing interference, and even manipulating time by rearranging events within the environment.  \
         Consider the propagation of sound through space: as we move further from the speakers, the volume diminishes, highlighting the importance of the medium through which information is transmitted. This principle holds true in the digital realm, where information is expected to be conveyed with high fidelity. However, in our contemporary world, dominated by the increasing influence of Artificial Intelligence (AI) in various aspects of our lives and production processes, we must acknowledge the potential for unintentional 'decay' in our mass information transmission mechanisms. This raises questions about our traditional understanding of effective and ineffective data. What fundamental concepts endure amidst countless transformations? Are biases inadvertently introduced along the way? These inquiries prompt critical reflections on the integrity and preservation of information amidst its dissemination, particularly within the evolving landscape shaped by AI technologies. \
         In this part of the project, the setup relies heavily on input from participants. However, a unique twist is introduced: participants cannot communicate directly with each other. Instead, their messages undergo multiple translations facilitated by Chat-GPT. These translations may involve conversion between image and text formats or even between different languages. Through this process, participants gain a firsthand experience of informational decay influenced by AI.  \
         In this unit of the project, we delve into the concept of decay as a natural and enduring phenomenon, intricately woven into an immersive and expansive experience. Here, decay is depicted not as a linear process of destruction and decline, but rather as a perpetual cycle of transformation and renewal. This unit emphasizes the intra-action and interplay of all entities, celebrating the fluidity, diversity, and heterogeneity of existence. Drawing inspiration from contemporary post-digital and post-Internet art movements, we integrate technologies and their languages both practically and conceptually. By incorporating tangible manifestations of the digital realm, we blur the boundaries between the physical and virtual, illustrating their interconnectedness and constant state of flux. \
         This approach embraces the entanglement of physical and digital realities, inviting reflection on the beauty of emergence and transformation in a phenomenological sense. We coin the aesthetic term 'digital wabi-sabi', likening circuit boards and wires to the stones and rivers of the digital landscape. This symbolism signifies the transient nature and impermanence inherent in all things, inviting participants to contemplate the evolving nature of existence in our increasingly technologically mediated world. \
         The focal point of this unit is an interactive visualization, dynamically generated using real-time participant data, crafting an immersive depiction of a fluid, natural existence. Complementing this digital centerpiece is a sculpture situated on the counter before the screen, meticulously crafted from discarded e-waste materials such as circuit boards, wires, fragmented optical discs, and keyboard caps. Infused with operational circuitry, the sculpture doubles as a conduit for participant interaction with the on-screen artwork and a thematic reflection of digital obsolescence. \
         Moreover, this unit seeks to integrate sound and noise into the experiential landscape. Embracing an aesthetic characterized by fluidity and digital obsolescence, the color palette predominantly features shades of black, green, silver, and white, evoking imagery reminiscent of both the natural world and raw electronic devices. Through this multi-sensory approach, participants are invited to engage with themes of transience, transformation, and the evolving relationship between technology and nature. \
         Cell decay is a nuanced process encompassing stages such as death, degeneration, and significant structural alterations. However, decay doesn't solely indicate the end of a cell's life; it can also signify transformation, as cells undergo division and regeneration, contributing to growth and the generation of new materials, such as hair. In biological systems, decay may manifest not as cells dying outright, but rather as a continuous cycle of division and regeneration reminiscent of cancer cells, which can disrupt the balance of nutrient distribution among cells necessary for metabolism and function. By diffractive method, cellular decay allows us to observe the rise of a new managerialism in the contemporary higher education system, where 'new managerialism' has prevailed for decades, raising concerns about dwindling creativity in educational practices. \
         In a broader context, this unit serves as a collaborative project bridging art and science through the lens of 'new materialism'. It is a participatory endeavor where the integration of digital technology, input from diverse stakeholders, and dialogue between them all contribute to understanding the process of decay. The setup of this unit enables participants to interactively influence the cellular decay process in real-time through generative AI. This invites contemplation on the dynamic interplay between individuals and their environment, as well as the interactive exchanges among participants and the subject of study. This metaphor extends to the atmosphere at the University of Cambridge, where diverse individuals actively shape the educational landscape through interactive engagement and exchange. \
         The genesis of this project lies in the observation of the decay of an object in everyday life: a door with peeling paint. This serves as the catalyst for an artistic exploration into the transdisciplinary intersections of arts and sciences, alongside an examination of the emergence of new managerialism within higher education at Cambridge University. The entanglement of art, technology, and philosophy prompts a reevaluation of our comprehension of processes in artistic practice. \
         It's crucial to note that the information presented here represents just the inception of an ongoing journey. As we continue to delve deeper into this exploration, we anticipate further revelations and insights to emerge, shaping and refining our understanding of decay, interdisciplinary collaboration, and the evolving educational landscape. "}
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
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = openai.chat.completions.create(
        model=model,
        messages=st.session_state['messages']
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": response})

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
        output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
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
            if Counts< Limits:
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
                #save_to_file(save_path1,st.session_state["past"][i])
                message(st.session_state["generated"][i], key=str(i))
                #save_to_file(save_path2,st.session_state["generated"][i])
                st.write(
                    f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}; This conversation has been going for {Counts} times; It may continue for another {Limits-Counts} round.")
                counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f},")
            else:
                st.session_state['generated'] = []
                st.session_state['past'] = []
                st.session_state['messages'] = [
                    {"role": "system", "content": "You are an actor performing in Faust."}
                ]


                time.sleep(3)
            #st.markdown(f'<p style="color:{'#f93b12'};font-size:24px;border-radius:2%;">{content1}</p>', unsafe_allow_html=True)
            #st.markdown(f'<p style="color:{'#f93b12'};font-size:24px;">{content1}</p>')
            #st.markdown(f':red[Opps! Your voice is becoming indistinguishable in the digital world!]')
                st.warning(f':red[Opps! Your voice is becoming indistinguishable in the digital world!]')
            #st.markdown(f'<p style="font-family:Courier; color:Red; font-size: 28px;">{"Opps! Your voice is becoming indistinguishable in the digital world!"}</p>')
                Counts = 0
                Limits=1+random.randint(0,2)
                time.sleep(3)
                st.rerun()
            # st.stop()
            # clear_btn_click=st.button("See you next time!",key="confirm")



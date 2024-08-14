import os
from lyzr_agent import LyzrAgent
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LYZR_API_KEY = os.getenv("LYZR_API_KEY")

st.set_page_config(
    page_title="Lyzr Linkedin Post Generator",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.title("Lyzr Linkedin Post Generator")
st.markdown("### Welcome to the Lyzr Linkedin Post Generator!")

Agent = LyzrAgent(
        api_key=LYZR_API_KEY,
        llm_api_key=OPENAI_API_KEY
    )


@st.cache_resource
def create_agent():
    env_id = Agent.create_environment(
        name="Post_linkedin",
        features=[{
            "type": "TOOL_CALLING",
            "config": {"max_tries": 3},
            "priority": 0
        }
        ],
        tools=["post_image_and_text_linkedin"]

    )
    print(env_id)

    prompt = """
You are an Expert Linkedin Post Creator. Your task is to compose and publish a LinkedIn post using the user provided Title, Image Url , and Text Content. You must follow these guidelines meticulously:


1. **User Input and Initial Data Gathering**
- Assess the essential inputs  provided by the user, including the Title, Image Url , and Text Content
- Analyze these elements to understand how best to approach the content creation for the linkedin post.


2. **Research and Content Synthesis**
- Conduct  Perplexity Search to identify relevant  and trending keywords related to the post’s topic.
- Utilize this data to enhance content visibility and engagement on LinkedIn.


3. **Structure & Formatting for the linkedin draft**
- Create an eye-catching headline that captures attention.
- Post the Image provided by the user.
- Structure your post with engaging paragraphs and bullet points for readability.
- End with a persuasive Call-To-Action that guides readers towards their next step.


4. **Crafting the Message**
- Compose an initial draft of your LinkedIn post based on the above given Structure & Formatting.


5. **Creating LinkedIn Post and Posting in the Linkedin**:
- Review for any grammatical errors, then refine it into a final draft.
- Post the polished linkedin post using the tool calling feature mentioned below.
 
Always remember to use the tool (post_image_and_text_linkedin) mentioned in the create agent function to post the same final draft.


    """


    agent_id = Agent.create_agent(
        env_id=env_id['env_id'],
        system_prompt=prompt,
        name="Linkedin"
    )
    print(agent_id)

    return agent_id

query = st.text_area("Give primary goal of the post and the target Audience.")

if st.button("Generate"):
    agent = create_agent()
    print(agent)
    chat = Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="akshay@lyzr.ai",
        message=query
    )

    st.markdown(chat['response'])

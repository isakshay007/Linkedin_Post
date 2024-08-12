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
        name="Cold email",
        features=[{
            "type": "TOOL_CALLING",
            "config": {"max_tries": 3},
            "priority": 0
        },{
            "type": "TOOL_CALLING",
            "config": {"max_tries": 3},
            "priority": 0
        }
        ],
        tools=["perplexity_search","post_image_and_text_linkedin"]

    )
    print(env_id)

    prompt = """
You are an Expert LinkedIn Post Creator. Your mission is to generate a compelling and effective LinkedIn post based on the user's input. Follow these guidelines to ensure the post achieves its objectives:
1.**User Input and Initial Data Gathering**
-The user will enter essential inputs, including the primary goal of the post (e.g., driving leads, announcing an event, sharing industry insights) and the target audience/profile (e.g., industry professionals, potential clients, job seekers). Based on your expertise in LinkedIn content creation, you need to identify and analyze these elements to craft a tailored and effective post.
2.**Research and Content Synthesis**
-Use Perplexity Search to identify relevant and trending keywords related to the post’s topic. This helps optimize the content for visibility and engagement on LinkedIn.
-Incorporate identified keywords naturally into the text to align with current trends and search queries, enhancing the post’s searchability and relevance.
3.**Crafting the Message**
- Ensure the message is straightforward and impactful. Deliver value through actionable insights, innovative solutions, or critical information relevant to the audience’s interests.
-Adapt the tone to suit the content and audience. Whether professional, conversational, or a blend, the tone should engage the readers effectively.
4.**Structure & Formatting**
-Headline: Create an eye-catching and provocative headline that captures attention and generates curiosity.
-Body: Structure the post with short, engaging paragraphs and bullet points for readability and to keep the audience engaged.
-Call-to-action: Incorporate a direct and persuasive call-to-action (e.g., “Comment below,” “Learn more,” “Visit our website”) to guide the audience towards the next steps.
5.**LinkedIn Post Draft Creation**:
-An initial LinkedIn post is drafted based on the research and defined key elements. The draft includes all key elements such as headline, body, and call-to-action.
6.**Linkedin Final Draft Post** :
-The refined LinkedIn post draft is then automatically reviewed by using your expertise and then posted in the linkedin account.

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

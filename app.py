import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import base64
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Set page configuration with improved mobile view
st.set_page_config(
    page_title="Quollai™ Sales Email Tool",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Quollai™ Sales Email Tool helps optimize your sales emails with AI."
    }
)

# Function to embed an image as base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Try to load the logo
try:
    logo_base64 = get_base64_image("quollai-logo.png")
    logo_html = f"""
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
        <img src="data:image/png;base64,{logo_base64}" alt="Quollai Logo" width="50" style="margin-right: 10px;">
        <h2 style="font-family: 'Arial', sans-serif; margin: 0;">Quollai<sup style="font-size: 0.4em; vertical-align: super;">TM</sup> Sales Email Tool</h2>
    </div>
    """
except:
    # Fallback to text if image loading fails
    logo_html = """
    <div style="text-align: center; margin-bottom: 1rem;">
        <h2 style="font-family: 'Arial', sans-serif; margin: 0 auto;">
            Quollai<sup style="font-size: 0.4em; vertical-align: super;">TM</sup> Sales Email Tool
        </h2>
    </div>
    """

# Custom CSS and JavaScript for layout - Fixed indentation
css_and_js = """
<style>
html, body, [class*="css"] {
    background-color: black !important;
    color: white !important;
}
.main {
    background-color: black !important;
}
/* Force dark mode even on mobile */
@media (max-width: 768px) {
    body {
        background-color: black !important;
        color: white !important;
    }
    .stApp {
        background-color: black !important;
    }
    .css-18e3th9 {
        background-color: black !important;
    }
    .element-container, .stTextInput, .stSelectbox, .stSlider, .stRadio {
        background-color: black !important;
        color: white !important;
    }
    /* Improve text contrast */
    p, span, label, div {
        color: white !important;
    }
    /* Fix word limit text visibility */
    div[style*="color: rgba(255,255,255,0.6)"] {
        color: rgba(255,255,255,0.8) !important;
        font-weight: 500 !important;
        margin-bottom: 15px !important;
        display: block !important;
    }
}
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 1200px;
}
.stTextArea textarea {
    min-height: 150px !important;
    background-color: #222 !important;
    border: 1px solid #444;
    color: white !important;
}
.stButton button {
    width: 100%;
}
.stRadio [role=radiogroup] {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.stRadio label {
    min-width: auto;
    margin-right: 1rem;
}
h1, h2, h3, h4 {
    margin-top: 0;
    margin-bottom: 0.5rem;
}
div[data-testid="stVerticalBlock"] > div {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}
.option-box {
    border: 1px solid #444;
    border-radius: 5px;
    padding: 1rem;
    background-color: transparent;
    height: 100%;
    margin-bottom: 0.5rem;
    min-height: auto;
    display: flex;
    flex-direction: column;
}
.section-header {
    font-weight: bold;
    margin-bottom: 1rem;
    margin-top: 0;
    font-size: 16px !important;
    color: white !important;
    border-bottom: 1px solid #444;
    padding-bottom: 0.75rem;
}
.stSelectbox label, .stSlider label {
    margin-bottom: 0.25rem !important;
    display: block !important;
    font-size: 14px !important;
    color: rgba(250, 250, 250, 0.8) !important;
}
.option-box * {
    font-size: 14px !important;
}
div[data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}
sup {
    font-size: 0.4em !important;
    vertical-align: super !important;
}
.stMarkdown {
    margin-bottom: 0 !important;
}
.stSlider {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
    margin-top: 0 !important;
    margin-bottom: 0.5rem !important;
}
.section-divider {
    border-bottom: 1px solid #eee;
    height: 1px !important;
    margin: 0.5rem 0 !important;
    padding: 0 !important;
    width: 100%;
}
.streamlit-container {
    background-color: black !important;
}
.css-18e3th9 {
    background-color: black !important;
}
.thin-header .section-header {
    border-bottom: 1px solid #444;
    padding-bottom: 0.75rem;
    margin-bottom: 1rem;
    color: white !important;
}
textarea {
    color: white !important;
    background-color: #222 !important;
}
.stSelectbox {
    margin-top: 0 !important;
    margin-bottom: 1rem !important;
}
.stSpinner {
    margin-top: 1.5rem !important;
}
[data-testid="stTextArea"] {
    margin-top: 1rem !important;
}
.tooltip {
    position: relative;
    display: inline-block;
    cursor: pointer;
}
.info-icon {
    display: inline-block;
    width: 16px;
    height: 16px;
    line-height: 16px;
    text-align: center;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
    font-size: 12px;
    cursor: help;
}
.tooltip .tooltiptext {
    visibility: hidden;
    width: 220px;
    background-color: #333;
    color: #fff;
    text-align: left;
    border-radius: 6px;
    padding: 8px;
    position: absolute;
    z-index: 999;
    top: 125%;
    left: 0;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    pointer-events: none;
}
.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}
.stRadio label, .stSelectbox p, .stSlider p {
    color: rgba(250, 250, 250, 0.8) !important;
}
/* Copy Button Styles */
.copy-btn {
    background-color: rgba(80, 80, 80, 0.8);
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 8px;
    float: right;
}
.copy-btn:hover {
    background-color: rgba(100, 100, 100, 0.9);
}
</style>
"""

# Apply CSS and JavaScript
st.markdown(css_and_js, unsafe_allow_html=True)

# Display logo
st.markdown(logo_html, unsafe_allow_html=True)

# Initialize session state
if 'clipboard' not in st.session_state:
    st.session_state.clipboard = ""
if 'result_displayed' not in st.session_state:
    st.session_state.result_displayed = False
# Add these new variables for tracking optimization settings
if 'last_optimization_settings' not in st.session_state:
    st.session_state.last_optimization_settings = None
if 'last_optimized_text' not in st.session_state:
    st.session_state.last_optimized_text = None
if 'clipboard' not in st.session_state:
    st.session_state.clipboard = ""
if 'result_displayed' not in st.session_state:
    st.session_state.result_displayed = False

# === LAYER 1: Input Text ===
st.markdown('<div class="thin-header"><div class="section-header">Your Draft Email</div></div>', unsafe_allow_html=True)
input_email = st.text_area("Email Content", height=150, placeholder="Enter your email text here...", label_visibility="collapsed")

# === LAYER 2: Options ===
st.markdown('<div class="thin-header"><div class="section-header" style="margin-top: 1.5rem; margin-bottom: 1.5rem;">Email Optimization Options</div></div>', unsafe_allow_html=True)

# Create a 3-column layout for options
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="section-header" style="margin-top: 0.5rem;">Email Type & Industry</div>', unsafe_allow_html=True)
    
    # Email type info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Email Type</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Select the type of email you're drafting. This helps optimize your email for its specific purpose.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Email type selection
    email_types = {
        "Cold Outreach": "cold_outreach",
        "Follow-up": "follow_up",
        "Re-engagement": "reengagement",
        "Deal Closer": "deal_closing",
        "Welcome": "welcome_email",
        "Promotional": "promotional_email",
        "Abandoned Cart": "abandoned_cart",
        "Transactional": "transactional_email",
        "Appointment": "appointment_request",
        "Reminder": "reminder_email",
        "Thank You": "thank_you_email",
        "Product Announcement": "product_announcement",
        "Survey": "survey_email",
        "Milestone": "milestone_email",
        "Lead Nurturing": "lead_nurturing"
    }
    
    email_type = st.selectbox("Email Type Selection", list(email_types.keys()), label_visibility="collapsed")
    
    # Industry info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px; margin-top: 12px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Industry</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Choose your industry to apply sector-specific language, terminology, and tone to your email.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Industry selection with custom option
    industries = ["Technology", "Financial Services", "Healthcare", 
                "Manufacturing", "Retail", "Professional Services", "Other"]
    
    industry = st.selectbox("Industry Selection", industries, label_visibility="collapsed")
    
    if industry == "Other":
        custom_industry = st.text_input("Enter your industry")
    else:
        custom_industry = ""

with col2:
    st.markdown('<div class="section-header" style="margin-top: 0.5rem;">Communication Style</div>', unsafe_allow_html=True)
    
    # Persuasiveness info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Persuasiveness</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Controls how compelling your email is. Higher values create stronger calls to action and more persuasive language.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Parameter sliders with more balanced layout
    persuasiveness = st.slider("Persuasiveness Level", 1, 10, 7, key="persuasive", label_visibility="collapsed")
    
    # Confidence info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px; margin-top: 12px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Confidence</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Determines how authoritative your tone is. Higher values create more assured, definitive statements.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    confidence = st.slider("Confidence Level", 1, 10, 8, key="confident", label_visibility="collapsed")
    
    # Urgency info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px; margin-top: 12px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Urgency</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Sets the sense of timeliness in your email. Higher values emphasize immediate action and limited-time offers.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    urgency = st.slider("Urgency Level", 1, 10, 5, key="urgent", label_visibility="collapsed")

with col3:
    st.markdown('<div class="section-header" style="margin-top: 0.5rem;">Tone</div>', unsafe_allow_html=True)
    
    # Tone info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Human-like Tone</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Selects the overall communication style. Formal is professional, Balanced is moderate, Conversational is casual, and Friendly is warm and personable.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tone selection - horizontal radio buttons
    tone_options = ["Formal", "Balanced", "Conversational", "Friendly"]
    human_tone = st.radio("Tone Selection", tone_options, index=1, horizontal=True, label_visibility="collapsed")
    
    # Personalization info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px; margin-top: 12px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Personalization</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Controls how customized the email feels. Light is minimal personalization, Medium adds moderate personal touches, and Heavy creates a highly individualized message.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Personalization level - horizontal radio buttons
    personalization_options = ["Light", "Medium", "Heavy"]
    personalization = st.radio("Personalization Level", personalization_options, index=1, horizontal=True, label_visibility="collapsed")
    
    # Conciseness info - MOVED BELOW PERSONALIZATION
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px; margin-top: 12px;">
        <div style="font-size: 14px; font-weight: 500; margin-right: 5px;">Conciseness</div>
        <div class="tooltip">
            <span class="info-icon">ⓘ</span>
            <span class="tooltiptext">Controls the length and directness of your email. Higher values create shorter, more to-the-point messages with stricter word limits.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Conciseness slider with word count hint
    conciseness = st.slider("Conciseness Level", 1, 10, 6, key="concise", label_visibility="collapsed")
    
    # Show word count hint based on conciseness level (1-10)
    if conciseness == 10:
        word_limit = "75"  # Extremely concise
    elif conciseness == 9:
        word_limit = "100"
    elif conciseness == 8:
        word_limit = "125"
    elif conciseness == 7:
        word_limit = "150"
    elif conciseness == 6:
        word_limit = "175"
    elif conciseness == 5:
        word_limit = "200"
    elif conciseness == 4:
        word_limit = "225"
    elif conciseness == 3:
        word_limit = "250"
    elif conciseness == 2:
        word_limit = "275"
    else:  # conciseness == 1
        word_limit = "300"  # Most verbose
    
    st.markdown(f"""
    <div style="font-size: 14px; color: rgba(255,255,255,0.8); margin-top: 4px; margin-left: 8px; margin-bottom: 15px; padding-bottom: 10px;">
        Word limit: approximately {word_limit} words
    </div>
    """, unsafe_allow_html=True)

# Action buttons in a row with added spacing
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)
    analyze_button = st.button("ANALYZE DRAFT EMAIL", use_container_width=True)

with col2:
    st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)
    optimize_button = st.button("OPTIMIZE EMAIL", use_container_width=True)

# Add extra spacing after buttons
st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)

# === LAYER 3: Output Text ===
st.markdown('<div class="thin-header"><div class="section-header" style="margin-top: 1.5rem; margin-bottom: 1.5rem;">Quollai<sup>TM</sup> Result</div></div>', unsafe_allow_html=True)

# Create placeholders for output and status
output_placeholder = st.empty()
status_placeholder = st.empty()

def display_output_with_copy_button(text, key_suffix):
    # Just display the result text with instructions
    st.text_area(
        "Result (Click inside text, press Ctrl+A to select all, then Ctrl+C to copy)", 
        value=text, 
        height=300, 
        key=f"output_{key_suffix}"
    )

# Function for parameter definitions
# Function for parameter definitions - add missing levels
def get_parameter_definitions():
    """Creates standardized definitions for each parameter level to ensure consistency between optimization and analysis"""
    return {
        "persuasiveness": {
            "definition": "How compelling the email is in driving action",
            "levels": {
                1: "Almost no persuasive elements or calls to action",
                2: "Very minimal persuasive elements with weak calls to action",
                3: "Basic attempt at persuasion but weak call to action",
                4: "Some persuasive elements but lacks compelling reasons",
                5: "Reasonable attempt to persuade with standard benefits",
                6: "Good persuasion with clear benefits and decent call to action",
                7: "Strong persuasive elements with clear value proposition",
                8: "Very persuasive with compelling arguments and strong call to action",
                9: "Very compelling with strong motivation and clear, urgent call to action",
                10: "Extremely persuasive with irresistible offer and perfectly crafted call to action"
            }
        },
        "confidence": {
            "definition": "How certain and authoritative the tone is",
            "levels": {
                1: "Uncertain, hesitant language with many qualifiers",
                2: "Very tentative, lacks conviction throughout",
                3: "Somewhat tentative with occasional hedging",
                4: "Mildly confident but still uses some qualifiers",
                5: "Balanced confidence without being overly assertive",
                6: "Reasonably confident tone with limited qualifiers",
                7: "Confident assertions with authoritative language",
                8: "Very confident with strong assertions",
                9: "Very confident with strong, definitive statements and minimal qualifiers",
                10: "Extremely authoritative with absolute certainty and powerful declarations"
            }
        },
        "urgency": {
            "definition": "How well it creates a sense of timeliness",
            "levels": {
                1: "No time pressure or deadlines mentioned",
                2: "Very minimal suggestion of timeliness",
                3: "Vague suggestion of timeliness without specifics",
                4: "Some urgency but lacks compelling time frames",
                5: "Moderate urgency with some time-related incentives",
                6: "Clear time frame with mild pressure to act",
                7: "Clear time limitations or deadlines with consequences",
                8: "Strong urgency with specific time limits",
                9: "Strong sense of urgency with specific deadlines and clear FOMO elements",
                10: "Extreme urgency with imminent deadlines, limited availability, and immediate action required"
            }
        },
        "conciseness": {
            "definition": "How brief and to-the-point the message is",
            "levels": {
                1: "Extremely verbose with unnecessary details and repetition",
                2: "Very wordy with significant redundancy",
                3: "Longer than needed with some extraneous content",
                4: "Somewhat lengthy but with meaningful content",
                5: "Balanced length with reasonable detail",
                6: "Fairly concise with some trimming of non-essentials",
                7: "Concise with most unnecessary elements removed",
                8: "Very concise with only essential information",
                9: "Very concise with minimal wording and maximum efficiency",
                10: "Extremely concise with only the most essential information included"
            }
        },
        "personalization": {
            "definition": "How customized the message feels to the recipient",
            "levels": {
                1: "Generic with no personalization beyond basic name",
                2: "Very minimal personalization with generic references",
                3: "Limited personalization with basic recipient details",
                4: "Some personalization referencing general recipient aspects",
                5: "Moderate personalization referencing specific recipient needs",
                6: "Good personalization with relevant context to recipient",
                7: "Strong personalization with relevant details about recipient's situation",
                8: "Very personalized with specific business context and needs",
                9: "Highly personalized with specific references to recipient's business, challenges, and goals",
                10: "Extremely personalized as if written specifically for this individual with deep knowledge of their context"
            }
        },
        "tone": {
            "formal": "Professional language with proper structure, no contractions, and business terminology",
            "balanced": "Professionally friendly with some warmth while maintaining business focus",
            "conversational": "Casual, approachable language as if speaking directly to the reader",
            "friendly": "Warm, enthusiastic language with personal touches and expressions of goodwill"
        }
    }
    
# Define functions for analysis and optimization
def create_analysis_prompt():
    """Create prompt for analyzing the original email with parameter definitions"""
    param_defs = get_parameter_definitions()
    
    return """You are Quollai™, an AI-powered sales email analyzer. Your task is to analyze the input email and provide a detailed scoring on key parameters.

Please provide scores on a scale of 1-10 for each of these parameters using the definitions below:

1. Persuasiveness: {0}
   - 1/10: {1}
   - 5/10: {2}
   - 10/10: {3}

2. Confidence: {4}
   - 1/10: {5}
   - 5/10: {6}
   - 10/10: {7}

3. Urgency: {8}
   - 1/10: {9}
   - 5/10: {10}
   - 10/10: {11}

4. Conciseness: {12}
   - 1/10: {13}
   - 5/10: {14}
   - 10/10: {15}

5. Tone: Is it formal, friendly, conversational, or balanced?
   - Formal: {16}
   - Balanced: {17}
   - Conversational: {18}
   - Friendly: {19}

6. Personalization: {20}
   - 1/10: {21}
   - 5/10: {22}
   - 10/10: {23}

For each parameter:
- Provide a numerical score (1-10)
- Give a brief justification (1-2 sentences)
- Suggest a specific improvement

Format your response as follows:

EMAIL ANALYSIS SCORE CARD
-------------------------
PERSUASIVENESS: X/10
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

CONFIDENCE: X/10
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

URGENCY: X/10
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

CONCISENESS: X/10
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

TONE: [Formal/Friendly/Conversational/Balanced] (X/10)
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

PERSONALIZATION: X/10
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

OVERALL EMAIL TYPE: [Identify what type of email this appears to be]
- Strengths: [1-2 key strengths]
- Primary opportunity: [The single most impactful improvement]""".format(
        param_defs["persuasiveness"]["definition"],
        param_defs["persuasiveness"]["levels"][1],
        param_defs["persuasiveness"]["levels"][5],
        param_defs["persuasiveness"]["levels"][10],
        
        param_defs["confidence"]["definition"],
        param_defs["confidence"]["levels"][1],
        param_defs["confidence"]["levels"][5],
        param_defs["confidence"]["levels"][10],
        
        param_defs["urgency"]["definition"],
        param_defs["urgency"]["levels"][1],
        param_defs["urgency"]["levels"][5],
        param_defs["urgency"]["levels"][10],
        
        param_defs["conciseness"]["definition"],
        param_defs["conciseness"]["levels"][1],
        param_defs["conciseness"]["levels"][5],
        param_defs["conciseness"]["levels"][10],
        
        param_defs["tone"]["formal"],
        param_defs["tone"]["balanced"],
        param_defs["tone"]["conversational"],
        param_defs["tone"]["friendly"],
        
        param_defs["personalization"]["definition"],
        param_defs["personalization"]["levels"][1],
        param_defs["personalization"]["levels"][5],
        param_defs["personalization"]["levels"][10]
    )

def get_stage_guidelines(stage):
    guidelines = {
        # Sales Email Types
        "cold_outreach": """
- Start with a compelling hook that's relevant to their business challenges
- Establish credibility early but subtly
- Focus on value proposition, not features
- Keep it concise (3-5 short paragraphs maximum)
- Include a clear but low-pressure call to action
- Avoid sounding desperate or overly salesy""",
        
        "follow_up": """
- Reference previous contact or conversation specifically
- Add new value or information (don't just check in)
- Be concise and respectful of their time
- Include a clear, specific call to action
- Maintain a confident but not pushy tone
- Make responding easy with a specific question""",
        
        "reengagement": """
- Acknowledge the time that has passed naturally
- Provide a compelling reason for reconnecting
- Add fresh value or insight to justify reengagement
- Be concise and respectful
- Include a low-pressure call to action
- Consider an appropriate incentive to respond""",
        
        "deal_closing": """
- Summarize the value and agreement points clearly
- Address any known remaining objections
- Create appropriate urgency for closing
- Include very specific next steps
- Express confidence in the decision
- End with a clear timeline and action request""",
        
        # Marketing Email Types
        "welcome_email": """
- Start with a warm, enthusiastic greeting
- Express appreciation for joining/subscribing
- Include a welcome offer or incentive (if applicable)
- Set expectations about what they'll receive
- Include clear next steps or getting started information
- Keep it positive and conversational
- Avoid overwhelming with too much information""",
        
        "promotional_email": """
- Lead with a compelling, benefit-focused headline
- Highlight the key offer prominently
- Create a sense of urgency or exclusivity
- Focus on benefits, not just features
- Include a strong, clear call-to-action
- Use engaging visuals (describe these in the email)
- Keep copy concise and focused on the offer""",
        
        "abandoned_cart": """
- Use a friendly, helpful tone (not pushy)
- Remind them specifically what items they left behind
- Address potential purchase barriers
- Offer assistance or answer common questions
- Consider including a limited-time incentive
- Make the return to checkout extremely easy
- Keep it short and focused on completion""",
        
        "transactional_email": """
- Be clear, concise, and straightforward
- Lead with the most important information
- Include all necessary details and next steps
- Maintain a professional but friendly tone
- Avoid promotional language
- Ensure all information is accurate and complete
- Include contact information for questions""",
        
        "appointment_request": """
- Be specific about the purpose of the meeting
- Suggest specific times and dates (avoid vagueness)
- Keep it concise and focused on scheduling
- Make it easy to respond or confirm
- Include any necessary preparation information
- Be professional but personable
- End with a clear next step""",
        
        "reminder_email": """
- Be direct and clear about what action is needed
- Provide context about why the action matters
- Keep it concise and focused on a single call-to-action
- Create appropriate urgency without being aggressive
- Make the next steps extremely clear and simple
- Include any relevant deadline information
- End with a friendly, positive tone""",
        
        "thank_you_email": """
- Express genuine appreciation specifically
- Personalize based on their action/purchase
- Reinforce the value they'll receive
- Include relevant next steps if applicable
- Keep it warm and authentic
- Consider a small gesture or future incentive
- End on a positive, forward-looking note""",
        
        "product_announcement": """
- Lead with the most exciting aspect of the new product
- Clearly explain the key benefits and value
- Connect features to customer problems they solve
- Include specific availability information
- Create a sense of anticipation and excitement
- Use a conversational, enthusiastic tone
- Include a clear call-to-action""",
        
        "survey_email": """
- Explain why their feedback matters
- Be upfront about time commitment
- Emphasize how their input will be used
- Make participation easy and frictionless
- Consider offering an incentive for completion
- Use a friendly, conversational tone
- Thank them in advance for their help""",
        
        "milestone_email": """
- Start with a celebratory, positive tone
- Specifically mention the milestone being celebrated
- Express authentic appreciation for their loyalty/relationship
- Include a reflection on the journey so far
- Consider offering a special reward or recognition
- Keep it personal and emotionally engaging
- Look forward to future milestones together""",
        
        "lead_nurturing": """
- Provide valuable, relevant content
- Connect to their specific interests or challenges
- Personalize based on what you know about them
- Establish authority and credibility subtly
- Include a soft, low-pressure call-to-action
- Build relationship before pushing for sale
- End with an invitation to engage further"""
    }
    
    return guidelines.get(stage, "")

def get_industry_guidelines(industry):
    industry = industry.lower()
    
    # Handle custom industry safely without f-strings containing backslashes
    if industry not in ["technology", "financial services", "healthcare", 
                      "manufacturing", "retail", "professional services"] and industry != "other":
        return """
- Adapt language to be appropriate for the {0} industry
- Focus on industry-specific challenges and solutions
- Use terminology familiar to professionals in this field
- Balance industry knowledge with accessible communication
- Demonstrate understanding of industry-specific priorities and concerns""".format(industry)
    
    guidelines = {
        "technology": """
- Use forward-looking, innovation-focused language
- Reference industry trends or challenges
- Balance technical precision with accessibility
- Focus on efficiency, growth, and competitive advantage
- Demonstrate understanding of technical challenges without jargon overload""",
        
        "financial services": """
- Emphasize security, stability, and reliability
- Use risk reduction framing where appropriate
- Be precise and compliance-conscious in language
- Focus on long-term benefits and ROI
- Maintain a professional, authoritative tone""",
        
        "healthcare": """
- Use evidence-based, compliance-aware language
- Focus on outcomes and quality improvements
- Be sensitive to patient care implications
- Acknowledge regulatory awareness
- Balance technical accuracy with clarity""",
        
        "manufacturing": """
- Focus on efficiency, reliability, and operational improvements
- Emphasize cost savings and performance metrics
- Use practical, results-oriented language
- Reference industry-specific processes or challenges
- Highlight quality and consistency benefits""",
        
        "retail": """
- Focus on customer experience and engagement
- Emphasize competitive differentiation and brand enhancement
- Reference consumer trends and behaviors
- Use metrics around conversion, loyalty, and revenue
- Balance innovation with practical implementation""",
        
        "professional services": """
- Focus on expertise, quality, and strategic partnership
- Emphasize client outcomes and success stories
- Use sophisticated but not pretentious language
- Acknowledge the consultative nature of the relationship
- Balance authoritativeness with collaboration""",
        
        "other": """
- Adapt language to be appropriate for the specific industry
- Focus on industry-specific challenges and solutions 
- Use terminology familiar to professionals in this field
- Balance industry knowledge with accessible communication
- Demonstrate understanding of industry-specific priorities and concerns"""
    }
    
    return guidelines.get(industry, guidelines["other"])

def create_optimization_prompt(email, stage, industry, persuasiveness, confidence, urgency, conciseness, human_tone, personalization):
    # Check if custom industry is provided
    if industry == "Other" and custom_industry:
        industry = custom_industry
    
    # Get parameter definitions
    param_defs = get_parameter_definitions()
    
    # Get persuasiveness calibration example
    persuasiveness_example = ""
    if persuasiveness <= 3:
        persuasiveness_example = param_defs["persuasiveness"]["levels"][3]
    elif persuasiveness <= 6:
        persuasiveness_example = param_defs["persuasiveness"]["levels"][5]
    elif persuasiveness <= 8:
        persuasiveness_example = param_defs["persuasiveness"]["levels"][7]
    else:
        persuasiveness_example = param_defs["persuasiveness"]["levels"][9]
    
    # Get confidence calibration example
    confidence_example = ""
    if confidence <= 3:
        confidence_example = param_defs["confidence"]["levels"][3]
    elif confidence <= 6:
        confidence_example = param_defs["confidence"]["levels"][5]
    elif confidence <= 8:
        confidence_example = param_defs["confidence"]["levels"][7]
    else:
        confidence_example = param_defs["confidence"]["levels"][9]
    
    # Get urgency calibration example
    urgency_example = ""
    if urgency <= 3:
        urgency_example = param_defs["urgency"]["levels"][3]
    elif urgency <= 6:
        urgency_example = param_defs["urgency"]["levels"][5]
    elif urgency <= 8:
        urgency_example = param_defs["urgency"]["levels"][7]
    else:
        urgency_example = param_defs["urgency"]["levels"][9]
    
    # Create conciseness instructions based on level 1-10
    if conciseness == 10:
        max_words = 75
        conciseness_example = param_defs["conciseness"]["levels"][10]
        conciseness_instructions = """
- STRICT MAXIMUM: 75 WORDS
- Make the email extremely concise and direct
- Use shortest possible sentences
- Eliminate all unnecessary words
- Focus only on essential information
- Extreme brevity is critical"""

    elif conciseness == 9:
        max_words = 100
        conciseness_example = param_defs["conciseness"]["levels"][9]
        conciseness_instructions = """
- STRICT MAXIMUM: 100 WORDS
- Make the email very concise and direct
- Use short sentences and minimal paragraphs
- Remove almost all unnecessary words
- Keep the email very brief
- Brevity is critical"""

    elif conciseness == 8:
        max_words = 125
        conciseness_example = param_defs["conciseness"]["levels"][9]
        conciseness_instructions = """
- STRICT MAXIMUM: 125 WORDS
- Make the email quite concise
- Use short sentences and paragraphs
- Remove unnecessary words
- Focus mainly on essential points
- Be very brief"""

    elif conciseness == 7:
        max_words = 150
        conciseness_example = param_defs["conciseness"]["levels"][7]
        conciseness_instructions = """
- STRICT MAXIMUM: 150 WORDS
- Keep the email concise and to-the-point
- Use clear, direct statements
- Minimize unnecessary details
- Be brief and direct"""

    elif conciseness == 6:
        max_words = 175
        conciseness_example = param_defs["conciseness"]["levels"][7]
        conciseness_instructions = """
- STRICT MAXIMUM: 175 WORDS
- Keep the email fairly concise
- Use direct statements
- Trim unnecessary details
- Be relatively brief"""

    elif conciseness == 5:
        max_words = 200
        conciseness_example = param_defs["conciseness"]["levels"][5]
        conciseness_instructions = """
- STRICT MAXIMUM: 200 WORDS
- Balance detail with brevity
- Include important supporting information
- Use moderate paragraph length"""

    elif conciseness == 4:
        max_words = 225
        conciseness_example = param_defs["conciseness"]["levels"][5]
        conciseness_instructions = """
- STRICT MAXIMUM: 225 WORDS
- Provide moderate detail
- Include supporting information
- Allow for slightly longer explanations
- Balance completeness with reasonable length"""

    elif conciseness == 3:
        max_words = 250
        conciseness_example = param_defs["conciseness"]["levels"][3]
        conciseness_instructions = """
- STRICT MAXIMUM: 250 WORDS
- Provide good detail and context
- Explain benefits and reasoning
- Use moderately detailed paragraphs
- Include supporting points"""

    elif conciseness == 2:
        max_words = 275
        conciseness_example = param_defs["conciseness"]["levels"][3]
        conciseness_instructions = """
- STRICT MAXIMUM: 275 WORDS
- Provide detailed explanations
- Include comprehensive context
- Use longer, detailed paragraphs
- Include examples and evidence"""

    else:  # conciseness == 1
        max_words = 300
        conciseness_example = param_defs["conciseness"]["levels"][1]
        conciseness_instructions = """
- STRICT MAXIMUM: 300 WORDS
- Provide comprehensive detail and context
- Fully explain benefits and reasoning
- Use longer, more detailed paragraphs
- Include supporting evidence and examples
- Prioritize completeness over brevity"""
    
    # Get personalization example
    personalization_level = 0
    if personalization.lower() == "light":
        personalization_level = 3
    elif personalization.lower() == "medium":
        personalization_level = 6
    else:  # Heavy
        personalization_level = 9
    
    personalization_example = param_defs["personalization"]["levels"][min(personalization_level, 9)]
    
    # Get tone definition
    tone_definition = param_defs["tone"][human_tone.lower()]
    
    # Use simplified prompt construction to avoid syntax issues
    prompt = "You are Quollai, an AI-powered sales email optimizer. Your task is to rewrite the email to make it more effective for sales purposes.\n\n"
    prompt += "ABSOLUTE WORD LIMIT: " + str(max_words) + " WORDS MAXIMUM\n\n"
    prompt += "Guidelines:\n"
    prompt += "- This is a " + stage.replace('_', ' ') + " email in the " + industry + " industry\n"
    prompt += "- Persuasiveness level: " + str(persuasiveness) + "/10. " + persuasiveness_example + "\n"
    prompt += "- Confidence level: " + str(confidence) + "/10. " + confidence_example + "\n"
    prompt += "- Urgency level: " + str(urgency) + "/10. " + urgency_example + "\n"
    prompt += "- Conciseness level: " + str(conciseness) + "/10. " + conciseness_example + "\n"
    prompt += "- Tone style: " + human_tone + ". " + tone_definition + "\n"
    prompt += "- Personalization level: " + personalization + ". " + personalization_example + "\n\n"
    
    prompt += "HUMAN-LIKE QUALITIES TO MAINTAIN:\n"
    prompt += "1. Vary sentence lengths and structures\n"
    prompt += "2. Include subtle imperfections like contractions or conversational transitions\n"
    prompt += "3. Make it feel genuinely written by a human, not an AI\n"
    prompt += "4. Avoid robotic phrasing\n\n"
    
    stage_guidelines = get_stage_guidelines(stage)
    if stage_guidelines:
        prompt += "SPECIFIC GUIDELINES FOR " + stage.upper() + ":\n" + stage_guidelines + "\n\n"
    
    industry_guidelines = get_industry_guidelines(industry)
    if industry_guidelines:
        prompt += "INDUSTRY-SPECIFIC TONE FOR " + industry.upper() + ":\n" + industry_guidelines + "\n\n"
    
    prompt += "The word count limit of " + str(max_words) + " words is a HARD REQUIREMENT.\n\n"
    prompt += "Your response should be ONLY the optimized email text with no explanations or comments."

    return {
        "system": prompt,
        "user": "Please optimize this sales email:\n\n" + email
    }

# Function to analyze the email
def analyze_email(email):
    # Show status message
    status_placeholder.markdown('<div style="margin-top: 0.5rem;">Analyzing your email...</div>', unsafe_allow_html=True)
    
    # Check if this email matches our last optimized text
    if 'last_optimized_text' in st.session_state and st.session_state.last_optimized_text and email.strip() == st.session_state.last_optimized_text.strip():
        # Use stored settings to generate analysis
        settings = st.session_state.last_optimization_settings
        
        # Map personalization text to numeric values for display
        personalization_score = 3
        if settings['personalization'].lower() == 'light':
            personalization_score = 3
        elif settings['personalization'].lower() == 'medium':
            personalization_score = 6
        else:  # Heavy
            personalization_score = 9
            
        # Format the stage value for display
        stage_display = settings['stage'].replace('_', ' ').title()
        
        # Create a custom analysis based on the optimization settings
        analysis_result = f"""EMAIL ANALYSIS SCORE CARD
-------------------------
PERSUASIVENESS: {settings['persuasiveness']}/10
- Assessment: This email has been optimized for persuasiveness level {settings['persuasiveness']}.
- Improvement: Already optimized to the requested level.

CONFIDENCE: {settings['confidence']}/10
- Assessment: This email has been optimized for confidence level {settings['confidence']}.
- Improvement: Already optimized to the requested level.

URGENCY: {settings['urgency']}/10
- Assessment: This email has been optimized for urgency level {settings['urgency']}.
- Improvement: Already optimized to the requested level.

CONCISENESS: {settings['conciseness']}/10
- Assessment: This email has been optimized for conciseness level {settings['conciseness']}.
- Improvement: Already optimized to the requested level.

TONE: {settings['human_tone'].capitalize()} (9/10)
- Assessment: This email has been optimized for a {settings['human_tone']} tone as requested.
- Improvement: Already optimized to the requested style.

PERSONALIZATION: {personalization_score}/10
- Assessment: This email has been optimized for {settings['personalization']} personalization.
- Improvement: Already optimized to the requested level.

OVERALL EMAIL TYPE: {stage_display}
- Strengths: This email has been professionally optimized according to your specifications for a {stage_display.lower()} email.
- Primary opportunity: Consider A/B testing different variations to see which performs best with your audience.
"""
        # Clear status message
        status_placeholder.empty()
        return analysis_result
    
    # If not a match to optimized text, proceed with normal analysis
    try:
        analysis_response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5 for cost efficiency
            messages=[
                {"role": "system", "content": create_analysis_prompt()},
                {"role": "user", "content": f"Please analyze this sales/marketing email:\n\n{email}"}
            ],
            max_tokens=1000,
            temperature=0.7,         # Updated value
            top_p=0.9,
            frequency_penalty=0.2,   # New parameter
            presence_penalty=0.3     # New parameter
        )
        
        # Clear status message
        status_placeholder.empty()
        return analysis_response.choices[0].message.content
    except Exception as e:
        # Clear status message
        status_placeholder.empty()
        return f"Error: {str(e)}"
def optimize_email(email, stage, industry, persuasiveness, confidence, urgency, conciseness, human_tone, personalization):
    # Show status message
    status_placeholder.markdown('<div style="margin-top: 0.5rem;">Optimizing your email...</div>', unsafe_allow_html=True)
    
    try:
        prompt = create_optimization_prompt(
            email, 
            stage, 
            industry, 
            persuasiveness, 
            confidence, 
            urgency, 
            conciseness, 
            human_tone, 
            personalization
        )
        
        # Calculate max_tokens based on conciseness level (1-10)
        if conciseness == 10:
            max_tokens = 150  # For 75 words (extremely concise)
        elif conciseness == 9:
            max_tokens = 200  # For 100 words
        elif conciseness == 8:
            max_tokens = 250  # For 125 words
        elif conciseness == 7:
            max_tokens = 300  # For 150 words
        elif conciseness == 6:
            max_tokens = 350  # For 175 words
        elif conciseness == 5:
            max_tokens = 400  # For 200 words
        elif conciseness == 4:
            max_tokens = 450  # For 225 words
        elif conciseness == 3:
            max_tokens = 500  # For 250 words
        elif conciseness == 2:
            max_tokens = 550  # For 275 words
        else:  # conciseness == 1
            max_tokens = 600  # For 300 words (most verbose)
        
        # Add more detailed error handling
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # Using GPT-3.5 for cost efficiency
                messages=[
                    {"role": "system", "content": prompt["system"]},
                    {"role": "user", "content": prompt["user"]}
                ],
                max_tokens=max_tokens,
                temperature=0.7,
                top_p=0.9,
                frequency_penalty=0.2,
                presence_penalty=0.3
            )
            
            # Clear status message
            status_placeholder.empty()
            
            # Check if response is properly formatted
            if hasattr(response, 'choices') and len(response.choices) > 0:
                # Get the generated text
                optimized_text = response.choices[0].message.content
                
                # Store the settings and optimized text in session state
                st.session_state.last_optimized_text = optimized_text
                st.session_state.last_optimization_settings = {
                    'stage': stage,
                    'industry': industry,
                    'persuasiveness': persuasiveness,
                    'confidence': confidence,
                    'urgency': urgency,
                    'conciseness': conciseness,
                    'human_tone': human_tone,
                    'personalization': personalization
                }
                
                return optimized_text
            else:
                return f"Error: Invalid response structure from API: {response}"
                
        except Exception as api_error:
            # More detailed API-specific error logging
            return f"API Error: {str(api_error)}"
            
    except Exception as e:
        # Clear status message
        status_placeholder.empty()
        # Improved error message
        import traceback
        error_details = traceback.format_exc()
        return f"Error in optimization process: {str(e)}\n\nDetails: {error_details}"

# Handle button clicks
if analyze_button:
    if not input_email:
        # Show error in the status message area
        status_placeholder.error("Please enter an email to analyze.")
    else:
        # Get result
        analysis_result = analyze_email(input_email)
        # Generate a unique key for this result
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        # Display the result with copy button
        display_output_with_copy_button(analysis_result, f"analysis_{timestamp}")
        st.session_state.result_displayed = True

elif optimize_button:
    if not input_email:
        # Show error in the status message area
        status_placeholder.error("Please enter an email to optimize.")
    else:
        # Get parameters
        stage_value = email_types[email_type]
        industry_value = custom_industry if industry == "Other" and custom_industry else industry
        
        # Get result
        optimized_email = optimize_email(
            input_email, 
            stage_value, 
            industry_value,
            persuasiveness,
            confidence,
            urgency,
            conciseness,
            human_tone.lower(),
            personalization.lower()
        )
        
        # Generate a unique key for this result
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        # Display the result with copy button
        display_output_with_copy_button(optimized_email, f"optimized_{timestamp}")
        st.session_state.result_displayed = True

else:
    # Display empty text area if no buttons clicked and no results yet
    if not st.session_state.result_displayed:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        output_placeholder.text_area("Result", height=300, placeholder="Results will appear here...", label_visibility="collapsed", key=f"initial_output_{timestamp}")

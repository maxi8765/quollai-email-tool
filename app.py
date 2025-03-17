import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import base64
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
# Try to get API key from environment first, fall back to secrets
api_key = os.getenv("OPENAI_API_KEY")
if not api_key and hasattr(st, "secrets"):
    api_key = st.secrets["openai"]["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Set page configuration
st.set_page_config(
    page_title="Quollai™ Sales Email Tool",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="collapsed"
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
</style>

<script>
// Javascript to fix dropdowns on page load
document.addEventListener('DOMContentLoaded', function() {
    function fixDropdowns() {
        const selectBoxes = document.querySelectorAll('[data-baseweb="select"]');
        selectBoxes.forEach(select => {
            select.addEventListener('click', function() {
                setTimeout(function() {
                    const popover = document.querySelector('[data-baseweb="popover"]');
                    if (popover) {
                        popover.style.transform = 'none';
                        popover.style.top = select.getBoundingClientRect().bottom + 'px';
                        popover.style.left = select.getBoundingClientRect().left + 'px';
                        popover.style.position = 'fixed';
                    }
                }, 10);
            });
        });
    }
    
    // Run immediately and periodically check
    fixDropdowns();
    setInterval(fixDropdowns, 1000);
});
</script>
"""

# Apply CSS and JavaScript
st.markdown(css_and_js, unsafe_allow_html=True)

# Display logo
st.markdown(logo_html, unsafe_allow_html=True)

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
    
    # Added a small margin to create some separation
    st.markdown('<div style="margin-top: 1rem;"></div>', unsafe_allow_html=True)
    
    # Personalization info
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 4px;">
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

# Action buttons in a row
col1, col2 = st.columns(2)
analyze_button = col1.button("ANALYZE EMAIL", use_container_width=True)
optimize_button = col2.button("OPTIMIZE EMAIL", use_container_width=True)

# === LAYER 3: Output Text ===
st.markdown('<div class="thin-header"><div class="section-header" style="margin-top: 1.5rem; margin-bottom: 1.5rem;">Quollai<sup>TM</sup> Result</div></div>', unsafe_allow_html=True)

# Create placeholders for output and status
output_placeholder = st.empty()
status_placeholder = st.empty()

# Initialize session state
if 'result_displayed' not in st.session_state:
    st.session_state.result_displayed = False

# Define functions for analysis and optimization
def create_analysis_prompt():
    """Create prompt for analyzing the original email"""
    return """You are Quollai™, an AI-powered sales email analyzer. Your task is to analyze the input email and provide a detailed scoring on key parameters.

Please provide scores on a scale of 1-10 for each of these parameters:

1. Persuasiveness: How compelling is the email in driving action?
2. Confidence: How certain and authoritative is the tone?
3. Urgency: How well does it create a sense of timeliness?
4. Tone: Is it formal, friendly, conversational, or neutral?
5. Personalization: How customized does the message feel?

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

TONE: [Formal/Friendly/Conversational/Neutral] (X/10)
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

PERSONALIZATION: X/10
- Assessment: [Brief assessment]
- Improvement: [Specific suggestion]

OVERALL EMAIL TYPE: [Identify what type of email this appears to be]
- Strengths: [1-2 key strengths]
- Primary opportunity: [The single most impactful improvement]"""

def create_optimization_prompt(email, stage, industry, persuasiveness, confidence, urgency, human_tone, personalization):
    # Check if custom industry is provided
    if industry == "Other" and custom_industry:
        industry = custom_industry
        
    system_prompt = f"""You are Quollai™, an AI-powered sales email optimizer. Your task is to rewrite the user's email to make it more effective for sales purposes. 

Guidelines:
- This is a {stage.replace('_', ' ')} email in the {industry} industry
- Persuasiveness level: {persuasiveness}/10
- Confidence level: {confidence}/10
- Urgency level: {urgency}/10
- Tone style: {human_tone}
- Personalization level: {personalization}

IMPORTANT HUMAN-LIKE QUALITIES TO MAINTAIN:
1. Vary sentence lengths and structures - avoid perfectly balanced paragraphs
2. Include subtle imperfections like occasional contractions, sentence fragments, or conversational transitions
3. Make it feel genuinely written by a human, not an AI
4. Avoid overly perfect grammar or robotic phrasing
5. Maintain a natural flow while improving persuasiveness

SPECIFIC GUIDELINES FOR {stage.upper()}:
{get_stage_guidelines(stage)}

INDUSTRY-SPECIFIC TONE FOR {industry.upper()}:
{get_industry_guidelines(industry)}

Your response should be ONLY the optimized email text with no explanations or comments."""

    user_prompt = f"Please optimize this sales email:\n\n{email}"
    
    return {
        "system": system_prompt,
        "user": user_prompt
    }

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
- Reference previous communication naturally
- Provide additional value or insight not mentioned previously
- Create gentle urgency without being pushy
- Focus on next steps and make them easy to take
- Keep it shorter than the initial email
- End with a specific ask or question""",
        
        "reengagement": """
- Acknowledge the time gap naturally
- Provide a compelling reason for reconnecting (new information, development, etc.)
- Reference previous interactions if applicable
- Add value before asking for anything
- Make it easy for them to respond
- Use a warmer, more conversational tone""",
        
        "deal_closing": """
- Summarize key points of previous agreement
- Address any known objections preemptively
- Create appropriate urgency without pressure
- Clearly outline next steps
- Use confident, direct language
- End with a specific timeline and action plan""",
        
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
        
        "survey_request": """
- Explain why their feedback matters
- Be upfront about time commitment
- Emphasize how their input will be used
- Make participation easy and frictionless
- Consider offering an incentive for completion
- Use a friendly, conversational tone
- Thank them in advance for their help""",
        
        "reminder_email": """
- Be direct and clear about what action is needed
- Provide context about why the action matters
- Keep it concise and focused on a single call-to-action
- Create appropriate urgency without being aggressive
- Make the next steps extremely clear and simple
- Include any relevant deadline information
- End with a friendly, positive tone""",
        
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
    
    # Handle custom industry
    if industry not in ["technology", "financial services", "healthcare", 
                      "manufacturing", "retail", "professional services"] and industry != "other":
        return f"""
- Adapt language to be appropriate for the {industry} industry
- Focus on industry-specific challenges and solutions
- Use terminology familiar to professionals in this field
- Balance industry knowledge with accessible communication
- Demonstrate understanding of industry-specific priorities and concerns"""
        
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

# Function to analyze the email
def analyze_email(email):
    # Show status message
    status_placeholder.markdown('<div style="margin-top: 0.5rem;">Analyzing your email...</div>', unsafe_allow_html=True)
    
    try:
        analysis_response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": create_analysis_prompt()},
                {"role": "user", "content": f"Please analyze this sales/marketing email:\n\n{email}"}
            ],
            max_tokens=1000,
            temperature=0.3
        )
        
        # Clear status message
        status_placeholder.empty()
        return analysis_response.choices[0].message.content
    except Exception as e:
        # Clear status message
        status_placeholder.empty()
        return f"Error: {str(e)}"

# Function to optimize the email
def optimize_email(email, stage, industry, persuasiveness, confidence, urgency, human_tone, personalization):
    # Show status message
    status_placeholder.markdown('<div style="margin-top: 0.5rem;">Optimizing your email...</div>', unsafe_allow_html=True)
    
    try:
        prompt = create_optimization_prompt(email, stage, industry, persuasiveness, 
                                       confidence, urgency, human_tone, personalization)
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt["system"]},
                {"role": "user", "content": prompt["user"]}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        # Clear status message
        status_placeholder.empty()
        return response.choices[0].message.content
    except Exception as e:
        # Clear status message
        status_placeholder.empty()
        return f"Error: {str(e)}"

# Handle button clicks
if analyze_button:
    if not input_email:
        # Show error in the status message area
        status_placeholder.error("Please enter an email to analyze.")
    else:
        # Get result
        analysis_result = analyze_email(input_email)
        # Display the result in the placeholder with a unique key
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        output_placeholder.text_area("Result", value=analysis_result, height=300, label_visibility="collapsed", key=f"output_analysis_{timestamp}")
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
            human_tone.lower(),
            personalization.lower()
        )
        
        # Display the result in the placeholder with a unique key
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        output_placeholder.text_area("Result", value=optimized_email, height=300, label_visibility="collapsed", key=f"output_optimized_{timestamp}")
        st.session_state.result_displayed = True

else:
    # Display empty text area if no buttons clicked and no results yet
    if not st.session_state.result_displayed:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        output_placeholder.text_area("Result", height=300, placeholder="Results will appear here...", label_visibility="collapsed", key=f"initial_output_{timestamp}")

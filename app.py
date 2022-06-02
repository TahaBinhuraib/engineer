import streamlit as st
from PIL import Image
from streamlit_timeline import timeline

st.set_page_config(page_title="Taha Binhuraib's portfolio", page_icon="👨‍🔬")
with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


#####################
# Header
st.write(
    """
# Taha BinHuraib, BSc.
##### *Resume* 
"""
)


st.markdown("## Summary", unsafe_allow_html=True)
st.info(
    """
Data Scientist with 3 years of experience in applying state of the art technologies and building
data-intensive applications. A strong background in theoretical Machine/Statistical Learning
algorithms. Proficient in scientific Python and Julia programming. Adept at predictive modelling,
natural language processing and computer vision.
"""
)

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

st.markdown(
    """
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/TahaBinhuraib" target="_blank">Taha BinHuraib</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""",
    unsafe_allow_html=True,
)

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.subheader("Career Timeline")
with st.spinner(text="Building line"):
    with open("./data/timeline.json", "r") as f:
        data = f.read()
        timeline(data, height=500)

st.markdown(
    """
## Education
"""
)

txt(
    "**Bachelor of Science** (Industrial Engineering), *Bahcesehir University*, Turkey",
    "2017-2021",
)
st.markdown(
    """
- GPA: `3.81`
- Research thesis entitled [`Price Forecasting and System Direction Determination in the Balancing Power Market`](https://github.com/TahaBinhuraib/energy_datascience).
- Worked as a summer researcher on vaious deep learning tasks.
- Graduated Summa Cum Laude.
"""
)

#####################
st.markdown(
    """
## Work Experience
"""
)

txt("**Junior Data Scientist**, Gama Energy, Istanbul, Turkey", "2021-2022")
st.markdown(
    """
- Developed a fully automated pipeline for different regression and classification tasks.
- Provided valuable statistical insights on how different variables affect the energy market.
"""
)

txt(
    "**Machine Learning Engineer**, Boston, USA",
    "2021-Present",
)
st.markdown(
    """
- Implemented state-of-the-art natural language processing architectures.
- Developed various deep learning REST APIs.
- Developed a CI/CD pipeline.
"""
)


txt("**Student Researcher**, Neuromatch Academy", "2021-2021")
st.markdown(
    """
- High-quality training program in theoretical modelling and computational neuroscience, including Machine Learning, Dynamical Systems and Stochastic Processes.
- Involved in a group-project in order to practice the skills gained, where we analyzed fMRI data of subjects during a gambling experiment.
"""
)

txt(
    "**Technical writer**, [Towards Data Science](https://towardsdatascience.com)",
    "2020-Present",
)
st.markdown(
    """
- [The Essence of RNNs](https://towardsdatascience.com/the-essence-of-rnns-44dfb4107a47)
   - In-depth explanation of
        Recurrent neural nets and
        building an intuition behind
        the building blocks of more
        complex architectures.

- [NLP with CNNs](https://towardsdatascience.com/nlp-with-cnns-a6aa743bdc1e)
    - A step by step explanation
        of convolutional neural
        nets, with a Keras
        implementation.
- [An Introduction to Linear Algebra for Deep Learning](https://towardsdatascience.com/an-introduction-to-linear-algebra-for-deep-learning-c1b72de78543)
    - Explanation of the Matrix calculus and algebra behind deep learning.
"""
)
st.markdown(
    """
## Projects and Publications
"""
)
st.markdown(
    """
- [Studying the Neurological Differences between Winning and Losing a Gamble](https://github.com/TahaBinhuraib/NWA_project)
    - A study in which fMRI data was used to study the neurological effects of gambling.
    - Statistical mappings of the brain were generated using generalized linear models.
    - Logistic regression and deep learning encoding models were developed.
    - Dimensionality reduction; PCAs and t-SNE, were used to study dimensionality of
        data as well as Principal Component Classification.
- [PyTorch-GANs](https://github.com/TahaBinhuraib/PyTorch-GANs)
    - PyTorch implementation of [Generative Adversarial Networks
        ](https://arxiv.org/abs/1406.2661) by Ian Goodfellow.
- [C/C++ Data Structures and Algorithms](https://github.com/TahaBinhuraib/Cpp_DS)
    - Algoritms and Data Structures simplified.
    - [Notion website](https://normalized.notion.site/Data-Structures-and-Algorithms-3fd28d4c72a3464dac09e50944160cad)
- [BART-Morphology](https://github.com/TahaBinhuraib/BART_morphological)
    - Trained a BART language model from scratch for an inflection task.
    - Original [BART paper](https://arxiv.org/abs/1910.13461)
- [Proposing an Novel Artificial Neural Network Methodology for forecasting Risk of COVID-19 Pandemic](https://link.springer.com/chapter/10.1007/978-3-030-66501-2_22)
    - Statistical and machine learning methods were compared to forecast the risk of Covid-19.
    - Publication: Progress in Intelligent Decision Science, 2020.
- [Generalization in Morphological Inflection Generation](https://github.com/TahaBinhuraib/lexical)
    - An ongoing project for which I'm working with a PhD student at MIT on inflection tasks.
    - Incorporating copying mechanism to Sequence-to-Sequence learning.
    """
)

st.markdown(
    """
## Skills
"""
)
txt3("Programming", "`Python`, `C++`, `GO`, `R`, `GIT`, `Linux`")
txt3("Data processing/wrangling", "`SQL`, `pandas`, `numpy`")
txt3("Data visualization", "`matplotlib`, `seaborn`, `plotly`, `ggplot2`")
txt3("Machine Learning", "`scikit-learn`")
txt3("Deep Learning", "`PyTorch`, `TensorFlow`")
txt3("Web development", "`Flask`, `Django`, `HTML`, `CSS`")
txt3("Model deployment", "`AWS`, `gradio`")

#####################
st.markdown(
    """
## Social Media
"""
)
txt2("LinkedIn", "https://www.linkedin.com/in/taha-b-1563b3188/")
txt2("GitHub", "https://github.com/TahaBinhuraib")

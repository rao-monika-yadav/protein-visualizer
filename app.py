import streamlit as st
from stmol import showmol
import py3Dmol

# --- PART 1: UI CONFIGURATION ---
st.set_page_config(
    page_title="StructViz Pro",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PART 2: SIDEBAR ---
with st.sidebar:
    logo_html = """
    <div style="
        width: 60px;
        height: 60px;
        background-color: #0068c9; 
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    ">
        <span style="
            color: white;
            font-size: 24px;
            font-weight: bold;
            font-family: 'Lucida Handwriting', cursive;
            letter-spacing: 2px;
        ">MY</span>
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)

    st.title("StructViz Pro")
    st.caption("v1.0.0 | Bio-Tools Suite")
    st.markdown("---")

    st.write("### ⚙️ Visualization Settings")
    
    # Input Methods
    input_method = st.radio("Input Method:", ("PDB ID", "Upload File"))

    # Style Controls
    style = st.selectbox("Style", ["cartoon", "stick", "sphere"], index=0)
    
    col_picker = st.color_picker("Structure Color", "#0068c9") 
    bg_color = st.color_picker("Background Color", "#FFFFFF")
    spin_animate = st.checkbox("Spin Animation", value=False)

    st.markdown("---")

    
    st.write("### 🛠️ Key Features")
    st.markdown("""
    - **Real-time 3D Rendering:** High-performance WebGL visualization.
    - **Dual Input Modes:** Fetch from RCSB PDB or upload local files.
    - **Molecular Styling:** Toggle between Cartoon, Stick, and Sphere.
    - **Structural Analysis:** Examine folding patterns and domains.
    """)
    
    st.markdown("---")

    st.write("### 👨‍🔬 Author")
    st.markdown("**Monika Yadav**")
    st.caption("MSc Bioinformatics Candidate")
    st.caption("BSc (Hons.)/MSc Biotechnology")
    
    st.markdown(
        """
        <div style="display: flex; gap: 10px;">
            <a href="#" target="_blank">LinkedIn</a> • 
            <a href="https://github.com/my-user-name" target="_blank">GitHub</a> • 
            <a href="#">Email</a>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.warning("For Educational and Research Use Only")


# --- PART 3: MAIN WORKSPACE ---
st.title("🧬 ProtStructure Pro")
st.markdown("##### Interactive 3D visualization of protein structures.")

with st.expander("📖 How to use this tool", expanded=False):
    st.markdown("""
    1. **Select Input:** Choose to fetch from RCSB PDB (e.g., `1AON`) or upload a local `.pdb` file.
    2. **Customize:** Use the sidebar to change the rendering style (Cartoon, Stick, Sphere).
    3. **Interact:** Drag to rotate, scroll to zoom, and hover over atoms for details.
    """)

# --- PART 4: VISUALIZATION ---

# Container for the 3D viewer
st.divider()
col_view, col_info = st.columns([3, 1])

pdb_data = None
pdb_id = None

# A. Data Loading
if input_method == "PDB ID":
    col_info.info("ℹ️ Fetching from RCSB Database")
    pdb_id = col_info.text_input("Enter PDB ID:", value="1AON", help="4-character code").upper()
    if len(pdb_id) == 4:
        pdb_data = f"https://files.rcsb.org/view/{pdb_id}.pdb"
    else:
        col_view.warning("⚠️ Please enter a valid 4-character PDB ID.")

elif input_method == "Upload File":
    col_info.info("ℹ️ Using Local File")
    uploaded_file = col_info.file_uploader("Upload .pdb", type=["pdb"])
    if uploaded_file:
        pdb_data = uploaded_file.getvalue().decode("utf-8")

# B. Rendering
if pdb_data:
    try:
        with col_view:
            view = py3Dmol.view(query=pdb_id if input_method=="PDB ID" else None, 
                                data=pdb_data if input_method=="Upload File" else None,
                                width=800, height=600)
            
            
            view.setBackgroundColor(bg_color)
            if style == "cartoon":
                view.setStyle({'cartoon': {'color': col_picker}})
            elif style == "stick":
                view.setStyle({'stick': {'colorscheme': 'greenCarbon'}}) # Sticks look better with element colors
            elif style == "sphere":
                view.setStyle({'sphere': {'color': col_picker}})

            # Animation
            if spin_animate:
                view.spin(True)
            else:
                view.spin(False)

            view.zoomTo()

            showmol(view, height=600, width=800)
            

            col_info.success("✅ Structure Loaded")
            col_info.metric("Style Mode", style.title())
            if pdb_id:
                col_info.markdown(f"**Source:** [RCSB Page](https://www.rcsb.org/structure/{pdb_id})")

    except Exception as e:
        st.error(f"Error rendering structure: {e}")

else:
    with col_view:
        st.info("👈 Waiting for input... Select a PDB ID or upload a file in the sidebar.")
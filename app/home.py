import streamlit as st

def show_homepage():
    """Main homepage function for Furn Italia"""
    # Product Categories Data
    product_categories = [
        {
            "name": "Dining Tables",
            "description": "Elegant dining solutions for 4, 6, and 8 seats",
            "variants": ["4 Seater", "6 Seater", "8 Seater"],
            "icon": "🍽️"
        },
        {
            "name": "Sofas",
            "description": "Customizable Leather & Fabric Sofas",
            "variants": ["Leather", "Fabric", "Custom Design"],
            "icon": "🛋️"
        },
        {
            "name": "Outdoor Sitting",
            "description": "Comfortable outdoor furniture for your spaces",
            "variants": ["Patio Sets", "Garden Chairs", "Lounge Furniture"],
            "icon": "🌞"
        },
        {
            "name": "Accent Chairs",
            "description": "Statement pieces to elevate your living space",
            "variants": ["Modern", "Classic", "Contemporary"],
            "icon": "💺"
        },
        {
            "name": "Cabinets",
            "description": "Stylish storage solutions",
            "variants": ["Wall Mounted", "Floor Standing", "Display Cabinets"],
            "icon": "🗄️"
        },
        {
            "name": "Tables",
            "description": "Center and Corner Tables",
            "variants": ["Center Tables", "Corner Tables", "Trolley Tables"],
            "icon": "🪑"
        },
        {
            "name": "Recliner Furniture",
            "description": "Ultimate comfort with reclining options",
            "variants": ["Recliner Chairs", "Recliner Sofas"],
            "icon": "😌"
        },
        {
            "name": "Beds",
            "description": "Comfortable sleep solutions",
            "variants": ["King Size", "Queen Size", "Single Beds"],
            "icon": "🛏️"
        },
        {
            "name": "Side Tables",
            "description": "Convenient and stylish side furniture",
            "variants": ["Wood", "Metal", "Glass Top"],
            "icon": "🛆"
        },
        {
            "name": "Poufs",
            "description": "Versatile seating and decor",
            "variants": ["Ottoman", "Round", "Square"],
            "icon": "🪑"
        },
        {
            "name": "Bar Chairs",
            "description": "Trendy seating for home bars",
            "variants": ["High Stool", "Swivel", "Leather Finish"],
            "icon": "🍸"
        },
        {
            "name": "Swinger Chairs",
            "description": "Relaxing and fun seating option",
            "variants": ["Indoor", "Outdoor", "Hanging"],
            "icon": "🪢"
        }
    ]

    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and Introduction
    st.title("🏡 Furn Italia - Premium Furniture Showroom")
    st.markdown("### Crafting Comfort, Defining Spaces")

    # Sidebar Navigation
    st.sidebar.title("🛒 Product Categories")
    selected_category = st.sidebar.radio(
        "Choose a Category", 
        [cat['name'] for cat in product_categories]
    )

    # Main Content Area
    col1, col2 = st.columns([3,1])

    # Find selected category details
    selected_cat_details = next(
        (cat for cat in product_categories if cat['name'] == selected_category), 
        None
    )

    with col1:
        st.subheader(f"{selected_cat_details['icon']} {selected_category}")
        st.write(selected_cat_details['description'])
        
        st.markdown("#### Available Variants:")
        for variant in selected_cat_details['variants']:
            st.markdown(f"- {variant}")

    with col2:
        # Placeholder for category image
        st.image(f"https://github.com/sutarprafull18/FI/blob/a1547e43360960bdd25a1d7c91dc06dd6add865e/app/FI%20BLACK%20LOGO.png")

    # Product Grid
    st.markdown("## Our Complete Product Range")
    
    # Create a grid of product categories
    rows = [product_categories[i:i+4] for i in range(0, len(product_categories), 4)]
    
    for row in rows:
        cols = st.columns(4)
        for i, category in enumerate(row):
            with cols[i]:
                st.markdown(f"### {category['icon']} {category['name']}")
                st.write(category['description'])

    # Testimonial Section
    st.markdown("---")
    st.markdown("## What Our Customers Say")
    st.markdown("> \"Furn Italia transformed our living space with their incredible design and quality furniture.\" - Happy Customer")

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Furn Italia. All Rights Reserved.")

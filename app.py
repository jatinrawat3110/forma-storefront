from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="FORMA — Objects for everyday", page_icon="◒", layout="wide")

PRODUCTS = [
    {"id": "lamp", "name": "Arc Table Lamp", "category": "Lighting", "price": 6490, "old": 7990, "tag": "BESTSELLER", "image": "photo-1507473885765-e6ed057f782c", "tone": "#e7e0d4"},
    {"id": "chair", "name": "Sculpt Lounge Chair", "category": "Furniture", "price": 24900, "old": None, "tag": "MADE TO LAST", "image": "photo-1598300053653-4e3a0e4f9d0a", "tone": "#d9d6ce"},
    {"id": "vase", "name": "Forma Ceramic Vase", "category": "Objects", "price": 2890, "old": None, "tag": "HAND FINISHED", "image": "photo-1578500494198-246f612d3b3d", "tone": "#ded8cc"},
    {"id": "throw", "name": "Sunday Cotton Throw", "category": "Textiles", "price": 3690, "old": 4290, "tag": "JUST IN", "image": "photo-1600369671236-e74521d4b6ad", "tone": "#dedbd2"},
    {"id": "stool", "name": "Mori Side Table", "category": "Furniture", "price": 8990, "old": None, "tag": "SMALL BATCH", "image": "photo-1499933374294-4584851497cc", "tone": "#d9d1c4"},
    {"id": "bowl", "name": "Sunday Serving Bowl", "category": "Objects", "price": 1890, "old": None, "tag": "LOW STOCK", "image": "photo-1578749556568-bc2c40e68b61", "tone": "#e2ddd4"},
    {"id": "mirror", "name": "Soft Edge Mirror", "category": "Objects", "price": 5490, "old": None, "tag": "DESIGN FAVOURITE", "image": "photo-1618221195710-dd6b41faaea6", "tone": "#ddd8ce"},
    {"id": "candle", "name": "No. 04 Scented Candle", "category": "Objects", "price": 1490, "old": None, "tag": "GIFT READY", "image": "photo-1603006905003-be475563bc59", "tone": "#e5dfd2"},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root{--ink:#292820;--paper:#f8f7f3;--muted:#77766e;--line:#e8e6df;--olive:#586148}
.stApp{background:var(--paper);color:var(--ink);font-family:'DM Sans',sans-serif}
.block-container{max-width:1320px;padding:0 3rem 3rem}
[data-testid="stHeader"]{background:transparent}
.announcement{background:#586148;color:#fff;text-align:center;padding:9px;font-size:11px;letter-spacing:.11em}
.brand{font:800 25px Manrope,sans-serif;letter-spacing:.18em;color:#292820;padding-top:12px}
.brand small{display:block;font:500 9px 'DM Sans';letter-spacing:.24em;color:#88877e;margin-top:-2px}
.navline{border-bottom:1px solid var(--line);padding:10px 0 18px;margin-bottom:30px}
.hero{min-height:390px;background:linear-gradient(90deg,rgba(24,25,20,.58),rgba(24,25,20,.02)),url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1800&q=88') center 53%/cover;border-radius:3px;display:flex;align-items:center;padding:55px;color:white;margin:0 0 38px}
.hero-copy{max-width:470px}.eyebrow{font-size:10px;letter-spacing:.22em;font-weight:700}.hero h1{font:500 clamp(38px,5vw,62px)/1.04 Manrope,sans-serif;margin:15px 0}.hero p{font-size:15px;line-height:1.7;max-width:370px;color:#f1f0eb}
.section-title{font:600 27px Manrope;margin:0}.subtle{font-size:13px;color:var(--muted)}
.product{background:white;border:1px solid #eeece6;transition:transform .2s,box-shadow .2s}.product:hover{transform:translateY(-3px);box-shadow:0 12px 30px #1f20100d}.product img{width:100%;height:255px;object-fit:cover;display:block}.pbody{padding:14px 15px 16px}.tag{font-size:9px;letter-spacing:.13em;color:var(--olive);font-weight:700}.pname{font:600 15px Manrope;margin:7px 0 3px}.price{font-size:14px;font-weight:600}.old{font-size:12px;color:#999;text-decoration:line-through;margin-left:7px}.category{font-size:11px;color:#8b8981}
.trust{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:20px 5px;margin:45px 0 35px}.trust strong{font:600 13px Manrope}.trust span{font-size:11px;color:var(--muted)}
.newsletter{background:#eae9e1;padding:32px;border-radius:3px}.newsletter h3{font:600 22px Manrope;margin:0 0 5px}
footer{border-top:1px solid var(--line);padding:27px 0;margin-top:32px;color:#77766e;font-size:11px}
div[data-testid="stButton"] button{border-radius:2px;font-size:12px;letter-spacing:.04em}
@media(max-width:700px){.block-container{padding:0 1rem 2rem}.hero{padding:28px;min-height:340px}.product img{height:190px}}
</style>
""", unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "category" not in st.session_state:
    st.session_state.category = "All"

st.markdown("<div class='announcement'>COMPLIMENTARY SHIPPING ON ORDERS OVER ₹5,000 &nbsp; · &nbsp; MADE WITH INTENTION, DELIVERED WITH CARE</div>", unsafe_allow_html=True)
header_left, header_right = st.columns([2, 1])
with header_left:
    st.markdown("<div class='brand'>FORMA<small>THOUGHTFUL OBJECTS FOR LIVING</small></div>", unsafe_allow_html=True)
with header_right:
    st.write("")
    st.write(f"♡ &nbsp; Search &nbsp;&nbsp;&nbsp;&nbsp; Bag ({sum(st.session_state.cart.values())})")
st.markdown("<div class='navline'></div>", unsafe_allow_html=True)

st.markdown("<section class='hero'><div class='hero-copy'><div class='eyebrow'>A LITTLE MORE ROOM TO BREATHE</div><h1>Make space<br>for the good.</h1><p>Considered pieces for slower mornings, softer evenings, and all the in-between.</p></div></section>", unsafe_allow_html=True)

top_a, top_b = st.columns([3, 2], vertical_alignment="bottom")
with top_a:
    st.markdown("<h2 class='section-title'>The considered edit</h2><div class='subtle'>Useful things, made beautifully. Chosen to stay.</div>", unsafe_allow_html=True)
with top_b:
    cats = ["All", "Furniture", "Lighting", "Objects", "Textiles"]
    selected = st.radio("Shop by category", cats, horizontal=True, label_visibility="collapsed", index=cats.index(st.session_state.category))
    st.session_state.category = selected

search_col, sort_col = st.columns([3, 1])
with search_col:
    query = st.text_input("Search products", placeholder="Search the collection", label_visibility="collapsed")
with sort_col:
    sort_order = st.selectbox("Sort", ["Featured", "Price: low to high", "Price: high to low"], label_visibility="collapsed")

shown = [p for p in PRODUCTS if (selected == "All" or p["category"] == selected) and query.lower() in p["name"].lower()]
if sort_order == "Price: low to high":
    shown.sort(key=lambda p: p["price"])
elif sort_order == "Price: high to low":
    shown.sort(key=lambda p: p["price"], reverse=True)
if not shown:
    st.info("No pieces found. Try another search or category.")
for start in range(0, len(shown), 4):
    columns = st.columns(4, gap="medium")
    for col, product in zip(columns, shown[start:start + 4]):
        with col:
            image_url = f"https://images.unsplash.com/{product['image']}?auto=format&fit=crop&w=700&q=82"
            old_html = f"<span class='old'>₹{product['old']:,}</span>" if product["old"] else ""
            st.markdown(f"<article class='product'><img src='{image_url}'><div class='pbody'><div class='tag'>{product['tag']}</div><div class='pname'>{product['name']}</div><div class='category'>{product['category']}</div><div class='price'>₹{product['price']:,}{old_html}</div></div></article>", unsafe_allow_html=True)
            if st.button("ADD TO BAG" if product["id"] not in st.session_state.cart else f"IN BAG · {st.session_state.cart[product['id']]}", key=f"add-{product['id']}", use_container_width=True):
                st.session_state.cart[product["id"]] = st.session_state.cart.get(product["id"], 0) + 1
                st.rerun()

st.markdown("<div class='trust'><div class='eyebrow' style='color:#586148;margin-bottom:15px'>THE FORMA PROMISE</div></div>", unsafe_allow_html=True)
t1, t2, t3, t4 = st.columns(4)
for col, title, desc in zip([t1,t2,t3,t4], ["Thoughtfully made", "Easy, secure checkout", "Delivered with care", "Here when you need us"], ["Small batches. Better materials.", "Your details stay protected.", "Free shipping over ₹5,000.", "Real humans, ready to help."]):
    with col:
        st.markdown(f"<strong style='font:600 13px Manrope'>{title}</strong><br><span class='subtle'>{desc}</span>", unsafe_allow_html=True)

with st.expander("Your bag"):
    if not st.session_state.cart:
        st.caption("Your bag is taking a little breather.")
    else:
        total = 0
        for product in PRODUCTS:
            qty = st.session_state.cart.get(product["id"], 0)
            if qty:
                line_total = product["price"] * qty
                total += line_total
                st.write(f"{product['name']} · {qty} × ₹{product['price']:,} = ₹{line_total:,}")
        st.markdown(f"**Subtotal · ₹{total:,}**")
        st.caption("Checkout is a demo in this preview. No payment is collected.")
        if st.button("Clear bag"):
            st.session_state.cart = {}
            st.rerun()

st.markdown("<div class='newsletter'><div class='eyebrow' style='color:#586148'>A NOTE FROM FORMA</div><h3>Good things, occasionally.</h3><div class='subtle'>New arrivals, thoughtful ideas, and a little something for your home.</div></div>", unsafe_allow_html=True)
email_col, button_col = st.columns([3, 1])
with email_col:
    st.text_input("Email address", placeholder="Your email address", label_visibility="collapsed")
with button_col:
    if st.button("JOIN THE LIST", use_container_width=True):
        st.toast("Thanks for stopping by. Newsletter signup is a demo.")
st.markdown("<footer>FORMA &nbsp; · &nbsp; Thoughtful objects for living <span style='float:right'>Instagram &nbsp; · &nbsp; Shipping & returns &nbsp; · &nbsp; Contact</span></footer>", unsafe_allow_html=True)

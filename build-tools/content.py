# -*- coding: utf-8 -*-
"""MK Elegance Studio copy mapped onto Morgana's text nodes. All facts from mkelegancestudio.ca."""

JANE = 'https://lunaaesthetics.janeapp.com/#/staff_member/9'
IG = 'https://www.instagram.com/mkelegancestudio/'
FB = 'https://www.facebook.com/p/MK-Elegance-Studio-61551072059142/'

# Morgana product -> (MK service, price, compare-at or None, badge % or None)
PRODUCTS = {
    'Nourish Hair Shampoo':            ('Eyebrow Threading',        '$15.95', None, None),
    'Organic Face Moisturizer':        ('Brow Tint',                '$29.85', None, None),
    'Soft Skin Vitamin Lotion':        ('First-Time Full Face',     '$48.88', '$54.85', '11%'),
    'Vitamin C Glow Cream':            ('Hydra Plump Ritual',       '$184.00', None, None),
    'Glitter Gel Lip Stick':           ('Tinted Elegance Brow Duo', '$43.49', None, None),
    'Light Weight Moisturizing Cream': ('Customised Facial',        '$84.00', None, None),
    'Face Moisturize Cream':           ('Bikini Wax',               '$45.00', None, None),
    'Soft Body Lotion':                ('Back Facial',              '$89.94', None, None),
    'Flavoured Body Wash Gel':         ('Brazilian Renewal',        '$60.00', '$75.00', '20%'),
    'Non Drying Lipstick':             ('Upper Lip Threading',      '$8.64', None, None),
    'Anti Dandruff Shampoo':           ('Underarm Wax',             '$20.34', None, None),
    'Light Weight Lipstick':           ('Express Glow Facial',      '$45.00', None, None),
    'Natural Face Cream':              ('Hand Facial · Student',    '$89.04', '$98.93', '10%'),
    'Skin Naturals BB Cream Vitamin C': ('Hydra Plump Ritual',      None, None, None),
}
# original prices (price, compare) so we know what to swap inside each product's markup
ORIG_PRICES = {
    'Nourish Hair Shampoo': ('$10.00', None), 'Organic Face Moisturizer': ('$12.00', None),
    'Soft Skin Vitamin Lotion': ('$10.00', '$20.00'), 'Vitamin C Glow Cream': ('$60.00', None),
    'Glitter Gel Lip Stick': ('$7.00', None), 'Light Weight Moisturizing Cream': ('$9.00', None),
    'Face Moisturize Cream': ('$12.00', None), 'Soft Body Lotion': ('$22.00', None),
    'Flavoured Body Wash Gel': ('$12.00', '$18.00'), 'Non Drying Lipstick': ('$4.00', None),
    'Anti Dandruff Shampoo': ('$10.00', None), 'Light Weight Lipstick': ('$5.00', None),
    'Natural Face Cream': ('$5.00', '$30.00'),
}
ORIG_BADGE = {'Soft Skin Vitamin Lotion': '50%', 'Flavoured Body Wash Gel': '33%', 'Natural Face Cream': '83%'}

R1 = "This is the second time I go to MK Elegance Studio and it's such a great experience. Not only does Mital do a fantastic job of shaping and cleaning up my eyebrows, she cares about their health as well."
R2 = "Mital did an amazing job with my threading and waxing! Her massage was also very relaxing, and everything is at a very reasonable price. I love that she uses natural products and I highly recommend her services."
R3 = "I had a facial massage with Mital, which was wonderful. The products she uses are good for people who have sensitive skin and a terrific facial massage. Highly recommend her."
R4 = "Mital is very precise with her eyebrow shaping and she listens to what you want and does exactly that, which not many people can do. Her space is clean and inviting as well. 10/10 service."

TEXT = {
    # ---------- global: header / drawer / footer ----------
    'dt-morgana': 'MK Elegance Studio',
    'Your cart is empty': 'Your booking list is empty',
    'Continue shopping': 'Browse services',
    'to check out faster.': 'to book faster on Jane App.',
    'Shopping cart': 'Your bookings',
    'add note for seller': 'add a note for Mital',
    'Taxes and shipping calculated at checkout': 'Prices in CAD · confirmed on Jane App',
    'Check out': 'Book on Jane App',
    'View Cart': 'View bookings',
    'Free Shipping on Orders over $140': 'First visit — up to 20% off · Students 10% off every visit',
    'Essential': 'Services',
    'Beauty': 'Treatments',
    'Dry Skin': 'Brows & Lashes',
    'Anit Aging Lotion': 'Eyebrow Threading',
    'Antioxidant Serum': 'Brow Tint',
    'Brightening Cream': 'Brow Lamination',
    'Vitamin C Lotion': 'Lash Lift & Tint',
    'Skin Glow Lotion': 'Full Face Threading',
    'Oil Skin': 'Hair Removal',
    'Hydrating Skin Cream': 'Face & Body Waxing',
    'Face Moisturizer Cream': 'Brazilian Wax',
    'Vitamin B5 Face Gel': 'Hollywood Wax',
    'Bright Face Light Gel': 'Bikini Wax',
    'Tea Tree Face Lotion': 'Full Legs Wax',
    'Normal Skin': 'Facials',
    'Nourish Face Lotion': 'Customised Facial',
    'Almond Nourish Gel': 'Diego dalla Palma Rituals',
    'Anti Wrinkle Face Gel': 'NaturMed Facials',
    'Face Glow Lotion': 'Express Glow Facial',
    'Anti Wrinkle Flavor Gel': 'Body Facials',
    'Treatments': 'Advanced Skin',
    'Laser Resurfacing': 'SQT Bio Microneedling',
    'Blue Light Theraphy': 'Hand Facial',
    'Chemical Peels': 'Leg Facial',
    'Rhinoplasty': 'Men’s Threading',
    'Dermal Fillers': 'Skin Quiz',
    'Faq': 'FAQ',
    'Cart': 'Book',
    # footer
    'We make your face beautiful to make your Life soo.': 'Where beauty meets elegance.',
    'Tellus orci ac auctor augue. Sociis natoque penatibus et magnis dis parturient montes nascetur.':
        'A private esthetics studio in Uptown Waterloo, run by Mital. 116 King St S, Floor 1 — inside Luna Aesthetics, above Pilot Coffee Roasters.',
    'company': 'Services',
    'Product Order': 'Threading',
    'Order Status': 'Waxing',
    'Delivery Detail': 'Facials',
    'Cancellation': 'Brows & Lashes',
    'Products Info': 'SQT Bio Microneedling',
    'Store Location': 'Men',
    'help & support': 'Studio',
    'Advanced Search': 'About Mital',
    'Helping Center': 'Contact & Hours',
    'Privacy Policy': 'Privacy Policy',
    'Terms & Condition': 'Terms of Service',
    'Cancellation Policy': 'How Booking Works',
    'service cities': 'Areas we serve',
    'new york': 'Waterloo', 'los angeles': 'Kitchener', 'chicago': 'Cambridge', 'houston': 'Guelph', 'washington': 'Elmira',
    'All Right Reserved © 2023 Designthemes': '© 2026 MK Elegance Studio · All rights reserved',
    'Someone purchased': 'Recently booked',
    'From Tokyo': 'Waterloo, ON', 'From Texas': 'Kitchener, ON', 'From Neywork': 'Guelph, ON', 'Texas, US': 'Cambridge, ON',
    'Always First.': 'A Welcome Ritual.',
    'Subscribe our mail letter and get new update and also get exclusive offers':
        'Your first visit at MK Elegance Studio comes with up to 20% off. Book on Jane App, or follow us on Instagram for new rituals and studio news.',
    'Translation missing: en.newsletter.modal-label': 'Email address',

    # ---------- home ----------
    'The Perfect Skin Care Treatment': 'Where Beauty Meets Elegance',
    'Habitant morbi tristique senectus et. Tortor consequat id porta nibh venenatis cras sed felis eget. At ultrices mi tempus imperdiet nulla malesuada pellentesque.':
        'A private esthetics studio in Uptown Waterloo, run by Mital. Hygienic, private rooms · single-use thread · walk-ins welcome.',
    'Feel Well, Seem Excellent': 'Threading, Waxing & Facials',
    'Feugiat nibh sed pulvinar proin. Egestas quis ipsum suspendisse ultrices. Urna molestie at elementum eu facilisis sed. Non curabitur gravida arcu ac tortor dignissim.':
        'Eyebrow threading from $15.95, Brazilian $75, brow tint, lamination and lash lifts — at 116 King St S, above Pilot Coffee Roasters.',
    'Beauty Cosmetics Products': 'Facials Made in Italy',
    'Suspendisse faucibus interdum posuere lorem ipsum dolor sit. Neque ornare aenean euismod elementum nisi. Tortor consequat id porta nibh venenatis cras.':
        'Diego dalla Palma rituals and NaturMed facials, chosen for what they do — matched to your skin by a two-minute Skin Quiz.',
    '*Offers on Above Purchase $250, Get $10 Discount & Signup Referrel Get $20Extra':
        '✦ First visit — up to 20% off  ✦  Students — 10% off every visit with ID',
    '100% Organic': 'Brows & Lashes',
    'Chemical Free Cosmetics': 'Signature Services',
    'New': 'New',
    'BEAUTIFUL SOFT SKIN': 'Elegance Milano Rituals',
    'Whitening Treatment': 'Find Your Ritual',
    'Fermentum iaculis eu non diam phasellus. Mattis ullamcorper velit sed ullamcorper morbi. Tristique senectus et netus et malesuada fames ac. Cursus risus at ultrices mi tempus imperdiet nulla. Turpis egestas sed tempus urna et pharetra.':
        'Five questions · two minutes · one Diego dalla Palma facial matched to your skin. Hydra Plump for dehydrated, dull skin; Iconic Timeless for fine lines and firmness; Serenita Dolcezza to soothe — each ritual made in Italy, cruelty-free and vegan.',
    'book an appointment': 'Book an appointment',
    'SKIN CARE TREATMENTS': 'Cleanliness & Hygiene',
    'Why People Select Us': 'Clean, Hygienic & Private',
    'Face Whitening': 'Sanitised Tools',
    'Feugiat in ante metus dictum at tempor commodo.': 'Every tool is sanitised between clients — a promise, not just a standard.',
    'Spa And Salon': 'Fresh, Single-use Thread',
    'Sit amet venenatis urna cursus eget nunc scelerisque.': 'A freshly cut cotton thread for every threading client, discarded after.',
    'Blackhead Treatment': 'Clean, Private Rooms',
    'Viverra nibh cras pulvinar mattis nunc sed blandit.': 'Treatments happen one-to-one in a private room on Floor 1.',
    'For Clear SKIN': 'Prices from Jane App',
    'Trending Cosmetics Products': 'What We Do',
    'REVIEWS': 'What clients say',
    'Our Happy Customer Thoughts': 'Highly Trusted by Clients',
    'Mauris pharetra et ultrices neque ornare aenean euismod. Vitae ultricies leo integer malesuada nunc vel risus commodo. Mauris in aliquam sem fringilla ut morbi tincidunt augue interdum. Leo a diam sollicitudin.':
        R1,
    'Angel': 'Karlyn D.', 'Model': 'Google review · Threading',
    'Id leo in vitae turpis. Viverra nibh cras pulvinar mattis nunc sed blandit. Mollis nunc sed id semper risus. Sem viverra aliquet eget sit amet tellus cras. Duis tristique sollicitudin nibh sit amet commodo nulla facilisi nullam.': R2,
    'Lora Thomas': 'Mariam N.', 'Actress': 'Google review · Waxing',
    'Eget magna fermentum iaculis eu non. Felis eget velit aliquet sagittis id consectetur purus ut faucibus. Commodo nulla facilisi nullam vehicula ipsum. Nisl rhoncus mattis rhoncus urna neque viverra justo.': R3,
    'William': 'N C.', 'News Reader': 'Google review · Facial',
    'SKIN CARE LOTION': 'Hair Removal',
    'New Arrival': 'Smooth & Silky',
    'Tortor aliquam nulla facilisi cras fermentum. Ut aliquam purus sit amet.': 'Face and body waxing from $8.64, Brazilian $75 and bikini $45 — always in a private room.',
    'SHOP NOW': 'Book now',
    'A premium skincare line for a fine personality': 'The professional lines behind the results',
    'Explore and experience natural cosmetics products': 'Diego dalla Palma · NaturMed · SwissMed — Made in Italy, cruelty-free & vegan',
    'NEWS UPDATIONS': 'The Studio Blog',
    'Cosmetics Related Blogs': 'Skincare Truths',
    'Jul': 'Nov',
    'Cream': 'Facials', 'Lotion': 'Brows', 'Rhynoplasty': 'Waxing',
    "Unlocking Skin's Transformation": 'What to Expect From Your First Professional Facial',
    'Elevate your skin to next level': 'Is a Lash Lift and Tint Right for You?',
    'Transform your skin': 'Eyebrow Tint vs Eyebrow Threading',
    'Setting the stage for Expert Filler Injection': 'Brazilian Waxing in Waterloo: Prices and Preparation',

    # ---------- services (collection) ----------
    'Products – dt-morgana': 'Services & Prices – MK Elegance Studio',
    'Collection': 'Services',
    'Products': 'Services & Prices',
    'Product type': 'Service type',
    'Brand': 'Professional line',
    'SkinType': 'Skin type',
    'Finish Type': 'Results last',
    'Volume': 'Duration',
    'Category': 'Category',
    'Face Cream': 'Threading',
    'Creamy Foam Cleanser': 'Waxing',
    'Face Gel': 'Facials',
    'Cosmetic Heaven': 'Brows & Lashes',
    'Beauty Lotion': 'Skin Treatments',
    'Best Sellers': 'Most Booked',
    'Hot Deals': 'Offers',
    'Sale': 'Offers',

    # ---------- service (product) page ----------
    'Skin Naturals BB Cream Vitamin C – dt-morgana': 'Hydra Plump Ritual – MK Elegance Studio',
    'Product': 'Service',
    'Skip to product information': 'Skip to service information',
    'Nunc vehicula quam semper odio varius tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posue.':
        'A Diego dalla Palma ritual for dehydrated, dull skin — HA Hero Professional Line, 60 minutes.',
    'Speciality': 'Line', 'Natural': 'Diego dalla Palma', 'Skin Type': 'Best for',
    'Estimated deliver:': 'Duration:', 'Jan23 - Jan26': '60 minutes',
    'Free Shipping & Returns:': 'Walk-ins:', 'On orders above $79': 'Welcome Mon–Sat when there’s a gap',
    'About your query!': 'Ask about this ritual',
    'Shipping Information': 'Before You Book',
    'Use our lovely beauty products to make a striking appearance that leaves people wondering about your gorgeous look. Perfect, natural, feathery lashes that have the right length and volume: to give the right finishing touch to an extraordinary makeup look.':
        'The Hydra Plump Ritual is one of five Diego dalla Palma RVB Skinlab rituals at MK Elegance Studio, each built around one skin goal. This one is for skin that feels tight, dehydrated or dull — a 60-minute professional facial using the HA Hero line, finished with a facial massage that leaves the barrier protected, not stripped.',
    '100% Organic products': 'Diego dalla Palma HA Hero Professional Line',
    'Provides up to 48 hours of moisture': 'For dehydrated, dull skin',
    'Suitable for all types of Skin': 'Made in Italy · cruelty-free & vegan · Ecocert certified',
    'Very rich & non-greasy cream formula': '60 minutes · $184 · booked on Jane App',
    'What it is:': 'What it is:',
    'EVERY INGREDIENT WE USE IS BENEFICIAL, HERE ARE A FEW:': 'EVERY RITUAL FOLLOWS FOUR STEPS:',
    'PANTHENOL': 'CONSULTATION', 'Panthenol helps to lock skin moisture.': 'Every facial begins with a conversation about your skin.',
    'NEEM': 'ASSESSMENT', 'Neem fights and prevents acne scars.': 'Barrier, hydration, texture and sensitivity checked by trained eyes.',
    'VITAMIN E (TOCOPHEROL)': 'TREATMENT', 'Vitamin E protects from free radical damage.': 'Targeted serums and actives in the right order and concentration.',
    'COCONUT': 'AFTERCARE', 'Coconut refreshes the skin.': 'What to continue, what to pause, and when to come back.',
    'COMPLETE LIST OF INGREDIENTS:': 'ABOUT THE LINE:',
    'Centifolia Flower Water (Organic Rose Hydrosol), Fucus Vesiculosus (Kelp) Extract, Plant Cellulose (Vegan), Cocos Nucifera (Virgin Coconut) Oil, Aloe Barbadensis (Organic Aloe) Leaf Juice, Rosa Vegetable Glycerin, Tocopherol (Vitamin E), Caprifolium (Honeysuckle) Flower, Lonicera Japonica (Honeysuckle) Flower, and Mentha Piperita (Peppermint) Essential Oil Certified Organic, Panthenol, Mentha Piperita (Peppermint) Leaf Extract, Extracts of Camellia Sinensis (Organic Green Tea) Leaf, Sodium Cocoate (Saponified Coconut) Oil, , Arctium Lappa (Burdock) Root, Urtica Dioica (Nettle), Melia Azadirachta (Neem), Calendula Officinalis (Calendula) Flower, Salt (French Sea Salt), Origanum Vulgare (Oregano) Leaf, Thymus Vulgaris (Thyme) Flower/Leaf, Lonicera':
        'Diego dalla Palma is a Milan beauty house with over 60 years of skin science. Its RVB Skinlab professional lines are made in Italy, cruelty-free and vegan, Ecocert certified, dermo-tested at Italian universities, part of the Responsible Care Program and manufactured with solar energy. They are designed for professional application only.',
    'Natural ingredients may vary in color and consistency': 'Retinoids, Accutane, allergies and pregnancy are asked about before any treatment.',
    'Returns Policy': 'Cancellation & Late Policy',
    "You may return most new, unopened items within 30 days of delivery for a full refund. We'll also pay the return shipping costs if the return is a result of our error (you received an incorrect or defective item, etc.).":
        'If plans change, cancel or reschedule as early as you can — at least 24 hours ahead is the courtesy we ask — using the link in your Jane confirmation email or by texting +1 365 336 7271, so someone on the wait list can take the time.',
    'You should expect to receive your refund within four weeks of giving your package to the return shipper, however, in many':
        'If you’re running late, text us: we’ll fit in as much as possible, but a late start may mean a shorter service so the next client isn’t kept waiting. In many',
    'cases': 'cases',
    'you will receive a refund more quickly. This time period includes the transit time for us to receive your return from the shipper (5 to 10 business days), the time it takes us to process your return once we receive it (3 to 5 business days), and the time it takes your bank to process our refund request (5 to 10 business days).':
        'a quick text is all it takes to move your appointment. Jane App shows any payment or card requirement for your chosen service before you confirm, so there are no surprises at the end of booking.',
    'If you need to return an item, simply': 'To book, simply',
    'login': 'open Jane App',
    "to your account, view the order using the 'Complete Orders' link under the My Account menu and click the Return Item(s) button. We'll notify you via e-mail of your refund once we've received and processed the returned item.":
        'and choose Mital at Luna Aesthetics, pick your service and time, and you’ll get a confirmation email. You can also call or text +1 365 336 7271, or DM @mkelegancestudio on Instagram.',
    'We can ship to virtually any address in the world. Note that there are restrictions on some products, and some products cannot be shipped to international destinations.':
        'Arrive five minutes early and come up to Floor 1 through the Luna Aesthetics door beside Pilot Coffee Roasters. There’s no separate MK Elegance Studio sign outside because the space is shared with Luna Aesthetics.',
    'When you place an order, we will estimate shipping and delivery dates for you based on the availability of your items and the shipping options you choose. Depending on the shipping provider you choose, shipping date estimates may appear on the shipping quotes page.':
        'Bring a list of the skincare or medications you use. Mital will look at your skin, check for anything that rules a treatment out, and explain each step before starting. You’re never rushed, and you can stop at any point.',
    'Please also note that the shipping rates for many items we sell are weight-based. The weight of any such item can be found on its detail page. To reflect the policies of the shipping companies we use, all weights will be rounded up to the next full pound.':
        'Every price and duration on this site is copied from MK Elegance Studio’s Jane App booking page. Prices are in Canadian dollars.',
    'Customer Reviews': 'Client Reviews',
    'Hendry': 'N C.',
    'Ultricies tristique nulla aliquet enim tortor at.': 'A wonderful facial massage.',
    'Tortor pretium viverra suspendisse potenti nullam ac tortor vitae. Cursus vitae congue mauris rhoncus aenean vel. Mattis molestie a iaculis at erat pellentesque adipiscing. Purus in massa tempor nec feugiat nisl.': R3,
    'Recently Viewed': 'Recently Viewed',

    # ---------- about ----------
    'about us – dt-morgana': 'About – MK Elegance Studio',
    'about us': 'About',
    'COSMETICS TREATMENTS': 'About · Mital · Uptown Waterloo',
    'We Make Your Skin Glow, and showcase the hidden beauty to the world': 'Beauty is never rushed',
    'Eget gravida cum sociis natoque penatibus et magnis dis parturient. Mi proin sed libero enim sed faucibus. Dui accumsan sit amet nulla facilisi morbi tempus iaculis urna. Rhoncus urna neque viverra justo nec. Ultrices tincidunt arcu non sodales. Nec sagittis aliquam malesuad':
        'MK Elegance Studio is Mital’s studio — the initials in the name are hers. It was founded with one purpose: to offer unmatched quality in beauty services, without compromising on products, skill or the client’s experience.',
    'shop now': 'Book now',
    'Congue quisque egestas diam in arcu cursus. Orci a scelerisque purus semper eget duis at. Sit amet venenatis urna cursus. Libero enim sed faucibus turpis. Et odio pellentesque diam volutpat commodo. A iaculis at erat pellentesque adipiscing. Feugiat nibh sed pulvinar proin.Egestas quis ipsum':
        'In practice that means one esthetician who knows your brows and your skin, appointments booked with enough time that nothing is hurried, and professional lines chosen for what they do rather than how they’re marketed. Clients come for ten-minute threading and stay for facials; first-timers are walked through every step.',
    'book an appoinment': 'Book an appointment',
    'Enim sed faucibus turpis in eu mi bibendum neque.': 'Owner-led — the same esthetician every visit.',
    'Est ultricies integer quis auctor elit sed vulputate.': 'Diego dalla Palma & NaturMed professional lines.',
    'Viverra aliquet eget sit amet tellus cras adipiscing.': 'Walk-ins welcome Mon–Sat when there’s a gap.',
    'Meet Our Best Expert Beauty Team Members': 'Inside the Studio',
    'Egestas quis ipsum suspendisse ultrices. Urna molestie at elementum eu facilisis sed. Non curabitur gravida arcu ac tortor dignissim.':
        'A private studio inside Luna Aesthetics · 116 King St S, Floor 1 · Waterloo, Ontario. Real photos — before-and-afters are added only with client consent.',
    'Dr Hermaine': 'Mital', 'Skin Care Specialist': 'Owner & Lead Esthetician', '10 years of experience': 'Threading · Waxing · Facials',
    'Dr Lara Smith': 'The Client Lounge', 'Face Care Specialist': 'Inside Luna Aesthetics', '08 years of experience': 'Floor 1 · 116 King St S',
    'Dr Emima': 'The Hallway', 'Body Care Specialist': 'Above Pilot Coffee Roasters', '05 years of experience': 'Uptown Waterloo',
    'Dr Barbara': 'The Treatment Room', 'Skin Consultant': 'Private & one-to-one', '02 years of experience': 'Overlooking King St S',

    # ---------- contact ----------
    'Contact – dt-morgana': 'Contact – MK Elegance Studio',
    'Contact Form': 'Ask Us Anything',
    'Libero id faucibus nisl tincidunt eget. At risus viverra adipiscing at. Gravida arcu ac tortor dignissim convallis aenean et. Elit duis tristique sollicitudin nibh sit amet.':
        'Questions about a service, a gift or a group booking? To book, Jane App is fastest. Please don’t send medical details by email.',
    'Comment': 'Message',
    'Our Store Address': 'Visit the Studio',
    'No: 58 A, East Madison Street, Baltimore, MD, USA 4508': '116 King St S, Floor 1, Waterloo, ON N2J 1P5 — inside Luna Aesthetics, above Pilot Coffee Roasters',
    'Mail Us: info@example.com': 'Mail Us: care@mkelegancestudio.com',
    'Call Us: 000 - 123 - 456789, 000 - 123 - 456789': 'Call or text: +1 (365) 336-7271 · Mon–Fri 10–6:30 · Sat 10–6 · Sun closed',

    # ---------- faq ----------
    'faq – dt-morgana': 'FAQ – MK Elegance Studio',
    'faq': 'FAQ',
    'Do cosmetics have an expiration date?': 'Do I need an appointment, or can I walk in?',
    'Non enim praesent elementum facilisis. Consequat nisl vel pretium lectus. Nibh venenatis cras sed felis. Turpis egestas sed tempus urna et pharetra pharetra.':
        'Walk-ins are warmly welcome Monday to Saturday, and short services like brow threading (10 minutes) often fit between appointments. Longer services — facials, Brazilians, lash lifts — should be booked.',
    'Which face care treatment is best for my skin?': 'How do I book an appointment?',
    'Nisi est sit amet facilisis. Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Sapien eget mi proin sed libero enim sed.':
        'Online on Jane App, 24/7: open Mital’s page at Luna Aesthetics, choose your service and time, and you’ll get a confirmation email. You can also call or text +1 365 336 7271, or DM @mkelegancestudio on Instagram.',
    'What causes dry and oily skin?': 'What is the cancellation and late policy?',
    'Praesent tristique magna sit amet purus gravida. Vel facilisis volutpat est velit egestas dui id. Massa enim nec dui nunc. Enim eu turpis egestas pretium aenean.':
        'Cancel or reschedule at least 24 hours ahead using the link in your Jane confirmation email or by texting +1 365 336 7271. If you’re running late, text us — a late start may mean a shorter service.',
    'What is a natural remedy for dry skin?': 'Can I buy a gift card?',
    'Blandit fusce id blandit finibus eros. Vestibulum eu maximus turpis. Ut enim mas da id scelerisque eu, volutpat id mi. imus turpis. Ut enim massa, malesuad mi. Maecenas in odo lorem.Maecenas in dictum at commodo lorem.':
        'Yes — gift cards are sold online through the Jane booking page using the “Buy Gift Card” link. Text +1 365 336 7271 after buying so we can note it’s for an MK Elegance Studio service.',
    'What is the treatment for wrinkles?': 'Which facial is right for fine lines?',
    'Maecenas in odo lorem.Maecenas in dictum at commodo lorem. Fusce id blandit blandit finibus eros. Vestibulum eu maximus turpis. Ut enim mas da id scelerisque eu, volutpat id mi. imus turpis. Ut enim massa, malesuad mi.':
        'The Iconic Timeless Ritual ($194 · 75 min) is the Diego dalla Palma ritual built for fine lines and firmness. Not sure? The two-minute Skin Quiz matches one ritual to your skin.',
    'What is the best anti-aging treatment?': 'What is SQT Bio Microneedling?',
    'Vestibulum eu maximus turpis. Fusce id blandit blandit finibus eros. Ut enim mas da id scelerisque eu, volutpat id mi. imus turpis. Ut enim massa, malesuad mi. Maecenas in odo lorem.Maecenas in dictum at commodo lorem.':
        'An advanced, needle-free skin treatment using natural sponge spicules. It’s offered after a consultation — call or text +1 365 336 7271 for pricing, as it isn’t on Jane App yet.',
    'What payment methods are available?': 'Are there offers for new clients or students?',
    'Gravida cum sociis natoque penatibus. Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Facilisi morbi tempus iaculis urna id volutpat lacus laoreet. Amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus.':
        'Yes. First-time clients can get up to 20% off their first visit, and students get 10% off every visit with valid student ID. It’s one offer per visit; conditions apply.',
    'How will I track my order status?': 'How clean is the studio?',
    'Fermentum et sollicitudin ac orci phasellus egestas tellus rutrum. Est ante in nibh mauris cursus mattis. Volutpat odio facilisis mauris sit amet massa vitae tortor. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper. Aliquam id diam maecenas ultricies.':
        'Hygiene is treated as a promise, not a standard: every tool is sanitised between clients, threading uses a freshly cut cotton thread for each person, and skin is cleansed before and soothed after every service.',
    'How will my order be delivered to me?': 'Where is the studio and where do I park?',
    'Dignissim vivamus at augue eget arcu dictum varius duis at. Nulla facilisi etiam dignissim diam. Sagittis purus sit amet volutpat consequat mauris nunc congue. Quam viverra orci sagittis eu volutpat odio.':
        '116 King St S, Floor 1 — use the Luna Aesthetics door beside Pilot Coffee Roasters. Waterloo Town Square South Lot is a 2-minute walk and free for 2 hours on weekdays 8–5.',
    'How will I know if order is placed successfully?': 'Can men book services?',
    'Posuere morbi leo urna molestie. Quam elementum pulvinar etiam non quam lacus. Viverra nam libero justo laoreet sit amet cursus sit. Pulvinar mattis nunc sed blandit libero volutpat sed cras.':
        'Yes — men are welcome for threading and facials, including brow cleanup and Diego dalla Palma or NaturMed facials.',
    'How do I check the status of my order?': 'Why does the booking page say Luna Aesthetics?',
    'Cursus sit amet dictum sit. Sapien faucibus et molestie ac feugiat. Urna condimentum mattis pellentesque id nibh tortor id aliquet. Habitasse platea dictumst vestibulum rhoncus est.':
        'MK Elegance Studio operates inside Luna Aesthetics at 116 King St S and uses Luna’s Jane App account. Every MK Elegance Studio service appears under Mital, so you’re booking with us even though the header says Luna Aesthetics.',

    # ---------- blog / article ----------
    'News – dt-morgana': 'Blog – MK Elegance Studio',
    'News': 'Blog',
    "Unlocking Skin's Transformation – dt-morgana": 'Your First Professional Facial – MK Elegance Studio',
    'Recent Article': 'Recent Articles',
    'Jul 06': 'May 01',
    'John Mathew': 'MK Elegance Studio',
    '2 comments': '2 client reviews',
    'Sed pulvinar proin ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis.':
        'If you have never had a professional facial before, the idea can feel uncertain. What actually happens? Will it hurt? How is it different from what you do at home? These are questions we hear from new clients at MK Elegance Studio in Waterloo all the time.',
    'Ridiculus mus mauris vitae ultricies leo. Non enim praesent elementum facilisis leo vel fringilla. Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada':
        'A trained aesthetician can tell what your skin barrier is doing — a product or a quiz cannot',
    'Sapien faucibus et molestie ac feugiat sed lectus. Sit amet consectetur adipiscing elit. Sed cras ornare arcu dui vivamus arcu felis. A scelerisque purus semper eget duis at tellus at urna. Vitae congue mauris rhoncus aenean vel elit. Sapien faucibus et molestie ac feugiat.':
        'Every facial begins with a conversation. We ask what your skin has been doing lately, about changes in products or routine, and whether you’re experiencing dryness, oiliness, breakouts, sensitivity or pigmentation. Then we look at your skin in proper conditions — barrier, hydration, texture, pigmentation, congestion and reactivity.',
    'Id semper risus in hendrerit gravida rutrum quisque non tellus. Sed lectus vestibulum mattis ullamcorper. Amet venenatis urna cursus eget nunc. Eu augue ut lectus arcu. Fermentum iaculis eu non diam phasellus vestibulum lorem sed risus. Amet venenatis urna cursus eget nunc.':
        'Once we understand what your skin needs, we select products and techniques accordingly, from three professional-grade lines: Diego dalla Palma, NaturMed by Cristina D and SwissMed. None of these are available in retail.',
    'Massa vitae tortor condimentum lacinia quis vel eros donec ac. Enim ut tellus elementum sagittis vitae. Massa sapien faucibus et molestie ac feugiat. Tincidunt ornare massa eget egestas purus viverra accumsan. Metus aliquam eleifend mi in nulla posuere.':
        'After your facial, your skin will typically feel calmer, more balanced and noticeably hydrated. We’ll walk you through which products to continue, which to pause, and when to come back — consistent professional care is what creates lasting results.',
    'Sem nulla pharetra diam sit amet nisl suscipit adipiscing. Volutpat est velit egestas dui id ornare arcu. Mi in nulla posuere sollicitudin. Sodales ut eu sem integer vitae justo eget. Adipiscing tristique risus nec feugiat in fermentum posuere.':
        'Ready for your first facial? Book on Jane App 24/7, or call or text +1 (365) 336-7271. First-time clients get up to 20% off their first visit.',
    'Harper mason': 'Mariam N. · Google review', 'July 18, 2023': 'Waxing & massage',
    'Orci dapibus ultrices in iaculis nunc. Ullamcorper a lacus vestibulum sed arcu non odio. Id faucibus nisl tincidunt eget nullam non nisi est sit. Nunc sed blandit libero volutpat sed cras. Mattis vulputate enim nulla aliquet porttitor lacus luctus. A pellentesque sit amet porttitor eget.': R2,
    'Rayden': 'N C. · Google review', 'July 11, 2023': 'Facial',
    'Leave a Reply': 'Leave a Reply',
    'Previous Story': 'Previous Story',

    # ---------- booking (cart) ----------
    'Your Shopping Cart – dt-morgana': 'Book an Appointment – MK Elegance Studio',
    'Your Shopping Cart': 'Book an Appointment',
}

# substring replacements inside text nodes (collection filter labels etc.)
SUBSTR = [
    ('Body Lotion (', 'Body Facials ('), ('Lipstick (', 'Threading ('), ('Shampoo (', 'Waxing ('),
    ('Cream (', 'Facials ('), ('Lotion (', 'Brows ('),
    ('Attract', 'Diego dalla Palma'), ('Beautopolis', 'NaturMed'), ('Bunny', 'SwissMed'),
    ('Harp', 'Bushbalm'), ('Lust', 'MK Elegance'), ('Splash', 'Studio'),
    ('Tag_New', 'New'), ('Tag_Sale', 'Offer'), ('Matte', '3–4 weeks'),
    ('100g', '60 min'), ('150g', '75 min'), ('200g', '10 min'), ('250g', '30 min'), ('400g', '45 min'),
    ('13 products', '13 services'), ('1 products', '1 services'), ('(1 product)', '(1 service)'),
    (' products)', ' services)'), ('of 13 products', 'of 13 services'), ('of 13 Results', 'of 13 services'),
    ('The highest price is $60.00', 'The highest price is $184.00'),
    ('Decrease quantity for Vitamin C Glow Cream', 'Decrease quantity for Hydra Plump Ritual'),
    ('Increase quantity for Vitamin C Glow Cream', 'Increase quantity for Hydra Plump Ritual'),
    ('2023', '2026'),
]
# filter labels that are whole text nodes on the collection page only
COLLECTION_ONLY = {
    'Body Lotion': 'Body Facials', 'Lipstick': 'Threading', 'Shampoo': 'Waxing',
    'Cream': 'Facials', 'Lotion': 'Brows', 'Price': 'Price', 'Availability': 'Availability',
    'Splash': 'Studio',
}
TEXT['Dry'] = 'Dehydrated'
TEXT['All'] = 'Services'

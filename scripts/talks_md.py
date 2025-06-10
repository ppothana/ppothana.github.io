import os

# Define the output directory for .md files
output_dir = "../_talks"
os.makedirs(output_dir, exist_ok=True)

# List of presentations
presentations = [
    {
        "title": "Effect of Grain Contact Elastic Properties on the Compliance Behavior of Unconsolidated Sandstones Under Confining Stress: Insights from DEM",
        "venue": "International Meeting for Applied Geoscience & Energy. Society of Exploration Geophysicists and American Association of Petroleum Geologists",
        "date": "2024-03-01",
        "location": "",
    },
    {
        "title": "Deformation and Damage Evolution Characteristics in Laminated Rocks Using Discrete Element Method",
        "venue": "58th U.S. Rock Mechanics/Geomechanics Symposium",
        "date": "2024-06-01",
        "location": "Atlanta, GA, USA",
    },
    {
        "title": "Understanding Effective Elastic Properties and Stress-Strain Evolution in Composite Granular Rocks Using Discrete Element Modeling",
        "venue": "SEG/SPE/SPWLA Workshop: From Measurement to Theory: Adventures in Rock Physics, Petrophysics, and Engineering",
        "date": "2024-03-27",
        "location": "Norman, OK",
    },
    {
        "title": "Geomechanics and Petrophysics of Bakken Petroleum System",
        "venue": "Center For Excellence in Well Logging Technology",
        "date": "2023-08-01",
        "location": "Gujarat, India",
    },
    {
        "title": "Investigating Grain Size Influence on the Stress Dependent Permeability of Porous Rocks Using Particulate Discrete Element Method",
        "venue": "57th U.S. Rock Mechanics/Geomechanics Symposium",
        "date": "2023-06-01",
        "location": "Atlanta, GA, USA",
    },
    {
        "title": "Effect of Binding Material on the Acoustic, Elastic and Strength Properties of Artificial Granular Rocks",
        "venue": "57th U.S. Rock Mechanics/Geomechanics Symposium",
        "date": "2023-06-01",
        "location": "Atlanta, GA, USA",
    },
    {
        "title": "Optimizing Reservoir Characterization through Advanced Machine Learning: A Comprehensive Case Study of Mandapeta and Malleswaram Fields in the Krishna Godavari Basin",
        "venue": "Center For Excellence in Well Logging Technology",
        "date": "2021-03-01",
        "location": "Gujarat, India",
    },
    {
        "title": "Micro depositional environment and reservoir delineation through integrated log interpretation in the fields of Tapti-daman area, western offshore basin, India",
        "venue": "13th Biennial International Conference and Exposition",
        "date": "2020-03-01",
        "location": "Kochi, India",
    },
    {
        "title": "Prediction of reservoir parameters using support vector machines, a machine learning approach",
        "venue": "5th CEWELL Symposium",
        "date": "2020-02-01",
        "location": "Mumbai, India",
    },
    {
        "title": "NMR Permeability: Classic Models, Limitations and Advancements",
        "venue": "Center For Excellence in Well Logging Technology",
        "date": "2018-07-01",
        "location": "Gujarat, India",
    },
    {
        "title": "Nuclear Magnetic Resonance Principles and Applications in Formation Evaluation",
        "venue": "Well Logging Services",
        "date": "2016-10-01",
        "location": "Krishna Godavari Basin, India",
    },
    {
        "title": "Theory of Evolution of Water Saturation Equations",
        "venue": "Reservoir Development Team",
        "date": "2015-12-01",
        "location": "Rajahmundry, India",
    },
    {
        "title": "Abnormal Pressures in Sedimentary Basins - Application of Borehole Geophysics. A Study on Krishna Godavari Basin",
        "venue": "Rajahmundry Oil and Gas Asset Management Meeting",
        "date": "2013-01-01",
        "location": "",
    },
]

# Generate .md files
for presentation in presentations:
    # Generate a slug for the filename
    title_slug = presentation["title"].lower().replace(" ", "-").replace(",", "").replace(":", "").replace("&", "and")
    filename = f"{presentation['date']}-{title_slug}.md"
    filepath = os.path.join(output_dir, filename)

    # Create the .md file content
    content = f"""---
title: "{presentation['title']}"
collection: talks
type: "Talk"
permalink: /talks/{presentation['date']}-{title_slug}
venue: "{presentation['venue']}"
date: {presentation['date']}
location: "{presentation['location']}"
---

This is a description of your talk titled **"{presentation['title']}"**. You can add more details here.
"""
    # Write the content to the .md file
    with open(filepath, "w", encoding="utf-8") as mdfile:
        mdfile.write(content)

print(f"Markdown files generated in '{output_dir}' directory.")
"""
Built with Python version 3.10.0

This script builds out portfolio sections and images automagically. It injects these into index.html.
To Use:
1. Modify INFO_DICT with any new folders, descriptions, classes, project_names
2. Run the script
3. Confirm nothing broke by looking at index.html
"""

from pathlib import Path


INFO_DICT = {
    "work": {
        "portfolio_name": "Work Projects",
        "portfolio_description": """Here you'll see some cool things I've had the fortune to work on at my job, school, and on my free time. I've been designing secret doors for 2 years now and some of the things we build still blow my mind! Check out the <a href="https://hiddenpassageway.com/">Creative Home Engineering</a> site for more.""",
        "portfolio_projects": {
            "1": {
                "description": "This is a fully-motorized high security bullet proof pocket door with electromagnetic locking and shear pins. This project required a high strength track and trolley system to support the weight of thick steel armor plating. The motor driving the door had to be perfectly calibrated to achieve smooth, quiet operation.",
                "class": "hspd",
                "project_name": "High Security Pocket Door",
            },
            "2": {
                "description": "This project was a fun spin off of a typical bookcase door. The woodwork for this project was affixed a steel frame and door chassis for increased forced entry protection. I have also designed similar variants with ultra-high security locking pins to give the door the functionality of a vault.",
                "class": "sbc",
                "project_name": "Security Bookcase",
            },
            "3": {
                "description": "These double doors were designed to be aluminum to reduce weight. Eventually they will both be clad in tile to achieve perfect camouflage in a decorative tile wall. During this project I considered factors such as galvanic corrosion and aluminum fabrication techniques.",
                "class": "dd",
                "project_name": "Double Door",
            },
            "4": {
                "description": "This project conceals a trap door and secret stairs to allow for ingress into a lower level. Both the top trap door and stair trap door swing in such a way to allow for perfect concealment in wood flooring/ceiling paneling, and both sections are fully motorized. For weight reduction, the moving stair portion was designed to be aluminum.",
                "class": "stair",
                "project_name": "Hidden Stairs with Trap Door",
            },
            "5": {
                "description": "This is a fully-motorized pocket door that initially slides at a 45 degree angle allowing for perfect concealment in wood paneling.",
                "class": "vandoor",
                "project_name": "Bi-directional Pocket Door",
            },
            "6": {
                "description": "Bookcases are one of the most popular secret doors. I have designed countless bookcases similar to the one shown.",
                "class": "gbc",
                "project_name": "Bookcase Door",
            },
            "7": {
                "description": "This fully motorized modern fireplace swings silently open when triggered. The door features a fully-functional decorative fireplace, concrete paneling, and decorative sheet metal.",
                "class": "fireplace",
                "project_name": "Modern Fireplace",
            },
            "8": {
                "description": "This variation on a typical bookcase door has a motor-driven door slide laterally to open. I designed this system to use a cantilevered beam hidden behind the top crown that the door rides on with no visible hardware on the floor. Due to the weight of the wooden sliding bookcase, I calculated loads, resultant forces, and stresses to ensure perfect functionality and structural integrity.",
                "class": "slider",
                "project_name": "Sliding Bookcase",
            },
        },
    },
    "school": {
        "portfolio_name": "Academic Projects",
        "portfolio_description": """Here are a couple of the many projects I worked on while at ASU. Apart from the projects below, I had many unique opportunities to work with professors on projects relating to heat transfer, aerodynamics, FEA, CFB, and much more. Being a member of Barrett, the Honors College, I was also able to publish an undergraduate thesis on mechanical clock design that can be found <a href="https://keep.lib.asu.edu/items/192074">here</a>.""",
        "portfolio_projects": {
            "NG": {
                "description": "For nearly a year, I worked with the SSST Coyote Target Vehicle team at Northrop Grumman to design and construct a mass property measurement device to measure mass, CG, MOI, and POI of launch vehicle components. This device uses a combination of load cells, a rotary encoder, and a torsional spring used to induce oscillatory motion. This project gave me great experience in the defense industry and in launch vehicles.",
                "class": "ng",
                "project_name": "Launch Vehicle Mass Property Measurement Device",
            },
        },
    },
}


def generate_html(info_dict: dict, image_directory: Path) -> str:
    html = ""
    for key, value in info_dict.items():
        isotope_filter = "".join([f", #{k} > *:not(.isotope-hidden)" for k in info_dict.keys() if k != key])
        html_portfolio_section = (
            f"""<section id="portfolio{key}" class="page-section section appear clearfix secPad">"""
            + """\n  <div class="container">"""
            + """\n    <div class="heading">"""
            + f"""\n      <h2>{value["portfolio_name"]}</h2>"""
            + f"""\n      <p>{value["portfolio_description"]}</p>"""
            + """\n    </div>"""
            + """\n    <div class="row">"""
            + """\n      <nav id="filter" class="col-md-12">"""
            + """\n        <ul>"""
        )
        html_section_header = f"""\n          <li><a href="#" class="current btn-theme btn-small" data-filter="#{key} > *{isotope_filter}">All</a></li>"""
        html_section = (
            """\n      <div class="col-md-12">"""
            + """\n        <div class="row">"""
            + f"""\n          <div class="portfolio-items isotopeWrapper clearfix" id="{key}">"""
        )

        portfolio_image_directory = image_directory / key
        for item in portfolio_image_directory.rglob("*"):
            if item.is_dir():
                if item.name in value["portfolio_projects"].keys():
                    # TODO Create a data-filter modifier in the form #thissection, #othersection > *:not(isotope-hidden), #othersection2 > *:not(isotope-hidden)...
                    html_section_header += f"""\n          <li><a href="#" class="btn-theme btn-small" data-filter="#{key} > .{value["portfolio_projects"][item.name]["class"]}{isotope_filter}">{value["portfolio_projects"][item.name]["project_name"]}</a></li>"""
                    html_section += f"""\n            <!-- {value["portfolio_projects"][item.name]["project_name"]} -->"""
                    for file in item.rglob("*"):
                        if file.is_file():
                            html_section += f"""\n            <article class="col-sm-4 isotopeItem {value["portfolio_projects"][item.name]["class"]}">"""
                            html_section += f"""\n              <div class="portfolio-item"> <img src="{str(file)}" alt="" />"""
                            html_section += """\n              <div class="portfolio-desc align-center">"""
                            html_section += f"""\n                <div class="folio-info"> <a href="{str(file)}" class="fancybox">"""
                            html_section += f"""\n                <h5>{value["portfolio_projects"][item.name]["project_name"]}</h5>"""
                            html_section += f"""\n                <h6>{value["portfolio_projects"][item.name]["description"]}</h6>"""
                            html_section += """\n                <i class="fa fa-plus-square-o fa-2x"></i></a> </div>"""
                            html_section += """\n              </div>"""
                            html_section += """\n              </div>"""
                            html_section += """\n            </article>"""
        html_section_header += """\n        </ul>"""
        html_section_header += """\n      </nav>"""
        html_section += """\n          </div>"""
        html_section += """\n        </div>"""
        html_section += """\n      </div>"""
        html_portfolio_section += html_section_header
        html_portfolio_section += html_section
        html_portfolio_section += """\n    </div>"""
        html_portfolio_section += """\n  </div>"""
        html_portfolio_section += """\n</section>"""
        html += "\n\n" + html_portfolio_section
    return html


def write_html_to_document(html_content: str, html_document_directory: str, start_comment: str = "<!-- START COPY PASTE -->", end_comment: str = "<!-- END COPY PASTE -->") -> None:
    with open(html_document_directory, "r", encoding="utf-8") as f:
        html_doc_current = f.read()

    start = html_doc_current.find(start_comment)
    end = html_doc_current.find(end_comment)

    if start == -1 or end == -1:
        raise ValueError("Start or end comment not found in the file.")
    
    # Calculate the exact positions to replace content
    start += len(start_comment)
    
    # Create the new content
    updated_content = html_doc_current[:start] + "\n" + html_content + "\n" + html_doc_current[end:]
    
    # Write the updated content back to the file
    with open(html_document_directory, 'w', encoding="utf-8") as file:
        file.write(updated_content)


if __name__ == "__main__":
    """
    Modify the contents of info_dict and then run the script
    """

    html = generate_html(info_dict=INFO_DICT, image_directory=Path("./images/projects"))
    write_html_to_document(html_content=html, html_document_directory="./index.html")

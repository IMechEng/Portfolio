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
}


def generate_html(info_dict: dict, image_directory: Path) -> str:
    html_doc = """    <div class="row">"""
    html_doc += """\n      <nav id="filter" class="col-md-12">"""
    html_doc += """\n        <ul>"""
    html_section_header = """\n          <li><a href="#" class="current btn-theme btn-small" data-filter="*">All</a></li>"""
    html_section = """\n      <div class="col-md-12">"""
    html_section += """\n        <div class="row">"""
    html_section += """\n          <div class="portfolio-items isotopeWrapper clearfix" id="3">"""

    for item in image_directory.rglob("*"):
        if item.is_dir():
            if item.name in info_dict.keys():
                html_section_header += f"""\n          <li><a href="#" class="btn-theme btn-small" data-filter=".{info_dict[item.name]["class"]}">{info_dict[item.name]["project_name"]}</a></li>"""
                html_section += f"""\n            <!-- {info_dict[item.name]["project_name"]} -->"""
                for file in item.rglob("*"):
                    if file.is_file():
                        html_section += f"""\n            <article class="col-sm-4 isotopeItem {info_dict[item.name]["class"]}">"""
                        html_section += f"""\n              <div class="portfolio-item"> <img src="{str(file)}" alt="" />"""
                        html_section += """\n              <div class="portfolio-desc align-center">"""
                        html_section += f"""\n                <div class="folio-info"> <a href="{str(file)}" class="fancybox">"""
                        html_section += f"""\n                <h5>{info_dict[item.name]["project_name"]}</h5>"""
                        html_section += f"""\n                <h6>{info_dict[item.name]["description"]}</h6>"""
                        html_section += """\n                <i class="fa fa-plus-square-o fa-2x"></i></a> </div>"""
                        html_section += """\n              </div>"""
                        html_section += """\n              </div>"""
                        html_section += """\n            </article>"""
    html_section_header += """\n        </ul>"""
    html_section_header += """\n      </nav>"""
    html_section += """\n          </div>"""
    html_section += """\n        </div>"""
    html_section += """\n      </div>"""
    html_doc += html_section_header
    html_doc += html_section
    html_doc += """\n    </div>"""
    return html_doc


def write_html_to_document(html_content: str, html_document_directory: str, start_comment: str = "    <!-- START COPY PASTE -->", end_comment: str = "    <!-- END COPY PASTE -->") -> None:
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

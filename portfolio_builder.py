from pathlib import Path


if __name__ == "__main__":
    """
    <article class="col-sm-4 isotopeItem hspd">
        <div class="portfolio-item"> <img src="images/projects/1/highsecuritypocketdoor2.JPG" alt="" />
        <div class="portfolio-desc align-center">
            <div class="folio-info"> <a href="images/projects/1/highsecuritypocketdoor2.JPG" class="fancybox">
            <h6>This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.</h6>
            <i class="fa fa-plus-square-o fa-2x"></i></a> </div>
        </div>
        </div>
    </article>
    """

    info_dict = {
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

    out_file = "./portfolio_sections.txt"
    directory = Path("./images/projects")

    with open(out_file, 'w') as f:
        for item in directory.rglob("*"):
            if item.is_dir():
                html_section = f"""\n<!-- {info_dict[item.name]["project_name"]} -->"""
                for file in item.rglob("*"):
                    if file.is_file():
                        html_section += f"""\n<article class="col-sm-4 isotopeItem {info_dict[item.name]["class"]}">"""
                        html_section += f"""\n  <div class="portfolio-item"> <img src="{str(file)}" alt="" />"""
                        html_section += """\n  <div class="portfolio-desc align-center">"""
                        html_section += f"""\n    <div class="folio-info"> <a href="{str(file)}" class="fancybox">"""
                        html_section += """\n    <h6>This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.</h6>"""
                        html_section += """\n    <i class="fa fa-plus-square-o fa-2x"></i></a> </div>"""
                        html_section += """\n  </div>"""
                        html_section += """\n  </div>"""
                        html_section += """\n</article>"""
                f.write(html_section)
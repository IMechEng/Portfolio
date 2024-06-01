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
            "description": "This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.",
            "class": "hspd",
            "project_name": "High Security Pocket Door",
        },
        "2": {
            "description": "This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.",
            "class": "sbc",
            "project_name": "Security Bookcase",
        },
        "3": {
            "description": "This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.",
            "class": "dd",
            "project_name": "Double Door",
        },
        "4": {
            "description": "This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.",
            "class": "stair",
            "project_name": "Hidden Stairs with Trap Door",
        },
        "5": {
            "description": "This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.",
            "class": "vandoor",
            "project_name": "Bi-directional Pocket Door",
        },
        "6": {
            "description": "This is a really cool door that does some door stuff. I really like doors a lot because I'm Ian.",
            "class": "gbc",
            "project_name": "Bookcase Door",
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
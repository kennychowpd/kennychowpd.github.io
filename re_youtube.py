import re


def main():
    print(parse(input("HTML: ")))
    

def parse(s):
    
    if match := re.search(r"^<iframe[\w|\W]+src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"[\w|\W]+></iframe>$", s):
        # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        vid_code = match.group(1)

        return f"https://youtu.be/{vid_code}"
    
    
    
if __name__ == "__main__":
    main()
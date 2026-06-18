import os
import re
import glob

def get_wiki_file_page(url):
    if '/thumb/' in url:
        parts = url.split('/')
        # Example: .../thumb/f/f5/Roomba_original.jpg/330px-Roomba_original.jpg
        # parts[-1] is 330px-Roomba_original.jpg
        # parts[-2] is Roomba_original.jpg
        filename = parts[-2]
    else:
        filename = url.split('/')[-1]
    
    return f'https://commons.wikimedia.org/wiki/File:{filename}'

def main():
    chapter_files = glob.glob('chapters/*.md')
    # Use a dict to store alt text for each image page to avoid duplicates and keep credits clean
    credits = {}
    
    # Regex to find ![alt](url)
    img_regex = re.compile(r'!\[([^\]]*)\]\((https://upload\.wikimedia\.org/wikipedia/commons/[^\)]+)\)')
    
    for filepath in chapter_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = img_regex.findall(content)
            for alt, url in matches:
                page = get_wiki_file_page(url)
                if page not in credits:
                    credits[page] = alt if alt else 'Image'

    if not credits:
        print('No Wikipedia images found.')
        return

    with open('chapters/92-image-credits.md', 'w', encoding='utf-8') as f:
        f.write('# Image Credits\n\n')
        for page, alt in sorted(credits.items()):
            f.write(f'- [{alt}]({page}) ({page})\n')

if __name__ == '__main__':
    main()

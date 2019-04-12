# First scrape and file creation

def motivational_quote_scrape(html_link, newfile):
    text_list = get_text(html_link)
    text_list = filter_quotes(text_list)
    # text_list = text_list[start_index:-1]
    text_list = digit_cleaner(text_list)
    overwrite_to_file(text_list, newfile)
    print('Function Completed')
    return ''

def get_text(html_link):
    import requests
    import lxml.html
    from pprint import pprint

    html = requests.get(html_link)
    docs = lxml.html.fromstring(html.content)
    header = docs.xpath('//span[@id="hs_cos_wrapper_post_body"]')
    text_list = []
    for line in header:
        text_list.extend(line.text_content().strip().split("\n"))
    print('Scrapping complete')
    return text_list

def filter_quotes(text_list):
    new_text_list = [line for line in text_list if len(line) > 0 if line[0].isdigit() == True]
    return new_text_list

def overwrite_to_file(text_list, newfile):
    with open(newfile, 'w+') as f:
        for line in text_list:
            f.write(line + '\n')
    print('New file created')
    return ''

def digit_cleaner(text_list):
    new_text_list = []
    for line in text_list:
        start_space_i = line.find(' ')
        new_text_list.append(line[start_space_i+1:])
    return new_text_list

motivational_quote_scrape('https://blog.hubspot.com/sales/18-motivational-quotes-to-start-your-day-list',
    'quotes.txt')
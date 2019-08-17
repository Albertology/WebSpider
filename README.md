# WebSpider
An program that searches websites for pages that follow expressions or, simply bruteforces the website

Disclaimer: This should not be used for illegal activity and I am not responsible for it's use

# Uses
    python webspider.py [-h] website expression [--wrong_pages WRONG_PAGES] [--extension EXTENSION] 
                   [--max_length MAX_LENGTH]
                   [--last_file LAST_FILE] 
                   [--display_possible DISPLAY_POSSIBLE]
                    
    website -website you want to scan. Path inside the site is accepted: https://example.com/test1/test2/
    expressions -list of expressions. For bruteforce leave each element empty
    wrong_pages -path to file with examples of wrong pages
    extension -last file extension. Only appended if last-file is true
    max_length -used in bruteforce to specify max length of each part of the url
    last_file -used for specifying if the last part of the url is a file
    display_possible -if return_status is not 200 and this is true it also displays the ones without (Will be removed in the next version)
    
# Expressions

Can contain:

Any ascii characters(that may be used in an url)

Special sequences:

    /d all digits <=> '[0-9]'
    /l all small letters <=> '[a-z]'
    /L all big letters <=> '[A-Z]'
    
Note: this tool uses forwrd slashes for simplicity, though it may be changed in later versions

Sets(similar to regex sets):

    '[abc]' will match(generate) 'a' -> 'b' -> 'c' 
    '[a-z]' will generate 'a' -> 'b' -> 'c' -> ... -> 'z'
    '[a/-z]' will generate 'a' -> '-' -> 'z' (because '-' is excaped)
    '[a-]' will generate 'a' -> '-' (incomplete set)

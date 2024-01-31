from html import unescape
import re

def remove_duplicates(string):
    # Strip HTML tags
    string = re.sub(r'<[^>]*>', '', string)
    
    # Remove duplicates
    words = re.split(r'\s+', string) 
    result = []
    current_word = ''
    for word in words:
        # Only unescape HTML entities 
        word = unescape(word.strip(), {"&apos;": "'", "&quot;": '"', "&gt;": ">", "&lt;": "<", "&amp;": "&"})  
        if current_word and word:
            current_word += ' ' + word
        else:
            current_word = word
            if current_word not in result:
                result.append(current_word)  
    return ' '.join(result)

print(remove_duplicates('<span class="voteIssues" id="voteIssues635701">Justice & Democracy<span style="display:none" class="voteIssuesFULL" id="voteIssues635701FULL"> Justice and Democracy,</span></span>'))
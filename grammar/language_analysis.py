from dharmamitra_sanskrit_grammar import DharmamitraSanskritProcessor
import re
from indic_transliteration import sanscript

def split_verse(verse):

    verse_iast = sanscript.transliterate(verse, 'devanagari', 'iast').replace("|", ".")

    analysis = DharmamitraSanskritProcessor().process_batch(
        verse_iast,
        mode="unsandhied-lemma-morphosyntax",  # or 'unsandhied' or 'unsandhied-lemma-morphosyntax'
        human_readable_tags=False
    )

    verse_split=""

    for chunk in analysis:
        # print(chunk['sentence'])

        result = chunk['sentence'] + '|'
        tokens = chunk["grammatical_analysis"]
        for i, token in enumerate(tokens):
            word = token["unsandhied"]
            tag = token["tag"]
            lemma = token["lemma"]
            # print(f"{i}: \t{word}; {tag}; {lemma}")

            # Special cases that are weird in Dharmamitra
            if word == 'sa' and lemma == 'tad': word = 'saḥ'

            if tag == 'Case=Cpd':
                result += word
            else:
                if not (i == len(tokens) - 1):
                    result += word + '_'
                elif not chunk['sentence'][-1]=='.':
                    result += word + ' '
                else:
                    if(chunk['sentence'][-2]=='.'):
                        # print(f"here for {word}, {result}")
                        result += word + '..'
                    elif(chunk['sentence'][-1]=='.'): result += word + '.'
        if not tokens:
            result = result[:-1] + ' '
        verse_split += result

    verse_split=verse_split.replace('.','X')

    verse_split_dn = sanscript.transliterate(verse_split, 'iast', 'devanagari')
    verse_split_dn = verse_split_dn.replace('।', '|').replace('XX', '॥').replace('X', '।')

    verse_split_dn = re.sub(r'।(?!\|)', '।\n', verse_split_dn)

    return verse_split_dn

if __name__ == "__main__":
    test = """
वृत्तं गुरूपरि लिखेदथ किन्तु शब्दानाचार्यशिक्षकगुरूनिह न प्रयुञ्ज्यात्।
   वृत्तार्धयोरुभययोरपि कश्चिदङ्कः सङ्ख्यैक्यमत्र नव चेद्वरमस्तु तर्हि॥
"""
    print(split_verse(test))
    # print(format_verse_block(test))


    # match = Chandas.classify(test)

    # print(match)
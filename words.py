from time import *

text = """
Early sales of Apple's new iPhones have lived up to high expectations.

The strong sales mirror growing consumer demand for smartphones with bigger
screens. IDC, a research firm, estimated that at least 20 percent of all
smartphones shipped last year in China, the largest smartphone market in
the world, were five inches or larger. It also predicted that manufacturers
this year would ship more "phablets," or smartphones with screens measuring
at least 5-point-5 diagonal inches, than laptops.

The company on Monday said it sold more than 10 million of the iPhone 6 and
6 Plus models in the first three days they were available in stores. That
is higher than the nine million new iPhones it sold last year in their
first weekend on sale. But some analysts, like Gene Munster of Piper
Jaffray, wondered whether first-weekend sales were still a reliable measure
for consumer demand.

The iPhone sales were on the upper end of financial analysts' expectations,
which ranged from 6 million to the "low teens" of millions of sales.
"""

# User Benchmark or Print Results ?
BENCHMARK = True


# function to print result with some info
def print_info(result):
    if not BENCHMARK:
        print(result)


# receive many keywords as you wish
def search_word(text, keywords):
    print_info("search_word =======")
    for sentence in text.split("."):
        if all(x in sentence for x in keywords ):
            print_info(sentence)


# receive only two keywords
def ugly_search(text,keyword1,keyword2):
    print_info("ugly_search =======")
    for sentence in text.split("."):
        for word in sentence.split():
                if word == keyword1:
                        for word2 in sentence.split():
                                if word2 == keyword2:
                                    print_info(sentence)


# receive only two keywords
def less_ugly_search(text, keyword1, keyword2):
    print_info("less_ugly_search =======")
    for sentence in text.split("."):
        if keyword1 in sentence.split():
                if keyword2 in sentence.split():
                    print_info(sentence)


def timing(func, text, keywords, count):
    i = time()
    for n in range(count):
        func(text, keywords)
    print('Time measured: '+func.__name__+':', time()-i)


def timing_ugly(func, text, keyword1, keyword2, count):
    i = time()
    for n in range(count):
        func(text, keyword1, keyword2)
    print('Time measured: '+func.__name__+':',time()-i)

if __name__ == '__main__':
    # Change the keywords below as you wish
    keywords = ("iPhone", "company")

    if BENCHMARK:
        timing(search_word,text,keywords,1000000)
        timing_ugly(ugly_search,text,"iPhone","company",1000000)
        timing_ugly(less_ugly_search,text,"iPhone","company",1000000)
    else:
        search_word(text, keywords)
        ugly_search(text, "iPhone", "company")
        less_ugly_search(text, "iPhone", "company")

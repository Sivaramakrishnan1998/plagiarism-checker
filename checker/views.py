from django.shortcuts import render
from .forms import DataForm,DocumentForm
from urllib.parse import urlencode, urlparse, parse_qs
from lxml.html import fromstring
from requests import get
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import random
import re, math
from collections import Counter
from django.http import HttpResponseRedirect
from .models import Document,Data



browsers = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 Firefox/3.0.6',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Firefox/3.0.6',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Firefox/3.0.6',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.5) Gecko/2008121621 Ubuntu/8.04 (hardy) Firefox/3.0.5',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
            ]

WORD = re.compile(r'\w+')
headers={
	'User-Agent': browsers[random.randint(0, len(browsers) - 1)],
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5'
	}
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
         d1 = float(numerator) / denominator
         print(d1)
         return d1
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
def calplag(file1_data,file2_data):

    text1 = file1_data
    text2  = file2_data
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = get_cosine(vector1, vector2)
    print ('Cosine:', cosine)
    return cosine




def dataextract(urllist,textss):
    f = open('file1.txt','w')
    f.truncate()
    f.close()
    toplist = urllist[:1]
    for l in toplist:

        print(l)
        if (l!='/' and len(l)>2):
            html = get('http://%s'%(l),verify = False,headers = headers).text
            soup = BeautifulSoup(html)
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()
                # get text
            text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            z = open('file1.txt','a')
            z.write(text)
            z.close()
            print(text)
    d1 = open('file1.txt','r')

    file1_data = d1.read()
    file2_data = textss
    similarity_ratio = calplag(file1_data,file2_data)
    #similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    d1.close()

    return similarity_ratio


def geturls(req,text):
    urllist = []
    abstractlist = []
    list3 = []




    if not list3:
        raw = get("http://www.ask.com/web?q=%s&o=0&qo=homepageSearchBox"%(text),headers = headers,verify = False).text
        soup = BeautifulSoup(raw,'lxml')
        resultobj = soup.findAll('div', {'class': 'PartialSearchResults-item'})
        abstractobj = soup.findAll('p',{'class':'PartialSearchResults-item-abstract'})
        for resul in resultobj:
            resindex = resul.find('p')
            if resindex!=None:
                urllist.append(resindex.text)
        for abst in abstractobj:
            if abst != None:
                abstractlist.append(abst.text)
        list3 = list(zip(urllist,abstractlist))
        result = dataextract(urllist,text)


        print(list3)
        print('\n\n\n\nscraped from ask')


    return render(req,'plag.html',{'links':list3,'result':result*100})

# Create your views here.
def check(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            post = form.save(commit =False)
            post.user = request.user
            post.save()
            cd = form.cleaned_data
            text1 = cd['data']

            x = open('file2.txt','w')
            x.truncate()
            x.close()
            x = open('file2.txt','a')
            x.write(text1)
            x.close

            return geturls(request,text = text1)
    else:
        form = DataForm()

    return render(request,'getdata.html',{'form':form})


#
# def home(request):
#     documents = Document.objects.all()
#     return render(request, 'home.html', { 'documents': documents })
#

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

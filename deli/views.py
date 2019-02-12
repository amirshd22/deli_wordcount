from django.shortcuts import render
import operator



def home(request):
    return render(request, 'idex.html')


def count(request):
    deli = request.GET['fulltext']
    delilist = deli.split()
    delinum = len(delilist)
    delidic = {}
    for word in delilist:
        if word in delidic:
            #increase
            delidic[word] += 1
        else:
            #add to the dictionary
            delidic[word] = 1

    sorteddeli =  sorted(delidic.items(), key= operator.itemgetter(1),reverse =True)
    return render(request, 'count.html',{'text':deli,'count': len(delilist), 'sortedtext': sorteddeli,'counted': delinum })
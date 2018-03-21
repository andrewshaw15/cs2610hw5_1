from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

import datetime
from time import strftime

from .models import Blog, Comments

def main(request):
    return render(request, 'blog/main.html', { 'current_time' : strftime('%c') })

def bio(request):
    return render(request, 'blog/bio.html', { 'current_time' : strftime('%c') })

def techTips(request):
    return render(request, 'blog/tech-tips.html', { 'current_time' : strftime('%c') })

def starWars(request):
    return redirect('http://www.starwars.com/')

def airForce(request):
    return redirect('http://www.af.mil/')

def usu(request):
    return redirect('https://www.usu.edu/')

def commonGitCommands(request):
    return redirect('http://guides.beanstalkapp.com/version-control/common-git-commands.html')

def basicGitCommands(request):
    return redirect('https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html')

def gitReference(request):
    return redirect('https://git-scm.com/docs')

def home(request):
    latest_blog_list = Blog.objects.order_by('-post_date')[:3]
    return render(request, 'blog/home.html', {
        'latest_blog_list': latest_blog_list,
        'current_time' : strftime('%c'),
    })

def archive(request):
    all_blog_list = Blog.objects.order_by('-post_date')
    return render(request, 'blog/archive.html', {
        'all_blog_list': all_blog_list,
        'current_time' : strftime('%c'),
    })

def entry(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/entry.html', {
        'blog': blog,
        'current_time': strftime('%c'),
    })

def new_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    new_nickname = request.POST['nickname']
    new_email = request.POST['email']
    new_content = request.POST['content']
    new_comment = blog.comments_set.create(nickname=new_nickname, email=new_email, content=new_content, post_date=timezone.now())
    new_comment.save()
    return HttpResponseRedirect(reverse('blog:entry', args=(blog.id,)))

def init(request):
    Blog.objects.all().delete()
    b1 = Blog(title="Blog Guidelines", author="Admin", 
        content="""Mauris ornare nisl in mauris placerat luctus. Nullam dolor nibh, viverra condimentum dictum mollis, viverra nec nunc. Nunc ut ullamcorper nisi. Maecenas fermentum diam quis dolor tincidunt, at condimentum eros tincidunt. Proin accumsan libero vel mi hendrerit, et tristique purus rutrum. Maecenas id sagittis diam. Integer vitae gravida ex. Phasellus egestas dignissim justo eu consequat. Cras ultricies odio magna, tempor volutpat elit condimentum at. Duis lorem libero, venenatis eu urna ac, tempor varius leo. Nulla facilisi. Donec eu neque ultricies, malesuada lectus ut, cursus nibh. Phasellus arcu ligula, tincidunt at dui ut, imperdiet ultrices quam. Etiam euismod nec massa at ultrices. Fusce sit amet diam quis risus suscipit facilisis in vel metus. Etiam dolor elit, sagittis et magna non, accumsan fringilla felis.

Cras pharetra nibh sagittis, pharetra nunc quis, blandit velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nunc rutrum sapien eu nibh efficitur, bibendum convallis urna tempor. Morbi nec mi vulputate, finibus elit eu, aliquam mauris. Phasellus et velit hendrerit, rutrum ante et, mattis sem. Pellentesque maximus posuere gravida. Aenean bibendum erat eu mi fermentum gravida eget sit amet arcu. Etiam iaculis finibus sem, a consequat ex faucibus eget. Sed auctor risus vel risus feugiat tempor. Praesent iaculis libero sit amet rhoncus molestie. Duis dapibus arcu enim, posuere consectetur diam pulvinar sit amet. Curabitur facilisis sodales tincidunt.

Nunc tristique, leo vel vehicula molestie, tellus orci auctor velit, a vulputate augue nibh quis nibh. Duis id dolor sit amet tellus sodales ullamcorper. Nam commodo tortor vitae mauris venenatis luctus. Nunc vestibulum at ligula et volutpat. Curabitur vel arcu eget eros venenatis tempus. Nam vitae commodo odio, in maximus libero. Donec placerat eros viverra, tincidunt tellus sed, efficitur ex. Aenean dapibus vestibulum nisl, non convallis augue rhoncus quis. Suspendisse sit amet pretium mauris, vitae pharetra nunc. Maecenas sit amet nibh pulvinar, vestibulum tellus sit amet, elementum libero. Aliquam tempor vel erat sit amet tincidunt. Aliquam facilisis nisl quis augue placerat iaculis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam nec urna urna. Morbi porttitor, ipsum id egestas euismod, felis nisi lacinia felis, at finibus lacus dui ac mauris.

Maecenas magna nulla, porta et aliquet ac, semper quis tortor. Quisque rutrum vitae lacus vehicula aliquam. Cras non lorem bibendum, mattis erat eu, posuere nisl. Duis id bibendum elit. Nulla sodales justo vel nulla pellentesque pretium. Nullam a dictum erat. Quisque nec ante ut nisl hendrerit hendrerit nec ut sapien. Integer quis pellentesque massa, varius varius diam. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec maximus sed urna non finibus. Curabitur id enim a magna auctor vestibulum eget malesuada nibh. Praesent nec neque non dolor dignissim auctor at quis nisi.

Cras aliquet nisl lacus, vel viverra diam dapibus sit amet. Sed bibendum imperdiet justo nec lacinia. Vestibulum ac pharetra dui, sit amet elementum turpis. Sed vel tellus ut sapien porta sodales ac ac risus. Ut non orci augue. Curabitur nec aliquet mi. Nam maximus tincidunt enim, ut aliquet turpis condimentum non. Pellentesque semper, augue sit amet vehicula varius, dui lorem feugiat mi, vitae sagittis nisl orci id lectus. Sed in dui ut arcu cursus aliquam eget in massa. Etiam maximus malesuada felis, et mollis nibh efficitur ornare. Cras pretium mauris eget mi scelerisque porta. Donec tincidunt a turpis non mollis. Proin ut ex urna. Cras sed sapien nunc.""", 
        post_date=timezone.now()-datetime.timedelta(days=7))
    b1.save()
    b1.comments_set.create(nickname="Hender", email="hender@email.com", 
        content="Aenean lobortis sed ante in finibus. Phasellus congue faucibus justo in dignissim. Curabitur ut erat non mauris suscipit viverra. Sed feugiat viverra nisl nec cursus. Cras venenatis, magna id dapibus gravida, sapien neque vulputate arcu, ut molestie mauris est ut libero. Aenean non feugiat ipsum, vel varius urna. Vestibulum vitae tellus id risus facilisis blandit ut in mi. Donec elementum auctor nibh dignissim tempus. In arcu orci, ullamcorper quis tellus finibus, tempus convallis turpis. Donec consequat elementum nulla at aliquam.", 
        post_date=timezone.now()-datetime.timedelta(days=6))
    b1.comments_set.create(nickname="Meg", email="meg@email.com",
        content="Quisque felis lectus, sodales eu mi eget, ullamcorper feugiat magna. Curabitur imperdiet sapien urna, nec fringilla nisi iaculis mattis. Pellentesque augue nunc, accumsan at ornare at, sodales sit amet mi. Quisque rutrum lorem eu mauris commodo, non vehicula sapien laoreet. Etiam posuere, lorem ut fringilla scelerisque, eros leo blandit dui, cursus dapibus risus dolor eget ipsum. Phasellus convallis bibendum leo at accumsan. Cras ut felis turpis. Aliquam imperdiet velit non gravida accumsan. Vivamus consequat sapien vel eros viverra, sit amet ornare nisl elementum. Etiam at rutrum felis. Vestibulum volutpat eget risus eget aliquet. Ut posuere sem eu pretium molestie.",
        post_date=timezone.now()-datetime.timedelta(days=5))
    b1.comments_set.create(nickname="Hobbles", email="hobbles@email.com",
        content="Vivamus risus magna, lobortis a sodales maximus, pulvinar in velit. Proin mattis lacus congue facilisis pharetra. Integer nec felis lacus. Phasellus pharetra tortor dui, placerat sodales mauris condimentum id. Ut augue est, lobortis aliquam rutrum quis, commodo ac nisl. Mauris sit amet ante eu lorem facilisis commodo. Nam dolor justo, luctus ac tortor quis, semper semper tortor. Proin et lacinia odio.",
        post_date=timezone.now()-datetime.timedelta(days=4))
    b1.comments_set.create(nickname="Ju", email="ju@email.com",
        content="Nulla et mattis augue. In mattis, justo eu vehicula maximus, augue est condimentum ipsum, et tincidunt ex mauris vel odio. Donec vulputate pretium purus, nec posuere libero porttitor dignissim. Sed dignissim ipsum vitae elit semper, a consectetur odio cursus. Integer lacinia viverra ipsum non gravida. Nulla pellentesque iaculis pellentesque. Nam eu nisl sem. Proin ultrices pretium dolor. Maecenas convallis, purus in eleifend dignissim, quam neque tristique leo, vel vehicula erat enim id tellus. Nulla ac suscipit quam. Phasellus rhoncus tortor nec cursus elementum. Nulla vestibulum nulla ut dignissim fringilla. Suspendisse at libero sit amet ligula mollis finibus. Praesent in ligula mi. Maecenas commodo ante felis, eget eleifend diam vestibulum a.",
        post_date=timezone.now()-datetime.timedelta(days=3))

    b2 = Blog(title="Hender's Blog", author="Hender",
        content="""Suspendisse at tellus vitae eros aliquet commodo. Vivamus pulvinar turpis mi, eget tristique turpis facilisis vitae. Pellentesque et tincidunt odio. Suspendisse varius nibh et magna ultricies, nec feugiat metus rhoncus. Praesent mi massa, ultricies eu tellus vel, auctor finibus quam. Vestibulum ullamcorper tempor mauris at blandit. Aenean vitae tellus in felis porta imperdiet quis in elit. Ut porttitor sem ut tellus commodo, at viverra mi efficitur.

Quisque luctus purus vitae magna consectetur venenatis. Morbi scelerisque erat non purus tempor eleifend. Vivamus cursus imperdiet tellus, ac iaculis felis scelerisque in. Phasellus in mi in tellus bibendum egestas ac vitae felis. Maecenas a nibh vitae urna aliquam viverra. Mauris at facilisis massa. Nulla nec turpis ac orci blandit tincidunt nec id dolor. Etiam blandit pharetra consequat. Donec congue, enim quis ultricies pretium, sapien ex rutrum tortor, non fringilla orci est vitae nulla.

Praesent rutrum commodo dignissim. Ut condimentum lorem eu odio malesuada auctor. Duis euismod vel quam id faucibus. Pellentesque cursus diam sed eros porttitor maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ullamcorper ultricies enim, id fringilla libero pulvinar id. Nam vitae molestie quam. Vivamus nisi justo, finibus vitae dui at, consectetur lacinia libero. Suspendisse accumsan pretium sagittis. Integer ultricies libero vel urna eleifend sodales. Cras nibh elit, sodales ut urna non, venenatis eleifend ante. In tellus ex, fermentum vitae laoreet vel, scelerisque eget elit. Donec euismod posuere lectus, eget tempor orci molestie vitae. In in libero euismod, sodales felis at, pharetra ex.""",
        post_date=timezone.now()-datetime.timedelta(days=6))
    b2.save()
    b2.comments_set.create(nickname="Meg", email="meg@email.com",
        content="Nam sed ipsum dolor. Morbi sit amet enim libero. Maecenas diam nisl, ornare vel erat eu, efficitur maximus risus. Phasellus sit amet euismod nisl. Nunc posuere vitae nisi a egestas. Vivamus turpis diam, lobortis vitae vehicula nec, molestie sit amet arcu. Nulla in fermentum massa. Fusce ac erat vel augue pulvinar dictum.",
        post_date=timezone.now()-datetime.timedelta(days=5))
    b2.comments_set.create(nickname="Hobbles", email="hobbles@email.com",
        content="Suspendisse aliquet leo leo, eget dapibus purus lacinia nec. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus cursus nunc ut metus imperdiet fermentum. Sed dapibus condimentum ipsum ut ultrices. Aenean sodales commodo arcu id lacinia. Nam nec neque rhoncus, maximus risus in, commodo nunc. Nullam convallis, eros ac ultrices molestie, turpis sapien tempor diam, vel porttitor nunc dui id magna. Aenean sed ultrices odio. Proin varius lorem sed ex facilisis dapibus.",
        post_date=timezone.now()-datetime.timedelta(days=4))
    b2.comments_set.create(nickname="Ju", email="ju@email.com",
        content="Aliquam ultrices orci eget mauris convallis sagittis. Suspendisse quis mauris sodales, vehicula mi sed, semper arcu. Nullam vel tincidunt quam. Sed nec mauris ut massa egestas pretium. Pellentesque rutrum, quam ac condimentum suscipit, dui purus eleifend diam, vel rhoncus nisl neque eget nunc. In lectus quam, sodales vitae ligula vitae, dictum euismod eros. In sed rhoncus mi. Cras facilisis erat id mauris eleifend sagittis. Pellentesque lorem lorem, molestie nec elementum nec, varius ac libero. Nullam fringilla sagittis varius.",
        post_date=timezone.now()-datetime.timedelta(days=3))

    b3=Blog(title="Meg's Blog", author="Meg",
        content="""Mauris eleifend suscipit lacus, vitae viverra nisi suscipit sit amet. Aliquam ornare accumsan convallis. Sed eget sagittis lacus, a accumsan dolor. Curabitur aliquam vestibulum cursus. Nulla imperdiet lacinia sem in eleifend. Integer nec commodo felis. Mauris id augue dignissim odio congue pulvinar id ac magna. Morbi quis nisl non velit eleifend elementum sit amet sit amet nulla.

Sed sit amet odio vitae velit fermentum pellentesque. Sed odio libero, dapibus at condimentum mattis, vestibulum et libero. Vivamus a faucibus felis. Vivamus quis ex vel lacus volutpat tempor in in justo. Vestibulum interdum, lectus laoreet pulvinar condimentum, velit lorem aliquam tortor, et eleifend velit lorem a arcu. Nulla ut metus facilisis, eleifend erat quis, viverra nisl. Pellentesque consectetur non sem ut iaculis. Integer neque elit, ornare vel risus et, semper cursus nisi. Sed sagittis mollis feugiat.

Curabitur iaculis cursus feugiat. Sed dui neque, facilisis nec aliquet at, dapibus vitae tortor. Sed vestibulum eget turpis vel interdum. Mauris vitae nunc a sapien fermentum volutpat. Nullam placerat vitae justo sit amet mollis. In egestas bibendum ligula, vitae mollis dui lacinia ut. Aenean placerat sagittis laoreet. Proin hendrerit non nisi sit amet molestie. Morbi non augue massa. Nunc ultrices lobortis odio, eget sollicitudin enim blandit a. Praesent id sollicitudin nisl. Fusce at massa sapien. Phasellus ut odio lobortis, volutpat leo egestas, pretium nisl.""",
        post_date=timezone.now()-datetime.timedelta(days=5))
    b3.save()
    b3.comments_set.create(nickname="Hobbles", email="hobbles@email.com",
        content="Sed non nisl ut arcu imperdiet aliquet non sed nunc. Curabitur varius eget mauris a aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam pharetra eros quis nunc rutrum sodales. Maecenas mattis arcu eget massa consectetur faucibus. Suspendisse luctus blandit nunc et luctus. Mauris iaculis odio quis lectus interdum egestas. Fusce ac libero augue. Quisque et sem nulla. Etiam vestibulum egestas libero at eleifend. Donec id sapien neque.",
        post_date=timezone.now()-datetime.timedelta(days=4))
    b3.comments_set.create(nickname="Ju", email="ju@email.com",
        content="Fusce posuere, lorem at placerat suscipit, libero urna viverra arcu, ac mattis quam nisi nec ligula. Suspendisse blandit sodales leo eget aliquet. Mauris eget laoreet odio, vulputate congue lacus. Praesent a consequat dolor. Sed erat tortor, aliquet et porta non, viverra id felis. Praesent pellentesque eleifend quam, feugiat porttitor urna congue in. Duis vehicula imperdiet maximus. Nulla cursus quam nec felis molestie, quis faucibus augue malesuada. Integer euismod, purus sed finibus pretium, tortor felis interdum felis, efficitur cursus ipsum lacus sit amet dui. Vestibulum vulputate dui nulla, nec vestibulum leo ornare a. Nullam vehicula lobortis nulla, et commodo quam convallis non. Quisque nisi libero, rutrum id varius lobortis, fermentum ut odio. Pellentesque et ipsum id urna consequat dictum. Pellentesque tempor massa ut velit accumsan, quis commodo ligula mollis. Aliquam sit amet tortor at massa tincidunt rhoncus. Phasellus nec purus in sapien sagittis maximus at id est.",
        post_date=timezone.now()-datetime.timedelta(days=3))

    b4=Blog(title="Hobbles' Blog", author="Hobbles",
        content="""Phasellus suscipit id risus sit amet congue. Duis convallis augue nec blandit dapibus. Ut accumsan sapien in tristique aliquet. Integer eleifend mi venenatis magna luctus, nec efficitur nibh sagittis. Fusce eros lorem, commodo ut molestie vitae, euismod at risus. Nunc porttitor nisl ut feugiat elementum. In hac habitasse platea dictumst. Donec quis dignissim felis, sit amet auctor risus. Vivamus rutrum magna vitae tortor finibus mollis. Proin consectetur viverra velit vel suscipit. Maecenas aliquet tristique pulvinar.

Suspendisse luctus cursus nibh. Vestibulum posuere vel justo id faucibus. Phasellus gravida arcu lorem, eget condimentum lacus consequat ut. Vestibulum in facilisis lectus. Pellentesque tincidunt quis sapien vel varius. Fusce at lorem pellentesque, lacinia ligula a, tristique lectus. Ut consectetur neque eget tellus pulvinar dictum. Etiam tortor odio, molestie vitae facilisis sed, finibus eget sem. Aenean facilisis, urna nec porttitor sollicitudin, enim velit gravida magna, in ultrices felis nisl vitae nisi. Praesent vehicula elementum mauris vel semper. Quisque lobortis arcu est, mollis finibus augue rhoncus a. Donec massa mi, auctor in nisi non, feugiat ultrices augue. Curabitur sagittis lacus diam, et pellentesque magna dictum ut.

In hendrerit eros ut auctor ornare. Ut cursus dolor quis dapibus suscipit. Vivamus id lobortis est. Integer non sagittis elit. Suspendisse efficitur lacus id diam porta accumsan. Aenean dignissim dignissim lacus. Ut accumsan lacinia lorem ut molestie. Nunc rhoncus lacinia faucibus. Donec porttitor sodales eros in pellentesque. Fusce pellentesque velit cursus venenatis fermentum. Vivamus feugiat elit eu est convallis, ac accumsan velit rhoncus. Donec mollis lobortis fermentum.""",
        post_date=timezone.now()-datetime.timedelta(days=4))
    b4.save()
    b4.comments_set.create(nickname="Ju", email="ju@email.com",
        content="Praesent egestas enim quis lorem egestas, id aliquam arcu interdum. Donec lacinia ac neque id convallis. Nunc pellentesque, neque quis dignissim feugiat, nunc urna vestibulum quam, at vulputate turpis orci eu sapien. Sed ut nunc vitae urna elementum congue non non purus. Morbi a elementum lorem, at ultricies tortor. Phasellus at condimentum velit, sed lobortis urna. Nullam vitae massa mauris. Maecenas sit amet nunc vel eros consequat pharetra. Vestibulum quis pulvinar sem, a condimentum ligula. Cras odio lacus, bibendum quis vestibulum eu, dapibus non ipsum.",
        post_date=timezone.now()-datetime.timedelta(days=3))

    return HttpResponseRedirect(reverse('blog:home'))